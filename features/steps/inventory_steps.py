from behave import given, when, then
from inventory import InventoryManager


@given('the inventory is empty')
def step_impl_inventory_is_empty(context):
    context.inventory = InventoryManager()


@given('the inventory contains a product "{product_name}"')
def step_impl_inventory_contains_product(context, product_name):
    if not hasattr(context, 'inventory'):
        context.inventory = InventoryManager()

    product_id = f'PROD-{len(context.inventory.products) + 1:03d}'
    quantity = 10
    price = 5.0
    context.inventory.add_product(product_id, product_name, quantity, price)


@when('the user adds a product "{product_name}"')
def step_impl_add_product(context, product_name):
    product_id = 'PROD-001'
    quantity = 10
    price = 5.0
    context.inventory.add_product(product_id, product_name, quantity, price)


@when('the user lists all products')
def step_impl_list_all_products(context):
    context.product_names = context.inventory.list_products()


@then('the inventory should contain "{product_name}"')
def step_impl_inventory_contains(context, product_name):
    assert context.inventory.has_product(product_name), f'Product "{product_name}" not found in the inventory'


@then('the inventory should show "{first_product}" and "{second_product}"')
def step_impl_inventory_should_show_products(context, first_product, second_product):
    expected_products = [first_product, second_product]
    assert context.product_names == expected_products, (
        f'Expected products {expected_products}, but got {context.product_names}'
    )
