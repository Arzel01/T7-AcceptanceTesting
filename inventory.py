class Product:
    def __init__(self, product_id, name, quantity, price):
        self.id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price


class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity, price):
        if name in self.products:
            return False
        self.products[name] = Product(product_id, name, quantity, price)
        return True

    def has_product(self, name):
        return name in self.products

    def list_products(self):
        return list(self.products.keys())

    def update_quantity(self, name, quantity):
        if name in self.products:
            self.products[name].quantity = quantity 
            return True
        return False
    
    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            return True
        return False
