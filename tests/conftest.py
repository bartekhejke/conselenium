import pytest
from src.configs import PlaywrightConfig, EnvConfig
from src.pom.taiga_pom import Taiga
import playwright.async_api as playwright

@pytest.fixture
def playwright_config():
    """Playwright config fixture"""
    return PlaywrightConfig()

@pytest.fixture
def taiga_url_config():
    """Env config fixture"""
    return EnvConfig()

@pytest.fixture
def taiga(page: playwright.Page) -> Taiga:
    return Taiga(page=page)