from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import converter

app = Flask(__name__, static_folder='../static', template_folder='../templates')
CORS(app) # Allow cross-origin requests for development

# Ensure static folder exists
if not os.path.exists('../static'):
    os.makedirs('../static')

@app.route('/')
def index():
    return send_from_directory('../static', 'index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    # Simple check to see if Ollama is reachable
    try:
        import requests
        res = requests.get("http://localhost:11434/api/tags")
        if res.status_code == 200:
            return jsonify({"status": "online", "model": "codellama"})
    except:
        pass
    return jsonify({"status": "offline", "details": "Ollama not reachable"}), 503

@app.route('/api/convert', methods=['POST'])
def convert_code():
    data = request.json
    java_code = data.get('code', '')
    
    if not java_code:
        return jsonify({"error": "No code provided"}), 400
        
    print("Received conversion request...")
    ts_code = converter.generate_conversion(java_code)
    
    return jsonify({
        "status": "success",
        "result": ts_code
    })

if __name__ == '__main__':
    print("Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)
