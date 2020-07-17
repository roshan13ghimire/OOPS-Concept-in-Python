#Author - Roshan Ghimire


#Static_Method


class Employee:
    
    
    @staticmethod      #StaticMethod
    def isHoliday(day):
        if day == "Saturday":
            return True
        else:
            return False
print(Employee.isHoliday("Saturday"))