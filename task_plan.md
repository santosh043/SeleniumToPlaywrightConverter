# 🚀 Project Plan (Based on B.L.A.S.T.)

## ✅ Phase 0: Initialization
- [x] Create project files
- [x] Answer **Discovery Questions**
- [x] Define **Data Schema** in `gemini.md`
- [x] Approve **Blueprint** in `task_plan.md`

## 🏗️ Phase 1: B - Blueprint (Vision & Logic)
- [x] **Discovery:**
    - **North Star:** UI-based Selenium Java -> Playwright TS Converter.
    - **Integrations:** Conversion Engine (TBD: LLM or AST?), File System.
    - **Source of Truth:** User Input (UI).
    - **Delivery Payload:** UI Display + File Save.
- [x] **Data-First Rule:** Defined `ConversionJob` schema in `gemini.md`.
- [ ] **Research:** Determine the best "Conversion Engine" strategy (Local LLM vs API vs Regex).

## ⚡ Phase 2: L - Link (Connectivity)
- [ ] **Verification:** Verify Python environment and dependencies.
- [ ] **Handshake:** Create a "Hello World" conversion script to test the pipeline.

## ⚙️ Phase 3: A - Architect (The 3-Layer Build)
- [ ] **Layer 1 (SOPs):** Define `architecture/conversion_flow.md` and `architecture/frontend_sop.md`.
- [ ] **Layer 2 (Navigation):** Build the Flask/FastAPI app to route requests.
- [ ] **Layer 3 (Tools):** Implement the `converter.py` logic.

## ✨ Phase 4: S - Stylize (Refinement & UI)
- [ ] **Payload Refinement:** Ensure converted code is formatted (Prettier/Black).
- [ ] **UI/UX:** Build a clean, 2-pane UI (Source (Java) | Target (TS)).

## 🛰️ Phase 5: T - Trigger (Deployment)
- [ ] **Manual Test:** Convert a real file.
- [ ] **Documentation:** Update README and usage guide.
