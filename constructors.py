class Point:                            #ADD THE CONSTRUCTOR   ####3## CORDINATES ########
    def __init__(self,x ,y):            #THIS METHOD USED TO CINSTRUCT AN OBJECT IT GETS CALLED WHEN YOU CREATE A NEW OBJECT
        self.x = x                  #THE SELF IS A REFERENCE TO THE CURRENT OBJECT
        self.y = y                          #TO INITIALISE THE OBJECT

    def move(self):
        print("move")             

    def draw(self):
        print("draw")



point = Point(10, 20) 
point.x = 15                # this updates the value of x          
print(point.x)


#### EXERCISE ####

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person("John Smith")
john.talk()

bob = Person("bob smith")
bob.talk()




##### === INHERITANCE ==== #######

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print('bark')

    
class Cat(Mammal):
    pass                    # You use the pass when no other function is passed out or written out


dog11 = Dog()
dog11.bark()
