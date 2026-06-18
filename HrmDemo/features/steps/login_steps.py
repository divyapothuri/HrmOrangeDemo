from behave import given, when, then
from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage
from playwright.sync_api import expect


@given("I navigate to the OrangeHRM login page")
def step_navigate(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login()

@then("I should see the Dashboard")
def step_dashboard(context):
    context.login_page.assert_dashboard()

@when("I go to the Admin page")
def step_admin(context):
    context.admin_page = AdminPage(context.page)
    context.admin_page.open_admin()

@when('I add a new user with employee name "{emp_name}", username "{username}", and password "{password}"')
def step_add_user(context, emp_name, username, password):
    context.admin_page.add_user(emp_name, username, password)
    context.admin_page.validate_success()

@then("I should be able to logout successfully")
def step_logout(context):
    context.admin_page.logout()


@when('I try to login with username "{username}" and password "{password}"')
def step_invalid_login(context, username, password):
    context.login_page.invalid_login(username, password)

@then('I should see an error message "{message}"')
def step_error_message(context, message):
    # The invalid_login method already asserts "Invalid credentials"
    # but you can add a check here if you want flexibility
    expect(context.page.get_by_text(message, exact=True)).to_contain_text(message)
