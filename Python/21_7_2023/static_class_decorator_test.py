class FixedFloat:
    def __init__(self,amount) -> None:
        self.amount = amount
        
    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"
    @classmethod
    def from_sum(cls,val1,val2):
        return cls(val1+val2)
    
number = FixedFloat(8.3255)
print(number.from_sum(4.45345,.999))
print(number.__class__)

    
class Euro(FixedFloat):
    def __init__(self, amount) -> None:
        super().__init__(amount)
        self.symbol = "$"
        
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'
        
tempVar = Euro.from_sum(4.546,45.3453)
print(tempVar)
