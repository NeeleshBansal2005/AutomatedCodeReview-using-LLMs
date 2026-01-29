# AI Engine - Core Logic
import os
import warnings
import google.generativeai as genai
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("CRITICAL ERROR: API Key not found. Please check your .env file.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def analyze_code_chunk(file_name, code_content):
    """
    Sends a specific file to Google Gemini for a code review.
    We instruct the AI to act as a Senior Engineer.
    """
    prompt = f"""
    You are a Senior Software Engineer and Code Reviewer.
    Review the following file from a GitHub repository: {file_name}
    
    Code Content:
    ```
    {code_content}
    ```
    
    Please provide a structured review covering:
    1. **Potential Bugs:** Logical errors or runtime crashes.
    2. **Security Risks:** Vulnerabilities (e.g., SQL injection, exposed keys).
    3. **Improvement Suggestions:** clean code practices, optimizations, or better naming conventions.
    
    Keep your response concise, professional, and formatted with bullet points.
    """
    
    try:
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing {file_name}: {str(e)}"