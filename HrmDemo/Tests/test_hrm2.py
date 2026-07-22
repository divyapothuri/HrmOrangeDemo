from playwright.sync_api import Page, expect


def test_orm(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")

    username_text = page.locator(".oxd-sheet .oxd-text.oxd-text--p").first.text_content()
    assert username_text is not None
    username = username_text.split(":", 1)[1].strip()

    password_text = page.locator(".oxd-sheet .oxd-text.oxd-text--p").last.text_content()
    assert password_text is not None
    password = password_text.split(":", 1)[1].strip()

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name=" Login ").click()
    expect(page.locator("h6:has-text('Dashboard')")).to_be_visible()
# dashboard
    page.locator(
        "span[class='oxd-text oxd-text--span oxd-main-menu-item--name']"
    ).filter(has_text="Admin").click()
    page.get_by_role("button", name=" Add ").click()

    page.locator(".oxd-select-text-input").first.click()
    page.get_by_role("option", name="Admin").click()
    page.locator(".oxd-select-text-input").last.click()
    page.get_by_role("option", name="Enabled").click()

    page.get_by_placeholder("Type for hints...").press_sequentially("a")
    page.wait_for_timeout(3000)
    autocomplete_option = page.locator(".oxd-autocomplete-option").first
    expect(autocomplete_option).to_be_visible()
    autocomplete_option.click()

    page.locator(".oxd-input.oxd-input--active").nth(1).fill("divya2")
    page.locator("input[type='password']").first.fill("Abcd@1234")
    page.locator("input[type='password']").last.fill("Abcd@1234")
    page.get_by_role("button", name=" Save ").click()

    success_toast = page.locator(".oxd-toast")
    expect(success_toast).to_be_visible()
    expect(success_toast).to_contain_text("Success")