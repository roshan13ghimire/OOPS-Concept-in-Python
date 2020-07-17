
# Author - Roshan Ghimire



#Creating_a_Class
class Employee:
    pass

roshan = Employee()
ravi = Employee()

roshan.fname = "Roshan"    
ravi.fname = "Ravi"

roshan.lname = "Ghimire"
ravi.lname = "Yadav"

roshan.age = "20"
ravi.age = "22"

print(roshan.age)
print(roshan.fname)


#Instead of writing these objects (fname,lname and age) two times,simply create a class and define these inside it as below.



class Employee:
    def __init__(self,fname,lname,age):    #Constructor
        self.fname = fname
        self.lname = lname
        self.age = age
        
roshan = Employee("Roshan","Ghimire",20)
ravi = Employee("Ravi","Yadav",22)

print(roshan.fname)

