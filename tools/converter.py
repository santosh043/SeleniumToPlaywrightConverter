import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "codellama"

SYSTEM_PROMPT = """
You are an expert Test Automation Engineer. Convert this Java Selenium code to Playwright TypeScript.
Rules:
1. Use 'await' for all async actions.
2. Use 'page.locator()' instead of 'driver.findElement()'.
3. Convert TestNG assertions to Playwright 'expect'.
4. If input is a Class, output a Class. If Test, output 'test()'.
5. OUTPUT CODE ONLY. No comments outside code. No markdown backticks.
"""

def generate_conversion(java_code: str) -> str:
    """
    Sends the Java code to Ollama and returns the TS code.
    """
    prompt = f"{SYSTEM_PROMPT}\n\n// Java Code:\n{java_code}\n\n// TypeScript Conversion:"
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2, # Low temperature for deterministic code
            "num_predict": 2048 # Allow enough tokens for full file
        }
    }
    
    try:
        print(f"Generating conversion with model {MODEL}...")
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        
        result_json = response.json()
        raw_output = result_json.get("response", "")
        
        # Post-processing to clean up markdown if the LLM ignored the rule
        cleaned_output = _clean_output(raw_output)
        return cleaned_output
        
    except requests.exceptions.RequestException as e:
        return f"// Error communicating with Ollama: {str(e)}"
    except Exception as e:
        return f"// Unexpected error: {str(e)}"

def _clean_output(text: str) -> str:
    """Removes markdown code blocks if present."""
    # Remove ```typescript or ```javascript or just ```
    text = re.sub(r'^```[a-zA-Z]*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n```$', '', text, flags=re.MULTILINE)
    return text.strip()

if __name__ == "__main__":
    # Test case
    sample_java = """
    @Test
    public void validLogin() {
        driver.get("https://example.com");
        driver.findElement(By.id("username")).sendKeys("tomsmith");
        driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");
        driver.findElement(By.cssSelector("button.radius")).click();
        Assert.assertTrue(driver.getCurrentUrl().contains("/secure"));
    }
    """
    print(generate_conversion(sample_java))
