class Car:
    car_count = 0
    def __init__(self, brand, model):
        # self.brand = brand
        self.__brand = brand
        self.__model = model
        Car.car_count += 1
    
    def get_brand(self):
        return self.__brand + "!"

    def printCarName(self):
        return self.__brand + " " + self.__model
    
    def fuel_type(self):
        return "Petrol/Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are a means of transport"
    
    
    def model(self):
        return self.__model


# my_car = Car("skoda","slavia")
# print(my_car.brand)
# print(my_car.printCarName())

# my_new_car = Car("Tata","nexon")
# print(my_new_car.printCarName())

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) 
        self.battery_size = battery_size

    def printCarName(self):
        return f"{self.brand} {self.model}({self.battery_size})"
    
    def fuel_type(self):
        return "electric charge"

# my_elec_car = ElectricCar("Waymo","T1","40KW")
# print(my_elec_car.printCarName())
# print(my_elec_car.battery_size)

# class DieselCar(Car):
#     def __init__(self, brand, model, engine):
#         super().__init__(brand, model)
#         self.engine = engine

# my_car = ElectricCar("tesla","ev1","50 KWH")
# print(my_car._Car__brand)
# print(my_car.get_brand())

# my_tesla = ElectricCar("tesla","m1","50kwh")

# safari = Car("tata","safari")

# print(my_tesla.fuel_type())
# print(safari.fuel_type())

# print(Car.car_count)

myCar = Car("tata","nexon")
# myCar.model = "city"
# print(Car.general_description())

# print(myCar.model())

print(isinstance(myCar,Car))
print(isinstance(myCar,ElectricCar))
