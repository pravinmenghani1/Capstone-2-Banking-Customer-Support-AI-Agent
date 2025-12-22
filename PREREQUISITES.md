# Prerequisites for Banking Customer Support AI Agent

## System Requirements

### Operating System Support
- **Windows**: Windows 10/11 (64-bit)
- **macOS**: macOS 10.14 or later
- **Linux**: Ubuntu 18.04+ / CentOS 7+ / Debian 9+

### Required Software

#### 1. Python 3.8+
**Installation:**

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Verify: `python --version` in Command Prompt

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
# Verify installation
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

**Linux (CentOS/RHEL):**
```bash
sudo yum install python3 python3-pip
# Or for newer versions:
sudo dnf install python3 python3-pip
python3 --version
```

#### 2. Git
**Windows:**
- Download from [git-scm.com](https://git-scm.com/download/win)
- Use Git Bash or Command Prompt

**macOS:**
```bash
# Using Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git
# or: sudo dnf install git
```

#### 3. OpenAI API Account
- Create account at [platform.openai.com](https://platform.openai.com)
- Generate API key from API Keys section
- **Important**: Keep your API key secure and never commit it to version control

### Optional but Recommended

#### 4. Code Editor/IDE
Choose one:
- **VS Code** (recommended): [code.visualstudio.com](https://code.visualstudio.com)
- **PyCharm Community**: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- **Sublime Text**: [sublimetext.com](https://www.sublimetext.com)

#### 5. Terminal/Command Line
**Windows:**
- Command Prompt (built-in)
- PowerShell (built-in)
- Git Bash (comes with Git)
- Windows Terminal (recommended, from Microsoft Store)

**macOS:**
- Terminal (built-in)
- iTerm2 (optional, more features)

**Linux:**
- Terminal (built-in)

## Pre-Installation Checklist

Before starting the project, ensure you have:

- [ ] Python 3.8+ installed and accessible via command line
- [ ] Git installed and configured
- [ ] OpenAI API account created
- [ ] OpenAI API key generated (keep it secure)
- [ ] Code editor installed (optional)
- [ ] Terminal/command line access
- [ ] Internet connection for package downloads

## Verification Commands

Run these commands to verify your setup:

```bash
# Check Python version (should be 3.8+)
python --version
# or on some systems:
python3 --version

# Check pip (Python package manager)
pip --version
# or:
pip3 --version

# Check Git
git --version

# Check if virtual environment creation works
python -m venv test_env
# Clean up test
rm -rf test_env  # Linux/macOS
rmdir /s test_env  # Windows
```

## Common Issues & Solutions

### Python Not Found
- **Windows**: Reinstall Python with "Add to PATH" checked
- **macOS/Linux**: Use `python3` instead of `python`

### Permission Errors
- **Windows**: Run Command Prompt as Administrator
- **macOS/Linux**: Use `sudo` for system-wide installations

### Virtual Environment Issues
- Ensure you're using the correct Python version
- Try `python3 -m venv` instead of `python -m venv`

### Package Installation Failures
- Update pip: `pip install --upgrade pip`
- Use `pip3` instead of `pip` on some systems
- Check internet connection and firewall settings

## Next Steps

Once you have all prerequisites installed:
1. Clone the project repository
2. Follow the setup instructions in README.md
3. Create and activate virtual environment
4. Install project dependencies
5. Configure your OpenAI API key
6. Run the application

## Support

If you encounter issues during setup:
1. Check the error message carefully
2. Verify all prerequisites are correctly installed
3. Try the common solutions above
4. Search for the specific error online
5. Ask for help with the specific error message and your operating system details
