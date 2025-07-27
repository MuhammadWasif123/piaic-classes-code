from abc import ABC,abstractmethod
# class House:
#     def __init__(self,address):
#         self.address:str= address
#         self.no_of_doors:int =2
#         self.no_of_rooms:int=4
    
#     def call_lift(self):
#         print(f'{self.address} Lift is called')


# h1=House(address="xyz 123")
# h2=House('xyz 124')
# h1.call_lift()


# class Student:
#     def __init__(self,name,rollNo,age):
#         self.name:str=name
#         self.rollNo:int=rollNo
#         self.institute:str="University of Karachi"
#         self.age:int=age

#     def getAdmission(self):
#         print(f'Roll No: {self.rollNo} of age {self.age} can take admission now')

#     def payFee(self):
#         print(f'Roll No: {self.rollNo} "pay all of your unpaid fee dues"')



# s1=Student(name="Muhammad Wasif Khan",rollNo=45,age=33)

# print(s1.name)
# print(s1.age)
# print(s1.rollNo)
# print(s1.institute)

# s1.payFee()


# class Course:
#     def __init__(self,courseName):
#         self.courseName=courseName
#         self.students=[]

#     def addStudent(self,student):
#         self.students.append(student)



# c1=Course("AI")
# c1.addStudent(s1)
# print(c1.students[0].name)
# print(c1.students[0].rollNo)
# print(c1.students[0].age)

# Inheritance concept in Python

# class Human:
#     def __init__(self,name,age):
#         self.name:str= name
#         self.age:int =age

    
#     def eatMethod(self):
#         print("I can eat both meat and vegetables")




# class Student(Human):
#     def __int__(self, name, age,rollNo):
#         super().__init__(name,age)
#         self.rollNo=rollNo

# Polymorphism in Pyhthon
# Method Overriding in Python Polymorphism

# class Teacher(Human):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age)
#         self.salary:int=salary

#     def eatMethod(self):
#         print("I eat only vegetables")

# h1=Human(name="wasif",age=23)
# # print(h1.age)
# # print(h1.name)
# # h1.eatMethod()

# t1=Teacher("Kamal",age=44,salary=300000)
# print(t1.name)
# print(t1.age)
# print(t1.salary)
# t1.eatMethod()


# class BankAccount():
#     def __init__(self,name,accountNumber,balance):
#         self.name:str=name
#         self.accountNumber:str=accountNumber
#         self.__balance:int = balance
    
#     def withdraw(self,account_no,amount):
#         if self.accountNumber != account_no:
#             return "Invalid Account Number"
#         else:
#             self.__balance -=amount


# class P