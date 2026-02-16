# 🔍 Findings & Discoveries

## Critical Constraints
- **Language Gap**: Converting Java (strongly typed, synchronous-looking but blocking) to TypeScript (async/await, Playwright patterns) is non-trivial using simple regex.
- **Dependency**: The "Converter" likely requires an Intelligent Agent (LLM) or a very robust AST parser. Given the "AITestingPractise" context, an LLM approach is assumed but needs verification.

## Research Notes
- **Playwright vs Selenium**:
    - Selenium: `driver.findElement(By.id("foo")).click()`
    - Playwright: `await page.locator('#foo').click()`
    - Assertions: TestNG `Assert.assertEquals(a, b)` -> Playwright `expect(a).toBe(b)`
- **Tech Stack Decision**:
    - Using Python for the backend allows easy integration with local LLMs (Ollama) or API calls if needed later.
