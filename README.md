# UI Automation Framework (Selenium + Python)

This project is a simple and scalable UI automation framework built with Python and Selenium using the Page Object Model (POM).

## Features
- Selenium WebDriver support for Chrome and Firefox
- Page Object Model for reusable UI interactions
- Pytest-based test structure
- WebDriver fixture for setup and teardown
- Cross-browser execution via command-line options

## Project Structure
```text
.
├── README.md
├── requirements.txt
├── pages/
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   └── test_login.py
└── utils/
    └── browser_factory.py
```

## Setup
1. Create and activate a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure ChromeDriver and GeckoDriver are available in your PATH.

## Running Tests
Run tests in Chrome:
```bash
pytest -q --browser=chrome
```

Run tests in Firefox:
```bash
pytest -q --browser=firefox
```

Run in headless mode:
```bash
pytest -q --browser=chrome --headless
```

## Example Usage
The sample login test uses a Page Object class to encapsulate page interactions and keep the test readable.
