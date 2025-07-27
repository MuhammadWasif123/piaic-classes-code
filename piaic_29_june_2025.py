# # def is_valid_age(age:int):
# #     if age>18:
# #         return True
# #     else:
# #         return False
    

# # result=is_valid_age(16)
# # print(is_valid_age(16));
# # print(result)

# # name="wasif"
# # print(id(name))
# # print(name)

# # name="hamza"
# # print(id(name))
# # name[0]='t'

# # print(name)

# # As the two different variables values are the same hence python will not create another new variablw with same value
# # name1="wasif"
# # print(id(name1))

# # name2="wasif"
# # print(id(name2))

# # Example 2 as it founds different values then it will give another variable reference
# # name1="wasif"
# # print(id(name1))

# # name2="Wasif"
# # print(id(name2))


# # traffic_light:frozenset=frozenset({"red","blue","black"})
# # traffic_light.add("green")
# # print(traffic_light)

# # SETS AND DICTIONARY AND FUNCTIONS

# # val={}
# # print(type(val))


# # numbers=[1,3,56,68]
# # newNumbers=numbers

# # newNumbers[0]="12"

# # print(numbers[0])


# # Short hand of If and Else Statements in Python (like ternary operator in JS)

# # age=15

# # result="you are allowed" if age >=18 else "You are not allowed"

# # print(result)

# # Object Oriented Programming in Python(OOP)
# # We make objects from the classes
# # Classes is utilized to make objects and then objects will be further used for more functionality
# # Class is basically a kind of blur print to make objects fron it
# # One more point classes have to things 1.Properties 2.Methods
# # Properties is just like variables and in Methods we will apply some logic
# # Now In order to make objects from the class Constructors are utilized


# # class House:
# #     def __init__(self,address,numberOfRooms,numberOfDoors):
# #         self.address=address
# #         self.numberOfRooms=numberOfRooms
# #         self.numberOfDoors=numberOfDoors
# #     def ring_bell(self):
# #         print("Ding Dong")


# # h1=House("nazimabad",12,31)
# # h1.address="north nazimabad"
# # print(h1.address)
# # print(h1.numberOfRooms)
# # print(h1.numberOfDoors)
# # h1.ring_bell()
# # h2=House("Johar",10,2)
# # print(h2.address,h2.numberOfRooms,h2.numberOfDoors) 


# # class Apartments():
# #     def __init__(self,adrs,fNumber):
# #         self.address=adrs
# #         self.numberOfRooms=3
# #         self.numberOfDoors=5
# #         self.flatNumber=fNumber


# # h1=Apartments("Main Johar Chowrangi","32A")

# # print(h1.address)
# # print(h1.flatNumber)



# class House:
#     def __init__(self,address,numberOfRooms,numberOfDoors):
#         self.address=address
#         self.numberOfRooms=numberOfRooms
#         self.numberOfDoors=numberOfDoors
#     def ring_bell(self):
#         print("Ding Dong")

# class Apartment(House):
#     def __init__(self,address,numberOfRooms,numberOfDoors,fNumber):
#         super().__init__(address,numberOfRooms,numberOfDoors)
#         self.flatNumber=fNumber

# h2=Apartment('Newyork',4,1,"32A")
# print(h2.numberOfDoors)
# print(h2.address)
# print(h2.numberOfRooms)
# print(h2.flatNumber)

bool("")