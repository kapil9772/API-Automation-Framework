# API Automation Framework

![Tests](https://github.com/kapil9772/API-Automation-Framework/actions/workflows/tests.yml/badge.svg)

A Python-based API testing framework built with **Requests** and **Pytest** to validate REST API endpoints — covering status codes, response data, and error handling.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Requests | HTTP client for API calls |
| Pytest | Test framework & assertions |
| pytest-html | HTML test report generation |
| GitHub Actions | CI - runs tests automatically on every push |

## 📌 What This Framework Tests

Tested against the public [reqres.in](https://reqres.in) API:

- **User management:** GET single user, GET user list, POST create user, PUT update user, DELETE user
- **Authentication:** Login with valid credentials, missing password, invalid user

**11 test cases total** — mix of positive (valid input, expected success) and negative (invalid input, expected errors) scenarios.

## 📂 Project Structure

```
API-Automation-Framework/
├── tests/
│   ├── test_users.py     # User CRUD endpoint tests
│   └── test_auth.py      # Login/auth tests
├── utils/
│   └── api_client.py     # Reusable API request wrapper
├── requirements.txt
├── pytest.ini
└── .github/workflows/tests.yml   # CI pipeline
```

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/kapil9772/API-Automation-Framework.git
cd API-Automation-Framework

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all tests
pytest
```

After running, an HTML report is generated at `report.html` — open it in a browser to view detailed pass/fail results.

## ✅ Example Test Cases

| Test | Type | Expected Result |
|------|------|------------------|
| Get existing user | Positive | 200 OK, correct user data |
| Get non-existent user | Negative | 404 Not Found |
| Create user with valid data | Positive | 201 Created |
| Login with valid credentials | Positive | 200 OK, token returned |
| Login with missing password | Negative | 400 Bad Request |

## 🚀 Future Improvements

- Add schema validation using `jsonschema`
- Add data-driven tests using `pytest.mark.parametrize`
- Integrate Allure reporting

---
**Author:** [Kapil Kumar Bhardwaj](https://github.com/kapil9772)
