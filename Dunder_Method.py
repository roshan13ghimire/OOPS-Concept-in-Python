#Author - Roshan Ghimire

#Dunder_Method


class Employee:
    def __init__(self,fname,lname,age):   #Constructor
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def __add__(self,nextt):        #Dunder_Method
        return self.age + nextt.age
        
roshan = Employee("Roshan","Ghimire",21)
ravi = Employee("Ravi","Yadav",22)

print(roshan + ravi)
