from behave import given, when, then
from inventory import InventoryManager

# Step 1: Given the inventory is empty
@given('the inventory is empty')
def step_impl(context):
    context.inventory = InventoryManager()
    
# Step 2: When the user adds a product "Coffee"
@when('the user adds a product "{product_name}"')
def step_impl(context, product_name):
    product_id = "PROD-001"
    quantity = 10
    price = 5.0
    context.inventory.add_product(product_id, product_name, quantity, price)

# Step 3: Then the inventory should contain "Coffee"
@then('the inventory should contain "{product_name}"')
def step_impl(context, product_name):
    assert context.inventory.has_product(product_name), f'Product "{product_name}" not found in the inventory'
