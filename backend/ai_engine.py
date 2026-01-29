import os
import google.generativeai as genai


GEMINI_API_KEY = "AIzaSyBlnrCRnLp3M_6s-mVzfcNP0C8nO5olTKE"

class CodeAnalyzer:
    def __init__(self):
        try:
            # Configure Gemini
            api_key = os.getenv("GEMINI_API_KEY") or GEMINI_API_KEY
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            print("✅ AI Engine Connected to Gemini")
        except Exception as e:
            print(f"❌ AI Engine Error: {e}")
            self.model = None

    def analyze_repo(self, repo_url):
        if not self.model:
            return {"summary": "Error: AI not connected. Check API Key.", "rating": "F", "bugs": [], "security": []}
            
        print(f"🤖 AI Engine: Analyzing {repo_url}...")
        
        # Simple prompt to test the connection
        prompt = f"""
        Analyze this GitHub Repository URL based on its name and typical structure: {repo_url}
        
        Provide a PRELIMINARY risk assessment.
        Format response strictly as JSON:
        {{
            "summary": "Brief overview of what this project likely does...",
            "rating": "Letter Grade (A-F)",
            "bugs": ["List 2 potential bugs"],
            "security": ["List 2 security checks"]
        }}
        """

        try:
            response = self.model.generate_content(prompt)
            # Return the raw text for now so we can see it working
            return {"summary": response.text, "rating": "B", "bugs": [], "security": []}
        except Exception as e:
            return {"summary": f"Gemini Error: {str(e)}", "rating": "Error", "bugs": [], "security": []}