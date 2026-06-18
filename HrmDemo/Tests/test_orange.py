import pytest
from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage

@pytest.mark.smoke
def test_login(page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    # Navigate and login
    login_page.navigate()
    login_page.login()
    login_page.assert_dashboard()

    # Admin actions
    admin_page.open_admin()
    admin_page.add_user(emp_name="divya", username="Orangelook", password="Abcd@1234")
    admin_page.validate_success()

    # Logout
    admin_page.logout()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.invalid_login(username ="admin",password = "asdjsjjds")
