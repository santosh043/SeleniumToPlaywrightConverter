# 🏗️ Architecture: Frontend UI (SOP)

## 1. Overview
The User Interface is a single-page application (SPA) focused on developer productivity. It mimics a code editor environment (VS Code style).

## 2. Layout Strategy
- **Header**: Simple branding ("Selenium -> Playwright Converter") + Status Indicator (Ollama Online/Offline).
- **Main Area**: A split-pane layout (50/50).
    - **Left Pane (Source)**: `<textarea>` for pasting Java Selenium code. Placeholder includes an example snippet.
    - **Right Pane (Target)**: Read-only `<pre><code>` block for the generated TypeScript code. Syntax highlighting (via simple CSS or library if available) is desirable.
- **Action Bar**: A central "Convert" button floating or situated between panes.
- **Footer**: minimal credits.

## 3. Technology Stack
- **HTML5**: Semantic structure.
- **CSS3**: Variables for theming (Dark Mode default). Flexbox/Grid for layout.
- **JavaScript (Vanilla)**: Fetch API to communicate with `backend_sop` endpoints.

## 4. State Management
- `isConverting`: Boolean. Controls the loading state (spinner/disabled button).
- `sourceCode`: String. Bound to the input textarea.
- `targetCode`: String. Bound to the output display.

## 5. User Feedback
- **Loading**: When converting, show a "Processing..." animation. This is critical as LLMs can take 10-30 seconds.
- **Error**: If the API fails, show a toast notification or inline red error message.
- **Success**: Auto-copy to clipboard button appeared next to the output.
