import re
from playwright.sync_api import expect, Page
from src.configs import EnvConfig
from src.pom.taiga_pom import Taiga
from src.pom.taiga.home_page import HomePage

def test_login(taiga: Taiga) -> None:

    taiga.home_page.goto()
    taiga.home_page.login()
    assert taiga.dashboard_page.is_opened

