class MyException(Exception):
    def __init__(self,message, code) -> None:
        super().__init__(f"Error Code {code} : {message} ")
    
x = MyException("System Critical Error Occured",500)
print(x)