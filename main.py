from customer_pack.modulo1 import Customer
from customer_pack.modulo2 import *


# Ejecucion del codigo del modulo2 (Entrega pasada)
while True:
    print("(1) Sign up\n(2) Log in\n(3) EXIT")

    option = input("Choose an option (1, 2 or 3): ")

    if option == "1":
        signup(username, password)
        saveData()
    elif option == "2":
        login(username, password)
    elif option == "3":
        print("Good bye!")
        break
    else:
        print("Invalid entry. Please select one of the 3 options..1.")


# Instancias del modulo1
cliente1 = Customer(name="Diana Gallego", email="didi@gmail.com", dni="95200338")
cliente3 = Customer(name="Johan Garcia", email="johan@gmail.com", dni="94967789")
cliente2 = Customer(name="Juan Ignacio Gaga", email="juani@gmail.com", dni="96045783")

cliente1.add_purchase(product="Zapatillas runners", cost=100)
cliente1.add_purchase(product="T-shirt", cost=30)
print("Lista de compras:", cliente1.purchase)
print(cliente1.pagar())

cliente2.add_purchase(product="Socks", cost=23)
print("Lista de compras:", cliente2.purchase)
print(cliente2.pagar())

cliente3.add_purchase(product="Short", cost=41)
print("Lista de compras:", cliente3.purchase)
print(cliente3.pagar())
