# Digital Pakistan Quiz Management System

A comprehensive quiz management system built with Streamlit that allows teachers to upload quiz documents and students to take timed quizzes.

## Features

- **Teacher Panel**: Upload PDF/DOCX files with MCQs, set correct answers, enable/disable quizzes
- **Student Panel**: Take quizzes with real-time timer, auto-submission when time expires
- **Timer System**: Visual countdown timer with color changes and auto-submission
- **File Support**: Upload PDF and DOCX documents
- **MCQ Generation**: Auto-generate MCQs from descriptive text
- **Results Tracking**: Store and display student results with Excel export

## Deployment on Streamlit Cloud

1. Fork this repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your GitHub repository
4. Set the main file path to `app.py`
5. Deploy!

## Teacher Login
- Username: `admin`
- Password: `Admin123`

## Local Development
```bash
pip install -r requirements.txt
streamlit run app.py
