import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    USERNAME = os.getenv("USERNAME", "admin")
    PASSWORD = os.getenv("PASSWORD", "password")