import random
import string
from abc import ABC, abstractmethod

class Order:
    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.status = "Pending"
        
    def set_status(self, status):
        self.status = status
    def show_staus(self):
        print("Satus: Payment "+self.status)

class Item(Order):
    def __init__(self):
        self.ItemType = input("Enter Item Type: ")
        self.ItemName = input("Enter Item Name: ")
        
    def FetchOrderID(self):
        Order.__init__(self)
        print("Order Status: Payment ",self.status ,"\nOrder ID: ",self.id )
    
    def PaymentStatus(self):
        
        if not paymentProcessor.pay():
            self.set_status("Rejected")
            super().show_staus()
            return
        print(f"Payment for order {self.id} is successful")
        self.set_status("Paid")


class AuthenticationModule:
    def __init__(self):
        self.authorized = False
        self.code = None
    
    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))
        
    def authorize(self):
        inpcode = input("Enter the code: ")
        self.authorized = inpcode==self.code
    def is_authorized(self):
        return self.authorized

class paymentProcessor:
    
    def pay():
        authorizer = AuthenticationModule()
        authorizer.generate_sms_code()
        print(paymentProcessor.returnGeneratedCode(authorizer))
        authorizer.authorize()
        if not authorizer.is_authorized():
            return False
        return True
        
    def returnGeneratedCode(AuthenticationModule):
        return AuthenticationModule.code
        


item = Item()
item.FetchOrderID()
item.PaymentStatus()
