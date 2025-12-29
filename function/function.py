# func may may not be 

# def greet_student(name:str):
#     print(f"Hello , {name}!Welcome to python class.")
#     return f"goood day {name}"

# name = 1
# result = greet_student(name=name) #why none?
# print(result)

# def a(name= "Ram"):
#     return f"goood day {name}"
# print(a())

#  create a small func to calculatr the volume of cuboin

# def vol_cubiod():
#     l = int(input("enter length"))
#     b = int(input("enter breadth"))
#     h = int(input("input height"))
#     return l*b*h
# print(vol_cubiod())

# def rev_list(list=[1,23]):
#     return f"{list[::-1]}"

# print(rev_list())
    
#repeat same message multiple n time using function

def repeat():
    n = int(input("enter a num "))
    name = "samir"
    for i in range(1,n+1):
       print(name)

repeat()