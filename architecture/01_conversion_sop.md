# 🏗️ Architecture: Java Selenium to Playwright TS Conversion Logic

## 1. The Challenge
Converting Java Selenium code to Playwright TypeScript involves three major shifts:
1.  **Language**: Java (Class-based, Verbose) -> TypeScript (Functional/Class-hybrid, Async).
2.  **Library**: Selenium `WebDriver` (Synchronous-looking) -> Playwright `Page` (Async/Await).
3.  **Assertions**: TestNG `Assert` -> Jest/Playwright `expect`.

## 2. The Prompt Strategy (System Prompt)
The LLM (codellama) will receive the following context for every conversion:

> **System Identity:** You are an expert Test Automation Engineer specializing in migrating legacy Java Selenium suites to modern Playwright TypeScript.
>
> **Task:** Convert the provided Java Selenium code into idiomatic Playwright TypeScript.
>
> **Rules:**
> 1. **Async/Await:** All Playwright interactions must use `await`.
> 2. **Locators:** Use `page.locator()` with robust selectors (text, role, test-id) where possible, replacing brittle XPath/CSS if obvious.
> 3. **Assertions:** Translates `Assert.assertEquals` to `await expect(locator).toHaveText()` or `expect(value).toBe(expected)`.
> 4. **Structure:**
>    - If the input is a Page Object, output a Class.
>    - If the input is a Test Class, output a `test()` block (from `@playwright/test`).
> 5. **Output Format:** PROVIDE ONLY THE CODE. No markdown backticks, no conversational filler.

## 3. The Code Processing Pipeline
1.  **Input:** Raw Java String.
2.  **Pre-processing:**
    - Detect if it's a full class or snippet.
    - Identify imports (to determine if it uses TestNG or JUnit).
3.  **LLM Call:**
    - Model: `codellama`
    - Temperature: `0.2` (Low creativity, high precision).
4.  **Post-processing:**
    - Strip any remaining markdown (` ```typescript ... ``` `).
    - Add standard imports if missing (`import { test, expect } from '@playwright/test';`).

## 4. Edge Cases Strategy
- **`Thread.sleep(5000)`** -> `await page.waitForTimeout(5000)` (add comment: "Prefer built-in auto-waiting").
- **`WebDriverWait`** -> Remove. Playwright auto-waits.
- **`@FindBy`** -> Convert to getter methods: `get myElement() { return this.page.locator(...) }`.
