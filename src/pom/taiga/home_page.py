from src.pom.base_pom import PageObjectModelBase


class HomePage(PageObjectModelBase):
    @property
    def default_url(self):
        return f"{self._env.taiga_ui_url}"

    def login(self):
        self._page.get_by_role("link", name="Log in").click()
        self._page.get_by_role("link", name="Sign in with Github").click()
        self._page.get_by_label("Username or email address").click()
        self._page.get_by_label("Username or email address").fill(self._env.taiga_user)
        self._page.get_by_label("Password").click()
        self._page.get_by_label("Password").fill(self._env.taiga_password)
        self._page.get_by_role("button", name="Sign in", exact=True).click()
