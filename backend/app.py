from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine import CodeAnalyzer

app = Flask(__name__)
CORS(app)  #  frontend to talk to this backend


analyzer = CodeAnalyzer() 

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json()
    repo_url = data.get('repo_url')

    if not repo_url:
        return jsonify({"error": "No URL provided"}), 400

    print(f"🚀 Received request for: {repo_url}")
    
   
    result = analyzer.analyze_repo(repo_url)
    
    return jsonify(result)

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)