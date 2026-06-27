# 🤖 AI Resume Analyzer

An AI-powered resume analysis tool built with Flask, Python, and Google Gemini AI.

## 🚀 Features

- 🔐 **User Authentication**: Login/Register with Google OAuth
- 📄 **Resume Parsing**: Extract text from PDF/DOCX
- 🎯 **Job Matching**: Match resume with 16+ job roles
- 💻 **Technical Skills**: Detect 100+ technical skills
- 🎤 **Interview Questions**: Generate role-specific questions
- 💰 **Salary Analysis**: Compare with market rates
- 🤖 **AI Chatbot**: Gemini-powered career assistant
- 🏢 **Tamil Nadu Jobs**: 8 companies per category with apply links
- 📊 **Dashboard**: Track analysis history and progress

## 📋 Prerequisites

- Python 3.11+
- Google Gemini API Key
- Google OAuth Credentials

## 🔧 Installation

```bash
# Clone repository
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your credentials

# Run the app
python app.py 
