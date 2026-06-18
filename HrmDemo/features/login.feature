Feature: OrangeHRM Login and Admin User Management

  @smoke
  Scenario: Login and add a new Admin user
    Given I navigate to the OrangeHRM login page
    When I login with username "Admin" and password "admin123"
    Then I should see the Dashboard
    When I go to the Admin page
    And I add a new user with employee name "Orange Test", username "Orangesform", and password "Abcd@1234"
    Then I should be able to logout successfully



  @negative
  Scenario Outline: Invalid login attempts
    Given I navigate to the OrangeHRM login page
    When I try to login with username "<username>" and password "<password>"
    Then I should see an error message "Invalid credentials"

    Examples:
      | username | password   |
      | Admin    | wrongpass  |
      | Wrong    | admin123   |
      | test     | test123    |