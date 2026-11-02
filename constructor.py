class Car:
    year = 2026 #class attribute
    def __init__(self,brand, model, price):  #parameterized constructor
        print("object created")
        self.brand = brand
        self.model = model
        self.price = price
    def drive(self):
        print("Driving..")

    # def __del__(self):
    #     print("Removed")


innova = Car("toyota","v.2.5",1500000)

maruti800 = Car('suzuki','2001',199999)
# del innova.model
# print(innova.model)   

# del innova
# innova.model


print(getattr(innova,'brand'))
print(getattr(innova,'milage',10))
setattr(maruti800, 'milage', '18km\\l')
print(maruti800.milage)
print(hasattr(innova,'milage'))
print(hasattr(innova,'brand'))
# delattr(innova,'model')
# print(innova.model)


# print(maruti800.year)
# print(innova.brand)
# innova.brand = 'audi'
# print(innova.brand)

# innova.year = 2015
# Car.year = 2023
# print(innova.year)
# print(maruti800.year)