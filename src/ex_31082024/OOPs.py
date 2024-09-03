#Class classname:
    #Attributes
     # all the variables
    #Behavior
     #Methods(Functions)

class Dog:

    #Attributes
    name = None
    color = None

    #Behaviour

    def __init__(self,name): # this is contructor function
        print("Object created with name",name)

    def sleep(self):
        print("Sleep")

dog1 = Dog("Chow")
dog1.sleep()