
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"la voiture est une {self.brand} {self.model} {self.year}")

# creer un objet de la classe car
mon_car = Car("toyota", "corolla", 2020) 

#appeler le mathode display_info()
mon_car.display_info()