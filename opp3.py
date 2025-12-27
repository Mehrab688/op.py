class Employee:
    
    
    
    
    def __init__(self):
        print('Employeee created')
        
    def __del__(self):
        print("Destructor called")
        
def Create_obj():
        print('Making Object...')
        obj = Employee()
        print("Function end...")
        return obj
        
        
print("Calling Create_obj() function...")
obj = Create_obj()
print('Peogram End...')


