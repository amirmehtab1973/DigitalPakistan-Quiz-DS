import subprocess
import sys
import os

def install_requirements():
    """Install required packages and download NLTK data"""
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("Downloading NLTK data...")
    import nltk
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('maxent_ne_chunker', quiet=True)
    nltk.download('words', quiet=True)
    
    print("Setup completed successfully!")

if __name__ == "__main__":
    install_requirements()
