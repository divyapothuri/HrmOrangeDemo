from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")
        title = self.page.title()
        print(title)

    def login(self):
        heading = self.page.get_by_text("Username : Admin", exact=True).text_content()
        username = heading.split(':')[1].strip()
        heading2 = self.page.get_by_text("Password : admin123", exact=True).text_content()
        password = heading2.split(':')[1].strip()
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def assert_dashboard(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_contain_text("Dashboard", timeout=15000)

    def invalid_login(self,username,password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        expect(
            self.page.get_by_text("Invalid credentials", exact=True)
        ).to_contain_text("Invalid credentials")
