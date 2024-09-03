class VWoLoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "rohit@gmail.com" and self.password == "Rohit":
            print("Allowed")
        else:
            print("Not Allowed")



obj = VWoLoginPage("rohit@gmail.com","Rohit" )
obj.login_confirm()