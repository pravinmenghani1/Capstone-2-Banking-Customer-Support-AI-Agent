# Banking Customer Support AI Agent

A multi-agent GenAI system for banking customer support that classifies customer messages and provides intelligent responses using OpenAI GPT-3.5.

## 🎯 Project Overview

This system handles:
- **Classification** of customer messages (positive feedback, negative feedback, queries)
- **Automated responses** based on sentiment analysis
- **Ticket management** for complaints and issues
- **Real-time processing** through an interactive web interface

## 🏗️ Architecture

### Multi-Agent System:
- **ClassifierAgent**: Uses OpenAI GPT-3.5 to categorize customer messages
- **FeedbackHandlerAgent**: Processes positive/negative feedback and creates support tickets
- **QueryHandlerAgent**: Handles ticket status inquiries and information requests

### Technology Stack:
- **Backend**: Python with OpenAI API integration
- **Database**: SQLite for ticket management
- **Frontend**: Streamlit web interface
- **AI Model**: OpenAI GPT-3.5-turbo for sentiment classification

## 📋 Prerequisites

**Before starting, please review [PREREQUISITES.md](PREREQUISITES.md) for detailed system requirements.**

Quick checklist:
- Python 3.8+ installed
- Git installed
- OpenAI API account and API key
- Internet connection

## 🚀 Setup Instructions

### 0. Verify Prerequisites (Recommended)
```bash
python verify_setup.py
```
This will check if your system has all required components.

### 2. Clone the Repository
```bash
git clone https://github.com/pravinmenghani1/Capstone-2-Banking-Customer-Support-AI-Agent.git
cd Capstone-2-Banking-Customer-Support-AI-Agent
```

### 3. Create Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure OpenAI API Key

**Option A: Environment Variable (Recommended)**
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=your_actual_openai_api_key

# Windows (PowerShell)
$env:OPENAI_API_KEY="your_actual_openai_api_key"

# macOS/Linux
export OPENAI_API_KEY=your_actual_openai_api_key
```

**Option B: .env File**
```bash
# Edit the .env file and add your key
OPENAI_API_KEY=your_actual_openai_api_key
```

**Option C: Streamlit Interface**
- Leave .env empty and enter your API key in the Streamlit sidebar when running the app

### 6. Run the Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🧪 Testing

### Run Automated Tests
```bash
python test_agents.py
```

### Manual Testing via Web Interface
1. Open the Streamlit app
2. Enter your OpenAI API key in the sidebar
3. Test these sample messages:
   - **Positive**: "Thanks for resolving my credit card issue!"
   - **Negative**: "My debit card replacement hasn't arrived yet"
   - **Query**: "What's the status of ticket 123456?"

## 📊 Features

### Customer Message Classification
- **Positive Feedback**: Generates personalized thank-you responses
- **Negative Feedback**: Creates support tickets with unique 6-digit IDs
- **Queries**: Retrieves and displays ticket status information

### Interactive Dashboard
- Real-time message processing
- Classification confidence display
- Processing logs and analytics
- Support ticket database viewer
- Quick test case buttons

### Database Management
- Automatic SQLite database creation
- Ticket storage with timestamps
- Status tracking (Unresolved/Resolved)
- Query interface for ticket lookup

## 🔧 Troubleshooting

### Common Issues

**"OpenAI API Key required" Error:**
- Ensure your API key is correctly set in environment variable or .env file
- Verify the API key is valid at [platform.openai.com](https://platform.openai.com)

**"Module not found" Errors:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**"Permission denied" Errors:**
- **Windows**: Run Command Prompt as Administrator
- **macOS/Linux**: Check file permissions or use `sudo` if needed

**Streamlit won't start:**
- Check if port 8501 is available
- Try: `streamlit run app.py --server.port 8502`

### Platform-Specific Notes

**Windows:**
- Use `python` instead of `python3`
- Use backslashes `\` in file paths
- Activate venv with `venv\Scripts\activate`

**macOS:**
- May need to use `python3` and `pip3`
- Activate venv with `source venv/bin/activate`

**Linux:**
- Usually requires `python3` and `pip3`
- May need to install `python3-venv` package first

## 📁 Project Structure

```
├── app.py                 # Streamlit web interface
├── agents.py              # Multi-agent system implementation
├── test_agents.py         # Automated test suite
├── verify_setup.py        # System verification script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (add your API key)
├── .gitignore            # Git ignore file
├── README.md             # This file
├── PREREQUISITES.md      # Detailed system requirements
└── support.db            # SQLite database (created automatically)
```

## 🔒 Security Notes

- **Never commit your OpenAI API key** to version control
- Keep your `.env` file in `.gitignore`
- Use environment variables in production
- Monitor your OpenAI API usage and costs

## 🎓 Learning Objectives

This project demonstrates:
- Multi-agent AI system architecture
- OpenAI API integration and prompt engineering
- Real-time sentiment analysis and classification
- Database integration with SQLite
- Web application development with Streamlit
- Error handling and fallback mechanisms
- Cross-platform Python development

## 📝 Example Workflows

### Workflow 1: Positive Feedback
```
Input: "Thanks for resolving my credit card issue!"
→ ClassifierAgent → Positive Feedback
→ FeedbackHandlerAgent → Thank you response
Output: "Thank you for your kind words! We're delighted to assist you."
```

### Workflow 2: Complaint Handling
```
Input: "My debit card replacement hasn't arrived"
→ ClassifierAgent → Negative Feedback  
→ FeedbackHandlerAgent → Create ticket #123456
Output: "We apologize for the inconvenience. Ticket #123456 has been created."
```

### Workflow 3: Status Inquiry
```
Input: "What's the status of ticket 123456?"
→ ClassifierAgent → Query
→ QueryHandlerAgent → Database lookup
Output: "Your ticket #123456 is currently marked as: Unresolved"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes as part of the Applied Generative AI Specialization Capstone.

## 🆘 Support

If you encounter issues:
1. Check [PREREQUISITES.md](PREREQUISITES.md) for system requirements
2. Review the troubleshooting section above
3. Ensure all dependencies are correctly installed
4. Verify your OpenAI API key is valid and properly configured
