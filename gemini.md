# ♊ PROJECT CONSTITUTION (gemini.md)

> This file is the single source of truth for Data Schemas, Rules, and Invariants.
> **Coding only begins once the Data Schema is defined here.**

## 1. Data Schemas (The "Payload")

### Core Entity: `ConversionJob`
The atomic unit of work in this system.

```json
{
  "id": "uuid-string",
  "timestamp": "ISO-8601",
  "source": {
    "language": "java",
    "framework": "selenium-testng",
    "content": "raw java code string"
  },
  "target": {
    "language": "typescript", // or 'javascript'
    "framework": "playwright",
    "content": "converted code string (null if pending)",
    "output_path": "path/to/save/file.ts"
  },
  "settings": {
      "model": "codellama",
      "prioritize_readability": true,
      "include_comments": true
  },
  "status": "pending" | "processing" | "completed" | "failed",
  "logs": [
    "step 1: receiving request...",
    "step 2: sending to Ollama...",
    "step 3: writing file..."
  ]
}
```

## 2. Behavioral Rules
1. **Readability First**: The output code should be idiomatic Playwright (e.g., use `await page.locator` instead of `driver.findElement`).
2. **Complete Conversion**: Attempt to convert all logic, including assertions.
3. **UI Feedback**: The user must see the result in the UI immediately.
4. **Persistence**: Save the result to a physical file in the specified directory.
5. **Model Constraint**: MUST use Local LLM (`Ollama`) with model `codellama`.

## 3. Architectural Invariants
1. **Separation of Concerns**: The *Converter Engine* must be decoupled from the *UI*.
2. **Stateless**: Each conversion is independent.
3. **Tech Stack**:
    - **Backend**: Python (Flask)
    - **Frontend**: HTML/CSS/JS (Vanilla)
    - **Engine**: Ollama API (Model: `codellama`) -> `http://localhost:11434/api/generate`
