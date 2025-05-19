import pytest
import requests
from utils.config import Config

@pytest.mark.api
def test_get_users():
    res = requests.get(f"{Config.BASE_URL}/api/users")
    assert res.status_code == 200
    assert isinstance(res.json(), list)