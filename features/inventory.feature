#language : en

Feature: Add a product to the inventory

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"

  Scenario: List all products in the inventory
    Given the inventory contains a product "Coffee"
    And the inventory contains a product "Tea"
    When the user lists all products
    Then the inventory should show "Coffee" and "Tea"