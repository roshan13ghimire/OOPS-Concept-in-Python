#Author - Roshan Ghimire

#Instance_And_Class_Variable
class Employee:
    
    inc = 2    #Class Variable 
    def __init__(self,fname,lname,sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
    
    def increase(self):
        self.sal = self.sal * Employee.inc
        
roshan = Employee("Roshan","Ghimire",2000)
ravi = Employee("Ravi","Yadav",2200)

print(roshan.sal)   
roshan.increase()         #We can increase the salary by using the new function called increase.
print(roshan.sal)
print(roshan.__dict__)    #We can print the dictionary values of the object.
print(Employee.__dict__)  #We can also print the dictioary of the class.

