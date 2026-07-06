from behave import given, when, then
from inventory import Inventory

@given('the inventory contains products:')
def step_impl(context):
    # Inicializamos un inventario limpio en este escenario
    context.inventory = Inventory()
    
    # Recorremos la tabla de Gherkin e insertamos los productos
    for row in context.table:
        # Enviamos los 4 atributos mínimos requeridos por la rúbrica
        context.inventory.add_product(
            name=row['Product'], 
            quantity=10, 
            price=2.99, 
            category="Groceries"
        )

@when('the user removes the product "{product}"')
def step_impl(context, product):
    # Ejecutamos el método de eliminación y guardamos el resultado por si acaso
    context.output = context.inventory.remove_product(product)

@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    # Evaluamos mediante un assert que el producto ya no exista en el diccionario
    assert product not in context.inventory.products, f"Error: {product} aún sigue en el inventario."
