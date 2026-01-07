#Inheritance in python 
#Creating a new class from existing class is bacially inheritance .
#It inherites either methods or attributes .
#if a child has to use or change/modify parents method is super method.

# class Animal:
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = name
    
#     def sound(self):
#         pass
    
# class Leach(Animal):
#     def __init__(self, name, age,vertible):
#         super().__init__(name, age)
#         self.vertible = vertible
    
#     def sound(self):
#         return "Leach is making sound"
    
# black_leach =Animal("Black Leach ", 5, True)
# print(black_leach.name)


#make a class called "smartphone" that inherits from phone
#It should have a new attribute called "memory" and a method called "take photo" 




# class Phone:
#     def __init__(self, brand):
#         self.brand = brand
    
 
# class Smartphone(Phone):
#     def __init__(self, brand, memory):
#         super().__init__(brand)
#         self.memory = memory 
    
#     def take_photo(self):
#         return "Photo is clicked"

# hello = Smartphone("iPhone", 256)
# print(hello.brand)    
# print(hello.memory)  
# print(hello.take_photo()) 


# Multiple Inheritance 
# class Employee:
#     def __init__(self,name):
#         self.name = name 

# class Salary:
#     def __init__(self,salary):
#         self.salary= salary 

# class Payroll(Employee,Salary):
#     def __init__(self, name,salary):
#         Employee.__init__(self,name)
#         Salary.__init__(self,salary)
    
#     def get_salary(self):
#          return self.salary
#     def get_name(self):
#          return self.name
        

# f = Payroll("sam",120)
# print(f.get_name())
# print(f.get_salary())


#task related to multiple inheritance 
#Functional Designation type multiple inheritaance .
#Create a class imternship thar inherits from employee and functional designation designation and department class and add anew attribute called "internship dutation "
#get all the interns related to specific department and functional designation.
#get the longest survival of an intrn in a particular department and functional designation 
#get the total numver of interns in a particular department and functional designation 

class Employee:
    def __init__(self, name):
        self.name = name 

class Functional_designation:
    def __init__(self, position):
        self.position = position 

class Department:
    def __init__(self, dname):
        self.dname = dname 

class Internship(Employee, Functional_designation, Department):
    def __init__(self, name, position, dname, intern_duration):
        Employee.__init__(self, name)
        Functional_designation.__init__(self, position)
        Department.__init__(self, dname)
        self.intern_duration = intern_duration

    def __str__(self):
        return {self.name}, {self.position}, {self.dname},{self.intern_duration}

interns = [
    Internship("Samir", "HR", "Creative_department", "9-10"),
    Internship("Aisha", "Finance", "Accounting_department", "10-11"),
    Internship("Rahul", "Marketing", "Digital_department", "11-12"),
    Internship("Neha", "IT", "Development_department", "12-1"),
    Internship("Vikram", "Sales", "Sales_department", "1-2"),
    Internship("Priya", "Design", "Creative_department", "2-3"),
    Internship("Karan", "Operations", "Operations_department", "3-4"),
    Internship("Ananya", "HR", "Recruitment_department", "4-5"),
    Internship("Rohan", "Finance", "Budget_department", "5-6"),
    Internship("Sneha", "Marketing", "Content_department", "6-7")
]

for i in interns:
    print(i)







