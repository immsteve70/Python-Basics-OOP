class Car:
    def __init__(car, brand, model, year):
        car.brand = brand
        car.model = model
        car.year = year

    def display_info(car):
        print(f"Brand: {car.brand}\nModel: {car.model}\nYear: {car.year}\n")

car1 = Car("Toyota", "Hilux", 2009)
car2 = Car("Mitsubishi", "Lancer", 2007)

car1.display_info()
car2.display_info()