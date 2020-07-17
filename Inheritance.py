#Author - Roshan Ghimire

#Inheritance

class Employee:   #Parent_Class
    def __init__(self,fname,lname,age):   #Constructor
        self.fname = fname
        self.lname = lname
        self.age = age
        
class Programmer(Employee):   #Derived_Class
    def __init__(self,fname,lname,age,proglanguage,experience):
        super().__init__(fname,lname,age)                        #Super method will call the init method of class Employee
        self.proglanguage = proglanguage
        self.experience = experience
    

roshan = Programmer("Roshan","Ghimire",20,"Python",2)
ravi = Programmer("Ravi","Yadav",21,"Python",2)


print(roshan.proglanguage)
print(roshan.experience)