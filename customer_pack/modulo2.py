import json

data = {}
username = ()
password = ()

# ----> NUEVO USUARIO

def signup(username, password):
    username = input("Enter your email: ")
    password = input("Create a password: ")

    if username in data:
        print("User already registered")
    else:
        data[username] = password
        print("User created succesfully !")


# ----> INICIAR SESION

def login(username, password):
    username = input("User or email: ")
    password = input("Password: ")

    if username in data and data[username] == password:
        print(f"Welcome {username}!")
    else:
        print("Incorrect username or password.")


# ----> MOSTRAR USUARIO

def show():
    print("Registered users: ")
    for username, password in data.items():
        print(f"User: {username}\nPassword: {password}")

# ----> GUARDAR EN ARCHIVO

def saveData():
    with open("/Users/gaga/Desktop/Entregas Py#50190 - Johan Garcia/customer_pack/files.txt", "w") as file:
        json.dump(data, file)
