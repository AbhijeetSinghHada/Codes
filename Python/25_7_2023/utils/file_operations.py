def save_to_file(content, filename):
    with open(filename,'w') as fs:
        fs.writelines(content)
        
def read_file(filename):
    with open(filename,'r')as fs:
        return fs.read()
    
print(__name__)