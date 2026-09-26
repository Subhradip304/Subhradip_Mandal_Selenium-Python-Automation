Feature: Selenium Automation Practice

  Scenario: Verify page title
    Given the Edge browser is opened
    When the user navigates to the Automation Practice page
    Then the page title should be displayed

  Scenario: Enter name
    Given the Edge browser is opened
    When the user navigates to the Automation Practice page
    And the user enters name "Subhradip"
    Then the name should be entered successfully

  Scenario: Select radio button
    Given the Edge browser is opened
    When the user navigates to the Automation Practice page
    And the user selects Radio2
    Then Radio2 should be selected

  Scenario: Handle alert
    Given the Edge browser is opened
    When the user navigates to the Automation Practice page
    And the user enters name "Subhradip"
    And the user clicks the Alert button
    Then the alert should be displayed with text containing "Subhradip"
