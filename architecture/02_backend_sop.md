# 🏗️ Architecture: Backend API (Flask)

## 1. Overview
A lightweight Flask server acts as the bridge between the UI (Frontend) and the Ollama LLM (Engine).

## 2. Endpoints

### `POST /api/convert`
- **Purpose:** Initiates a conversion job.
- **Input (JSON):**
  ```json
  {
    "code": "public class LoginTest { ... }",
    "filename": "LoginTest.java" (optional)
  }
  ```
- **Process:**
  1. Receives Java code.
  2. Calls `tools.converter.convert_code(code)`.
  3. Returns the converted TypeScript code.
- **Output (JSON):**
  ```json
  {
    "status": "success",
    "converted_code": "import { test } ...",
    "logs": ["Parsed Java class...", "Converted assertions..."]
  }
  ```

### `GET /api/health`
- **Purpose:** Checks if Ollama is running.
- **Output:** `{"status": "ok", "model": "codellama"}`

## 3. Directory Structure
- `tools/server.py`: The Flask app entry point.
- `tools/converter.py`: The logic module (LLM wrapper).
- `static/`: HTML/CSS/JS files for the frontend. (Served relative to root or via Flask static).

## 4. Error Handling
- If Ollama is offline: Return 503 Service Unavailable.
- If conversion fails: Return 500 with error log.
