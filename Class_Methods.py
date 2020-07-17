#Author - Roshan Ghimire

#Class_Methods


#When we want to change  some variables of the class, We use ClassMethod.


class Employee:
    
    inc = 2 
    def __init__(self,fname,lname,sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
    
    
    def increase(self):
        self.sal = self.sal * Employee.inc
     
    @classmethod              #ClassMethod
    def change_sal(ch,amount):
        ch.inc = amount 
        
roshan = Employee("Roshan","Ghimire",2000)
ravi = Employee("Ravi","Yadav",2200)

print(roshan.sal)
Employee.change_sal(2)
roshan.increase()
print(roshan.sal)

