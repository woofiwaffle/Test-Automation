# Created by User at 26.07.2024
Feature: Employee Management in OrangeHRM

  Scenario: Add a new employee and verify in the employee list
    Given I am logged in as an admin
    When I navigate to the "Add Employee" page
    And I fill in the employee details