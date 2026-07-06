class Product:
    def __init__(self, name, quantity=0, price=0.0, category="General"):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

class Inventory:
    def __init__(self):
        # Usamos un diccionario para buscar productos rápidamente por su nombre
        self.products = {}

    def add_product(self, name, quantity=0, price=0.0, category="General"):
        product = Product(name, quantity, price, category)
        self.products[name] = product

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            return f"Product {name} was removed"
        return f"Product {name} was not found"