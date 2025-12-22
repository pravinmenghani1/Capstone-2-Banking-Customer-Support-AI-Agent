#!/usr/bin/env python3
"""
Project Setup Verification Script
Run this to verify your environment is ready for the Banking Customer Support AI Agent
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is 3.8+"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.8+")
        return False

def check_git():
    """Check if Git is installed"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()} - OK")
            return True
    except FileNotFoundError:
        pass
    print("❌ Git not found - Please install Git")
    return False

def check_pip():
    """Check if pip is available"""
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()} - OK")
            return True
    except:
        pass
    print("❌ pip not found - Please install pip")
    return False

def check_venv():
    """Check if virtual environment can be created"""
    try:
        result = subprocess.run([sys.executable, '-m', 'venv', '--help'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Virtual environment support - OK")
            return True
    except:
        pass
    print("❌ Virtual environment not supported - Please install python3-venv")
    return False

def check_api_key():
    """Check if OpenAI API key is configured"""
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key.strip() and api_key != "your_openai_api_key_here":
        print("✅ OpenAI API key configured - OK")
        return True
    else:
        print("⚠️  OpenAI API key not configured - You'll need to add it later")
        return False

def main():
    print("🔍 Banking Customer Support AI Agent - Setup Verification\n")
    
    checks = [
        ("Python 3.8+", check_python_version),
        ("Git", check_git),
        ("pip", check_pip),
        ("Virtual Environment", check_venv),
        ("OpenAI API Key", check_api_key)
    ]
    
    results = []
    for name, check_func in checks:
        results.append(check_func())
    
    print(f"\n📊 Results: {sum(results)}/{len(results)} checks passed")
    
    if sum(results) >= 4:  # API key is optional for initial setup
        print("🎉 Your system is ready! You can proceed with the project setup.")
        if not results[-1]:  # API key not configured
            print("💡 Remember to configure your OpenAI API key before running the application.")
    else:
        print("⚠️  Please install missing requirements before proceeding.")
        print("📖 See PREREQUISITES.md for detailed installation instructions.")

if __name__ == "__main__":
    main()
