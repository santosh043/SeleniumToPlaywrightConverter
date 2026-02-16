import requests
import json
import sys

def check_ollama():
    """Checks if Ollama is running and if 'codellama' is available."""
    url = "http://localhost:11434/api/tags"
    
    print(f"Testing connection to {url}...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Ollama is reachable.")
            models = response.json().get('models', [])
            model_names = [m['name'] for m in models]
            print(f"Available models: {model_names}")
            
            if any("codellama" in name for name in model_names):
                print("✅ 'codellama' model found.")
                return True
            else:
                print("⚠️ 'codellama' NOT found via API. It might need to be pulled (ollama pull codellama).")
                # We return True anyway to proceed with the attempt, but warn user
                return True
        else:
            print(f"❌ Ollama returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama. Is it running on port 11434?")
        return False

def test_generation():
    """Sends a simple hello world prompt to codellama."""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "codellama",
        "prompt": "// Java: System.out.println(\"Hello\");\n// Convert to TypeScript:",
        "stream": False
    }
    
    print("\nSending test prompt to 'codellama'...")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json().get("response", "")
            print(f"✅ Response received:\n---\n{result}\n---")
            return True
        else:
            print(f"❌ Generation failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Initiating Handshake with Ollama...")
    if check_ollama():
        test_generation()
    else:
        sys.exit(1)
