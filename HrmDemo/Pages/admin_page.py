from playwright.sync_api import expect


class AdminPage:
    def __init__(self, page):
        self.page = page

    def open_admin(self):
        self.page.get_by_role("link", name="Admin").click()

    def add_user(self, emp_name, username, password):
        self.page.get_by_role("button", name="Add").click()
        self.page.locator("div.oxd-select-text").nth(0).click()
        self.page.locator("span").filter(has_text="Admin").last.click()
        self.page.get_by_role("textbox", name="Type for hints...").fill(emp_name)
        self.page.locator(f"span:has-text('{emp_name}')").click()
        self.page.locator("div").filter(has_text="-- Select --").last.click()
        self.page.get_by_text("Enabled", exact=True).click()
        self.page.locator("input.oxd-input.oxd-input--active").nth(1).fill(username)
        self.page.locator("input[type='password']").nth(0).fill(password)
        self.page.locator("input[type='password']").nth(1).fill(password)
        self.page.get_by_role("button", name="Save").click()
    def validate_success(self):
        toast_message = self.page.locator("#oxd-toaster_1")

        expect(toast_message).to_be_visible(timeout=30000)

        msg = toast_message.text_content()
        print("Toast Message:", msg)

        assert "Successfully Saved" in msg

    def logout(self):
        self.page.locator("i.oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon").click()
        self.page.get_by_role("menuitem", name="Logout").click()
