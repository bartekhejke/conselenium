import playwright.sync_api as playwright
from src import configs

class PageObjectModelBase:
    def __init__(self, page: playwright.Page):
        self._page = page
        self._env: configs.EnvConfig = configs.EnvConfig()
        self._playwright: configs.PlaywrightConfig = configs.PlaywrightConfig

    @property
    def default_url(self):
        raise NotImplemented


    def goto(self):
        self._page.goto(self.default_url)