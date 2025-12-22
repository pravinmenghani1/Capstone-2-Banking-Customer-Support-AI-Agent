import sqlite3
import random
import re
from typing import Dict, Tuple
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self, db_path="support.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS support_tickets (
                ticket_id TEXT PRIMARY KEY,
                status TEXT,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def insert_ticket(self, ticket_id: str, description: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO support_tickets (ticket_id, status, description) VALUES (?, ?, ?)",
            (ticket_id, "Unresolved", description)
        )
        conn.commit()
        conn.close()
    
    def get_ticket_status(self, ticket_id: str) -> str:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM support_tickets WHERE ticket_id = ?", (ticket_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

class ClassifierAgent:
    def __init__(self):
        self.client = None
    
    def _get_openai_client(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not self.client and api_key and api_key.strip() != "":
            try:
                import openai
                self.client = openai.OpenAI(
                    api_key=api_key
                )
                print(f"✅ OpenAI client created successfully")
                return self.client
            except Exception as e:
                print(f"❌ Failed to create OpenAI client: {e}")
                self.client = None
        return self.client
    
    def classify(self, message: str) -> Dict:
        client = self._get_openai_client()
        if not client:
            raise Exception("OpenAI API key is required for classification")
            
        prompt = f"""You are a banking customer service classifier. Classify this message into EXACTLY ONE category:

POSITIVE_FEEDBACK: Customer is happy, satisfied, thanking, praising, or expressing gratitude
NEGATIVE_FEEDBACK: Customer is complaining, unhappy, reporting problems, or expressing dissatisfaction  
QUERY: Customer is asking about ticket status, requesting information, or checking on something

Examples:
- "Thanks for helping me" → POSITIVE_FEEDBACK
- "I hate your app, it crashes" → NEGATIVE_FEEDBACK  
- "What's the status of ticket 123?" → QUERY
- "It is always best experience" → POSITIVE_FEEDBACK

Message: "{message}"

Respond with ONLY the category name (POSITIVE_FEEDBACK, NEGATIVE_FEEDBACK, or QUERY):"""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20,
            temperature=0
        )
        result = response.choices[0].message.content.strip().upper()
        
        # Map to our format
        if "POSITIVE" in result:
            return {"classification": "positive_feedback", "using_openai": True}
        elif "NEGATIVE" in result:
            return {"classification": "negative_feedback", "using_openai": True}
        elif "QUERY" in result:
            return {"classification": "query", "using_openai": True}
        else:
            return {"classification": "negative_feedback", "using_openai": True}  # Default
    
    def _fallback_classify(self, message: str) -> str:
        message_lower = message.lower()
        
        # Strong negative indicators
        strong_negative = ["hate", "worst", "terrible", "awful", "crashes", "broken", "useless", "horrible", "sucks", "garbage"]
        # Strong positive indicators  
        positive_words = ["thank", "thanks", "great", "excellent", "good", "love", "amazing", "wonderful", "perfect", "smooth", "best", "always best", "experience"]
        # Problem indicators
        problem_words = ["problem", "issue", "error", "not working", "failed", "trouble", "complaint", "bad", "hasn't arrived", "delayed"]
        # Query indicators
        query_words = ["status", "check", "ticket", "what is", "how is", "update"]
        
        # Check for strong negative first
        if any(word in message_lower for word in strong_negative):
            return "negative_feedback"
            
        # Check for queries
        if any(word in message_lower for word in query_words) and any(word in message_lower for word in ["ticket", "status"]):
            return "query"
        
        # Check for strong positive indicators
        if any(word in message_lower for word in positive_words):
            return "positive_feedback"
            
        # Count remaining indicators
        negative_count = sum(1 for word in problem_words if word in message_lower)
        
        if negative_count > 0:
            return "negative_feedback"
        else:
            return "positive_feedback"  # Default to positive if unclear

class FeedbackHandlerAgent:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def handle_positive(self, customer_name: str = "Customer") -> str:
        return f"Thank you for your kind words, {customer_name}! We're delighted to assist you."
    
    def handle_negative(self, message: str) -> str:
        ticket_id = str(random.randint(100000, 999999))
        self.db_manager.insert_ticket(ticket_id, message)
        return f"We apologize for the inconvenience. A new ticket #{ticket_id} has been generated, and our team will follow up shortly."

class QueryHandlerAgent:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def handle_query(self, message: str) -> str:
        ticket_match = re.search(r'#?(\d{6})', message)
        if not ticket_match:
            return "Please provide a valid 6-digit ticket number."
        
        ticket_id = ticket_match.group(1)
        status = self.db_manager.get_ticket_status(ticket_id)
        
        if status:
            return f"Your ticket #{ticket_id} is currently marked as: {status}."
        else:
            return f"Ticket #{ticket_id} not found in our system."

class MultiAgentSystem:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.classifier = ClassifierAgent()
        self.feedback_handler = FeedbackHandlerAgent(self.db_manager)
        self.query_handler = QueryHandlerAgent(self.db_manager)
        self.logs = []
    
    def process_message(self, message: str, customer_name: str = "Customer") -> Dict:
        classification_result = self.classifier.classify(message)
        classification = classification_result["classification"]
        using_openai = classification_result["using_openai"]
        
        if classification == "positive_feedback":
            response = self.feedback_handler.handle_positive(customer_name)
            agent_used = "Feedback Handler (Positive)"
        elif classification == "negative_feedback":
            response = self.feedback_handler.handle_negative(message)
            agent_used = "Feedback Handler (Negative)"
        elif classification == "query":
            response = self.query_handler.handle_query(message)
            agent_used = "Query Handler"
        else:
            response = "I'm sorry, I couldn't understand your message. Please try again."
            agent_used = "Error Handler"
        
        log_entry = {
            "message": message,
            "classification": classification,
            "agent_used": agent_used,
            "response": response,
            "using_openai": using_openai
        }
        self.logs.append(log_entry)
        
        return log_entry
