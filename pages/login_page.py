from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[id='email']")
        self.password_input = page.locator("input[id='password']")
        self.login_button = page.locator("button[id='login-button']")

    def navigate(self):
        self.page.goto("https://staging.minute-master.com/login")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_url("**/bookcase*")

    def get_current_url(self):
        return self.page.url
