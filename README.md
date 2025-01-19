QA Automation Project
Overview
This project is a QA automation solution designed to automate the testing process for https://www.saucedemo.com website.
The goal is to improve the efficiency and reliability of the testing process by using automation frameworks and tools.

Features
Automated Test Scripts: Includes tests for functional, regression, and smoke testing.
Cross-browser Testing: Supports multiple browsers including Chrome, Firefox, and Edge.
Parallel Test Execution: Tests can be executed in parallel to reduce test time.
Reports: Generates detailed test reports with results.
Integration with CI/CD: Easily integrates with CI/CD pipelines (e.g., Jenkins, GitLab CI).
Technologies Used
Programming Language: Python
Automation Framework: Selenium WebDriver
Test Runner: PyTest
Reporting Tool: Allure
CI/CD Integration: GitHub Actions
Setup Instructions
Prerequisites
Before running the project, make sure you have the following installed on your machine:

Python 3.12 version
Automation Framework: Selenium WebDriver
Test Runner: PyTest
Clone the repository:

Installing Dependencies:
1. Clone the repository:
git clone https://github.com/AlexanderY88/AutomationProject_python.git
cd AutomationProject_python

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
pip install -r requirements.txt


Running Tests
1. To run the tests:
pytest --maxfail=5 --disable-warnings --capture=no

2. To generate Allure test reports after running the tests:
allure serve allure-results

Running Tests in Parallel
If you want to run tests in parallel to speed up execution:
pytest -n 4  # Run tests in 4 parallel processes


Configuration
The configuration for browser options (like headless mode, screen resolution) is located in the config directory.
You can modify it based on your needs.

Directory Structure

├── requirements.txt        # Python dependencies

├── tests/confitest.py      # Configuration file (browser settings, URLs)

├── tests/                  # Directory containing all test cases

├── pages/                  # Page Object Model (POM) classes

├── pages/base_page.py      # Base functions (like get_url, copy_text...)

├── allure-results/         # Folder for Allure reports

└── README.md               # This file

Acknowledgements
Selenium WebDriver: For browser automation.
Allure Report: For generating rich HTML reports.
PyTest: For running the tests and managing test cases.



