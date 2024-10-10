#Encapsulation is basically about private variable

class Myclass:
    public_var = "Public variable"#can be accessible from anywhere
    _protected_var = "Protected variable" #can be accessible only upto same python package
    __private_var = "private_var" #Can't accessible outside of this class


obj = Myclass()
print(obj.public_var)
print(obj._protected_var)
# print(obj.__private_var) can't be accessed