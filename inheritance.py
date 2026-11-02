# class Human:

#     def run(self):
#         print("running")
#     def eat(self):
#         print("eating")
#     def sleep(self):
#         print("sleeping")

# class Student(Human):
#     pass

# alan = Student()
# alan.eat()


# class vehicle:
#     wheels = 4
#     brand = 'Toyota'

#     def start(self):
#         print("Vehicle started")

#     def apply_break(self):
#         print("break applied")

# class Car(vehicle):
#     def color(self):
#         print("matt black")

# innova = Car()
# innova.apply_break()
# print(innova.wheels)

# class miniBus(vehicle):
#     pass

# innova.color()



# class Animal:

#     def __init__(self, name):
#         self.name = name
#         print("parent constructor")

#     def eat(self):
#         print("Animal is eating")

#     def sleep(self):
#             print("Sleep")

# class Cat(Animal):

#     def __init__(self, name):
#         super().__init__(name)
#     def play(self):
#         print("play")
#     def sleep(self):
#         super().sleep()
#         print("Sleeping")

# c = Cat("Luna")
# c.eat()
# c.sleep()




# class Camera:
#     def take_photos(self):
#         print("taking photo")

# class phone(Camera):
#     def make_call(self):
#         print("calling")

# class Smartphone(phone):
#     def browser(self):
#         print("Browsing the internet")

# iphone = Smartphone()
# iphone.take_photos()


# class Grandparent:
#     def farming(self):
#         print("farm")
#     def drive(self):
#             print("G drive")


# class Father:
#     def sportsman(self):
#         print("Sports man")
#     def drive(self):
#             print("F drive")

# class Mother:
#     def talent(self):
#         print("Painting")

#     def drive(self):
#         print("M drive")

# class Child(Father, Mother, Grandparent):
#     pass

# c = Child()
# c.sportsman()
# c.talent()
# c.farming()
# c.drive()







# class Employee:
#     def display(self):
#         print("salary credited")

# class Manager(Employee):
#     def manager_team(self):
#         print("this is manager team")

# class Developer(Employee):
#     def write_code(self):
#         print("write code")