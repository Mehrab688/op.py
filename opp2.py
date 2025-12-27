class IOSstring:
    def __init__(self):
        self.str1=''
    def get_string(self):
        self.str1=input("Enter String: ")
        
        
    def printstring(self):
        print("Upper case :",self.str1.upper())
        
obj1=IOSstring()
obj1.get_string()
obj1.printstring()
    
