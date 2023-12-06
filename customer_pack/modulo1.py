
class Customer:

    store = "ADIDAS 012"

    def __init__(self, name, email, dni, product=None, cost=None):
        self.name = name
        self.email = email
        self.dni = dni
        self.purchase = []
        
        if product is not None and cost is not None:
            self.add_purchase(product, cost)
    
    def add_purchase(self, product, cost):
        self.purchase.append({"product": product, "cost": cost})
    
    def pagar(self):
        total = sum(purchases["cost"] for purchases in self.purchase)
        return f"{self.name}, your total purchase amount is {total}"

    def __str__(self):
        return f"{self.name} está comprando en la tienda {Customer.store}"
