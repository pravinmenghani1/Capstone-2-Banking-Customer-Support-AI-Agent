import streamlit as st
import pandas as pd
import os
from agents import MultiAgentSystem

st.title("🏦 Banking Customer Support AI Agent")
st.markdown("Multi-Agent Architecture for Customer Service")

# API Key Configuration
st.sidebar.header("🔑 Configuration")
api_key = st.sidebar.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key (required)")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    st.sidebar.success("✅ API Key configured")
else:
    st.sidebar.error("❌ OpenAI API Key required")
    st.error("⚠️ Please enter your OpenAI API key in the sidebar to use the application.")
    st.stop()

# Initialize session state
if 'agent_system' not in st.session_state:
    st.session_state.agent_system = MultiAgentSystem()

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Customer Message Input")
    customer_name = st.text_input("Customer Name", value="Customer")
    message = st.text_area("Enter your message:", height=100)
    
    if st.button("Process Message", type="primary"):
        if message:
            try:
                result = st.session_state.agent_system.process_message(message, customer_name)
                
                st.success("✅ Message Processed (OpenAI Classification)")
                
                # Color-code classification
                classification_display = result['classification'].replace('_', ' ').title()
                if result['classification'] == 'positive_feedback':
                    st.success(f"**Classification:** 😊 {classification_display}")
                elif result['classification'] == 'negative_feedback':
                    st.error(f"**Classification:** 😞 {classification_display}")
                else:
                    st.info(f"**Classification:** ❓ {classification_display}")
                    
                st.write(f"**Agent Used:** {result['agent_used']}")
                st.write(f"**Response:** {result['response']}")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("Please check your OpenAI API key and try again.")

with col2:
    st.subheader("Quick Test Cases")
    
    test_cases = [
        ("Thanks for resolving my credit card issue.", "Positive Feedback"),
        ("My debit card replacement still hasn't arrived.", "Negative Feedback"),
        ("Could you check the status of ticket 650932?", "Query")
    ]
    
    for test_msg, expected in test_cases:
        if st.button(f"Test: {expected}", key=test_msg):
            result = st.session_state.agent_system.process_message(test_msg, "Test Customer")
            st.write(f"**Response:** {result['response']}")

# Logs and History
st.subheader("📊 Processing Logs")

if st.session_state.agent_system.logs:
    df = pd.DataFrame(st.session_state.agent_system.logs)
    st.dataframe(df, use_container_width=True)
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Messages", len(df))
    with col2:
        st.metric("Positive Feedback", len(df[df['classification'] == 'positive_feedback']))
    with col3:
        st.metric("Tickets Created", len(df[df['classification'] == 'negative_feedback']))

# Database View
st.subheader("🎫 Support Tickets Database")
if st.button("Refresh Tickets"):
    import sqlite3
    conn = sqlite3.connect("support.db")
    tickets_df = pd.read_sql_query("SELECT * FROM support_tickets ORDER BY created_at DESC", conn)
    conn.close()
    
    if not tickets_df.empty:
        st.dataframe(tickets_df, use_container_width=True)
    else:
        st.info("No tickets in database yet.")

# Clear logs
if st.button("Clear Logs"):
    st.session_state.agent_system.logs = []
    st.rerun()
