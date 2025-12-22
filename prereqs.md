# Prerequisites for Banking Customer Support AI Agent

**📧 Send this to learners BEFORE the session to ensure they're ready!**

## 🎯 What You Need to Prepare

### 1. Python 3.8+ Installation

**Windows:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.8+ (latest recommended)
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Test: Open Command Prompt and type `python --version`

**macOS:**
```bash
# Option 1: Download from python.org (recommended for beginners)
# Go to python.org/downloads and download the installer

# Option 2: Using Homebrew (if you have it)
brew install python
```
Test: Open Terminal and type `python3 --version`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Linux (CentOS/RHEL):**
```bash
sudo yum install python3 python3-pip
# or for newer versions: sudo dnf install python3 python3-pip
```
Test: Type `python3 --version`

### 2. Git Installation

**Windows:**
- Download from [git-scm.com](https://git-scm.com/download/win)
- Install with default settings

**macOS:**
```bash
# Option 1: Download from git-scm.com
# Option 2: Install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git
```

### 3. OpenAI API Account & Key

**CRITICAL - Do this before the session:**

1. **Create Account**: Go to [platform.openai.com](https://platform.openai.com)
2. **Sign up** or log in
3. **Add Payment Method**: Go to Billing → Add payment method
4. **Generate API Key**: 
   - Go to API Keys section
   - Click "Create new secret key"
   - **COPY AND SAVE IT SECURELY** (you won't see it again!)
   - Format looks like: `sk-proj-...` (long string)

**💰 Cost**: Minimal usage (~$0.50-2.00 for the entire project)

### 4. Code Editor (Optional but Recommended)

Choose one:
- **VS Code**: [code.visualstudio.com](https://code.visualstudio.com) (recommended)
- **PyCharm Community**: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Any text editor you prefer

## ✅ Pre-Session Checklist

**Complete these BEFORE the session:**

- [ ] Python 3.8+ installed and working (`python --version` or `python3 --version`)
- [ ] Git installed and working (`git --version`)
- [ ] OpenAI account created
- [ ] OpenAI API key generated and saved securely
- [ ] Payment method added to OpenAI account
- [ ] Code editor installed (optional)
- [ ] Stable internet connection

## 🧪 Test Your Setup

**Run these commands to verify everything works:**

```bash
# Test Python
python --version
# or on Mac/Linux:
python3 --version

# Test pip
pip --version
# or:
pip3 --version

# Test Git
git --version

# Test virtual environment creation
python -m venv test_env
# Clean up
rmdir /s test_env  # Windows
rm -rf test_env    # Mac/Linux
```

## 🚨 Common Issues & Quick Fixes

**"Python not found":**
- Windows: Reinstall Python with "Add to PATH" checked
- Mac/Linux: Use `python3` instead of `python`

**"Permission denied":**
- Windows: Run Command Prompt as Administrator
- Mac/Linux: Use `sudo` for system installations

**OpenAI API Key Issues:**
- Make sure you've added a payment method
- API key should start with `sk-proj-` or `sk-`
- Keep it secure - never share it!

## 📱 What to Bring to the Session

1. **Your OpenAI API Key** (saved securely)
2. **Laptop** with all software installed
3. **Stable internet connection**
4. **Enthusiasm to learn!** 🚀

## ❓ Need Help?

If you encounter issues during setup:
1. Try the common fixes above
2. Search for the specific error message online
3. Ask for help in our discussion forum
4. Come to the session - we'll help you get set up!

## 🎯 Session Day

On the day of the session, we'll:
1. Verify your setup quickly
2. Clone the project repository
3. Set up the virtual environment
4. Configure your API key
5. Run the Banking Customer Support AI Agent!

**You're going to build an amazing multi-agent AI system! 🤖✨**
