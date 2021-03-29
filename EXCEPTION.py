# try:
#     age = int(input('Age:'))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# # anticipate these problems and use try so your program does not crush

############################COMMENTS################# NOT TO EXPLAIN WHY'S AND HOW'S


#############CLASSES########3CLASSESS

# Used to define new types ----------different from conversion--------
#numbers = [1, 2, 3,]
#-define a class
#EXAMPLE THE CONCEPT OF A POINT

# numbers = [1,2,3]
# point

# 1. start bf defining a class
class Point:                                #capitalize the first character and NO underscores
    def move(self):
        print("move")             # no underscores used and Capitalized at the first character

    def draw(self):
        print("draw")



point1 = Point()               #objects are the instances based on the class )in this eg ----point1-----is the object
point1.x = 10                   #they can have attributes set anywhere in our program (.x, .y)
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)