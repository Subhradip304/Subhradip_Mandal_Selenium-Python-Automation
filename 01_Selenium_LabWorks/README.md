# 01_Selenium_LabWorks

Hands-on test automation lab implementations based on the **Python Automation CoE Curriculum**, executed on **Microsoft Edge** using **Selenium WebDriver**, **PyTest**, **Behave (BDD)**, and **Robot Framework**.

---

## 📌 Syllabus & Lab Mapping

| Module / Tier | Assignment / Topic | Script / Artifact | Description |
| :--- | :--- | :--- | :--- |
| **Tier 1: Core Fundamentals** | **Assgn 1: Multi-Locator Challenge** | `01_locators_challenge.py` | Element identification using `ID`, `NAME`, `XPATH`, `CSS`, `CLASS_NAME`, `TAG_NAME`, and Link Texts. |
| | **Assgn 2: Synchronization & Waits** | `02_explicit_waits.py` | Replacing hardcoded delays with `WebDriverWait` and `expected_conditions`. |
| | **Assgn 3: Dynamic Elements** | `03_dynamic_dropdowns.py` | Handling auto-suggest dropdowns and checkbox selection verifications. |
| **Tier 2: Advanced Interactions** | **Assgn 4: Alerts & Confirms** | `04_alerts_and_confirms.py` | Switching to JS alerts/confirms, handling popup prompts, and dismiss/accept actions. |
| | **Assgn 5: WebTable Extractor** | `05_webtable_extractor.py` | Dynamic HTML table traversal, row/column parsing, and target text search. |
| | **Assgn 6: Windows, Tabs & Iframes** | `06_windows_and_iframes.py` | Multi-window handle switching (`window_handles`) and nested iframe context switching. |
| **Frameworks: PyTest** | **PyTest Integration & Fixtures** | `test_automation_practice.py` | Test fixtures, `@pytest.mark.smoke`, `@pytest.mark.regression`, and `@pytest.mark.parametrize`. |
| **Frameworks: BDD (Behave)** | **BDD End-to-End Scenarios** | `practice.feature`, `steps.py` | Gherkin scenarios covering browser flows with step definitions in Behave. |
| **Frameworks: Robot Framework** | **Robot Automation Labs** | `ass1.robot` – `ass6.robot` | Keyword-driven testing using `SeleniumLibrary` with HTML log and report generation. |

---

## 🚀 Quick Execution Guide

* **Run all Robot Framework tests:**
  ```powershell
  python -m robot -d results ass*.robot
