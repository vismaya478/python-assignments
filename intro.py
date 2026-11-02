# class Student:
#     name = "student name"
#     email = "student mail"
#     college = "quest"

#     def get_details(self):
#         print(self.name, self.email, self.college)

   
# vismaya = Student()
# alan = Student()
# vismaya.get_details()
# print(vismaya.name)
# print(type(vismaya))
# print(id(vismaya))



class Students:
    college = 'Quest'

    # def __new__(self):
    #     print("Object created")

    def __init__(self, id, name, email):  #constructor 
        print("Object initialization")
        self.stud_id = id
        self.stud_name = name
        self.stud_email = email

    def get_details(self):
        print(self.stud_id,self.stud_name,self.stud_email)


alisha = Students(2004,'alisha','alicha.co.cin')
alisha.get_details()
print(alisha.stud_id)
