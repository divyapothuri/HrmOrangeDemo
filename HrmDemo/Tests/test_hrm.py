import pytest

from Pages.hrm_page import HrmPage


@pytest.mark.smoke
def test_admin_user_workflow(page) -> None:
    hrm_page = HrmPage(page)

    hrm_page.login()
    hrm_page.add_admin_user(
        employee_name="a",
        username="Orangelook",
        password="Abcd@1234",
    )
    hrm_page.logout()
