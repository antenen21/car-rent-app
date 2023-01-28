# *******************************************************************************************
# *********************************** USER **************************************************
class User:

    def __init__(self, name, lastname, age, gender, address, username_in_sys, password_in_sys, user):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.address = address
        self.username_in_sys = username_in_sys
        self.password_in_sys = password_in_sys
        self.user = user


def search_user(parameter_username):
    for user_listed in users:
        if parameter_username == user_listed["username_in_sys"]:
            print(user_listed)


users = [
    {"name": "Andreas", "lastname": "Antenen", "age": 33, "gender": "male", "address": "Cormoret",
     "username_in_sys": "1",
     "password_in_sys": "1", "online status": "OFFLINE", "type": "admin"},
    {"name": "Robert", "lastname": "Antenen", "age": 65, "gender": "male", "address": "Büetigen",
     "username_in_sys": "2",
     "password_in_sys": "2", "online status": "OFFLINE", "type": "guest"}
]

# ********************************************************************************************
# ************************************ CARS **************************************************


class Cars:
    def __init__(self, brand, model, color, price, status):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.status = status

    def change_price(self, new_price):
        self.price = new_price

    def change_status(self, new_status):
        self.status = new_status


car_choice = [
    {"brand": "toyota", "model": "supra", "color": "black", "price": 60, "status": "not rented"},
    {"brand": "ferrari", "model": "testarossa", "color": "red", "price": 350, "status": "not rented"},
    {"brand": "opel", "model": "astra", "color": "silver", "price": 55, "status": "not rented"}
]


def search_car(parameter_brand, parameter_model):
    for cars_listed in car_choice:
        if parameter_brand == cars_listed["brand"]:
            if parameter_model == cars_listed["model"]:
                print(cars_listed)
