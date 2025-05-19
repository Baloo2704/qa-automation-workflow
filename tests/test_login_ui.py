# tests/test_login_ui.py
import pytest
from pages.login_page import LoginPage
from utils.config import Config

@pytest.mark.ui
def test_login_success(driver):
    driver.get(Config.BASE_URL)
    login = LoginPage(driver)
    login.login(Config.USERNAME, Config.PASSWORD)
    assert "dashboard" in driver.current_url
