from playwright.sync_api import sync_playwright

class setupPlaywright:
    """
    To setup playwright
    """
    def __init__(self) -> None:
        playwright = sync_playwright().start()
        self.firefox = playwright.firefox
        self.browser = self.firefox.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
    def _page_(self):
        return self.page
