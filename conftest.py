import pytest
import requests
import yaml
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.api import get_auth_token

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def auth_token(config):
    return get_auth_token(config['username'], config['password'], config['login_url'])

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Настройка логирование может выглядеть так:

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
