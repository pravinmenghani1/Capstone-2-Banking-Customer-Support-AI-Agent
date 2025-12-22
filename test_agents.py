from agents import MultiAgentSystem
import os

def test_agent_system():
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "":
        print("❌ OpenAI API key is required!")
        print("Please set OPENAI_API_KEY environment variable or add it to .env file")
        print("Example: export OPENAI_API_KEY=your_actual_api_key")
        return
    
    system = MultiAgentSystem()
    
    # Test cases
    test_cases = [
        ("Thanks for resolving my credit card issue.", "positive_feedback"),
        ("My debit card replacement still hasn't arrived.", "negative_feedback"),
        ("Could you check the status of ticket 650932?", "query")
    ]
    
    print("🧪 Testing Multi-Agent System (OpenAI Required)\n")
    
    for message, expected_classification in test_cases:
        print(f"Input: {message}")
        try:
            result = system.process_message(message, "Test Customer")
            print(f"Classification: {result['classification']}")
            print(f"Agent: {result['agent_used']}")
            print(f"Response: {result['response']}")
            print(f"Expected: {expected_classification}")
            print(f"✅ Match: {result['classification'] == expected_classification}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    test_agent_system()
