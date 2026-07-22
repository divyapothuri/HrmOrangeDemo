from playwright.sync_api import Page, expect


class HrmPage:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page: Page) -> None:
        self.page = page

    def login(self) -> None:
        self.page.goto(self.url)
        expect(self.page).to_have_title("OrangeHRM")

        username_text = self.page.locator(
            ".oxd-sheet .oxd-text.oxd-text--p"
        ).first.text_content()
        password_text = self.page.locator(
            ".oxd-sheet .oxd-text.oxd-text--p"
        ).last.text_content()
        assert username_text is not None
        assert password_text is not None

        username = username_text.split(":", 1)[1].strip()
        password = password_text.split(":", 1)[1].strip()
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name=" Login ").click()
        expect(self.page.locator("h6:has-text('Dashboard')")).to_be_visible()

    def add_admin_user(self, employee_name: str, username: str, password: str) -> None:
        self.page.get_by_text("Admin", exact=True).first.click()
        self.page.get_by_role("button", name=" Add ").click()

        self.page.locator(".oxd-select-text-input").first.click()
        self.page.get_by_role("option", name="Admin").click()
        self.page.locator(".oxd-select-text-input").last.click()
        self.page.get_by_role("option", name="Enabled").click()

        self.page.get_by_placeholder("Type for hints...").press_sequentially(employee_name)
        self.page.wait_for_timeout(3000)
        employee_option = self.page.locator(".oxd-autocomplete-option").first
        expect(employee_option).to_be_visible()
        employee_option.click()

        self.page.locator(".oxd-input.oxd-input--active").nth(1).fill(username)
        self.page.locator("input[type='password']").first.fill(password)
        self.page.locator("input[type='password']").last.fill(password)
        self.page.get_by_role("button", name=" Save ").click()

        success_toast = self.page.locator(".oxd-toast")
        expect(success_toast).to_be_visible()
        expect(success_toast).to_contain_text("Success")

    def logout(self) -> None:
        self.page.locator("i.oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon").click()
        self.page.get_by_role("menuitem", name="Logout").click()
