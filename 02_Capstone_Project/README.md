## Capstone Assignment1:  VIDEO LINK
https://drive.google.com/file/d/1TSpuPaq-OPcgSSoUPeEzL8aja_husww_/view?usp=drive_link




## Prerequisites

- Python 3.10+
- Edge (EdgeDriver is managed automatically by Selenium Manager)
- A valid TutorialsNinja demo-store account. Create one via **My Account > Register** if needed.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` with the demo account credentials. The first test run automatically creates `data/test_data.xlsx` from the JSON seed data; this keeps the binary spreadsheet out of source control while still exercising Excel input.

## Run

```powershell
pytest
```

Run without a visible browser:

```powershell
$env:HEADLESS='true'; pytest
```

Outputs:

- `reports/execution_report.html` — self-contained pytest HTML report
- `screenshots/` — timestamped screenshots for key workflow stages and failures
- `data/test_data.xlsx` — generated Excel test-data source

## Project structure

```
pages/       Page Object Model classes
tests/       Selenium end-to-end test
utils/       configuration, Excel/JSON readers, screenshots, alert helper
data/        JSON seed and generated Excel test data
```

