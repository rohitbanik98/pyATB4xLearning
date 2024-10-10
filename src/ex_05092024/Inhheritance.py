# Inheritance is like extend in DART


class grand_parent:
    grand_parenthome = "1BHK"
class Father(grand_parent):
    Fatherhome = "FatherBHK"

class Mother(grand_parent):
    Motherhome = "MotherBHK"
class child(Father, Mother):
    childhome = "3BHK"


Par_obj = Father()
print(Par_obj.Fatherhome)

child_obj = child()
print(child_obj.grand_parenthome)# multi-level inheritance
print(child_obj.Motherhome) #multi-level + multiple inheritance
print(child_obj.childhome)
