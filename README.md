# Sample QA Automation Project

This project demonstrates a structured end-to-end test automation setup including:

- **UI Testing** with Selenium and Pytest
- **API Testing** using `requests`
- **Performance Testing** with Locust
- **Security Scanning** stub with OWASP ZAP
- **GitHub Actions Workflows** to automate test runs
- **Grafana Integration** to visualize test results

---

## 🧪 Test Types

| Test Type       | Tool        | Location        | Trigger             |
|-----------------|-------------|------------------|---------------------|
| Functional UI   | Selenium    | `tests/` + `pages/` | On push / PR to main |
| API             | requests    | `tests/`         | On push / PR to main |
| Performance     | Locust      | `performance/`   | Daily @ midnight     |
| Security        | OWASP ZAP   | `security/`      | Daily @ midnight     |

---

## 📁 Project Structure

```bash
sample_qa_project/
├── tests/           # Functional tests
├── pages/           # Page Object Models
├── utils/           # Shared utilities
├── performance/     # Locust performance tests
├── security/        # ZAP test stubs
├── .github/workflows/  # CI setup
├── push_metrics.py  # Placeholder to push data to Grafana
├── requirements.txt
├── pytest.ini
└── README.md
