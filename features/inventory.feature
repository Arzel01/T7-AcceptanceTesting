#language : en

Feature: Inventory Management

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"

  Scenario: List all products in the inventory
    Given the inventory contains a product "Coffee"
    And the inventory contains a product "Tea"
    When the user lists all products
    Then the inventory should show "Coffee" and "Tea"

  Scenario: Update the quantity of a product
    Given the inventory contains products:
    | Product | Quantity | Id | Price |
    | Coffee | 10 | PROD-67 | 2.5 |
    When the user updates product “Coffee” to quantity “25”
    Then the inventory should show product “Coffee” with quantity “25”