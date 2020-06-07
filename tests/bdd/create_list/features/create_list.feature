Feature: Creating new list

  Scenario: New lists are empty
    When a new list is created
    Then the list should be empty.

  Scenario: New lists with one element in them are not empty.
    When a new list is created passing an element
    Then the list should not be empty.