# class Dog:
#     def sound(self):
#         print("Dog barks")
# class Cat:
#     def sound(self):
#         print("Cat mew")
# class Cow:
#     def sound(self):
#         print("Cow moooo")
# cat = Cat()
# dog = Dog()
# cow = Cow()
# dog.sound()
# cat.sound()
# cow.sound()





# class Whatsapp:
#     def send(self):
#         print("Sending message through whatsapp")
# class Email:
#     def send(self):
#         print("Sending message email")
# class SMS:
#     def send(self):
#         print("Sending message through SMS")

# def send_notification(API):
#     API.send()

# w = Whatsapp()
# e = Email()
# s = SMS()

# send_notification(w)



# class Calculator:
#     def add(self, a ,b):
#         return a+b
#     def add(self,a,b,c):
#         print(a+b+c)
#     def add(self, a, b,c,d):
#         return a+b+c+d

# obj = Calculator()
# print(obj.add(23,35))


# class Student:
#     def __init__(self,name):
#         self.name = name
#     def __init__(self, name, age = 0):
#         self.name = name
#         self.age = age
# alan = Student('alan',23)

class Animal:
    def sound(self):
        print("soundd")

class Dog(Animal):
    def sound(self):
        print("dog bark")
d = Dog()
d.sound()
print(Dog.__mro__)