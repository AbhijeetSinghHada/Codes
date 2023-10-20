from dataclasses import dataclass, field


@dataclass
class D:
    x: list = field(default_factory=list)

assert D().x is not D().x

class A:
    
    def __init__(self,x= []):
        self.x = x


obj1 = A([1,2,3])
obj2 = A([3,4,5])

print(obj1.x)