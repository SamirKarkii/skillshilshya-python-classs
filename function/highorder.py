#high order functions 
# it takes function as argument 
 #wrapper higher ordser function 





# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} is called with arguments {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#     return wrapper

# @logger
# def rev_string(samir):
#     return samir[::-1]

# print(rev_string('samir'))


# def asmin(func):
#     def samir(*bis,**asmmm):
#         print(*bis)

#     return samir

# @asmin
# def rev(name):
#     return name[::-1]
# rev("sdkjfbshjdfb")




# def logger(func):
#     def wrapper(*args, **kargs):
#         print(*args)
#     return wrapper

# @logger
# def rev_string(sam):
#     return sam[::-1]

# rev_string("asminnnn")


# def asmin(thar):
#     def samir():
#         print(thar)
#     return samir()

# asmin("don")



# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b

# # def calculate(func,a,b):
# #     return add(a,b)


# print(add(2,3))

#Built in higher order function map, filter, reduce 
# def square(num):
#     if num%2==0:
#        return True
#     else:
#        return False
# numbers = [1,2,3,4,5]

# sq_numbers = map(square, numbers)
# print(sq_numbers) #iterator hunxha 
# print(list(sq_numbers)) #then does conversion (itreable )

"-------------------------------------------------------------------------"
# def square(num): #fun
#    return num.lower()
# string = ["HAPPY", "NEW", "YEAR"]

# LOWER_STRING = map(square,string) #higher order 
# print(LOWER_STRING)
# print(list(LOWER_STRING))
"-----------------------------------------------------------------"

#find the sum of each nested list and return true or false if sum>10
# def nested(num):
#    if sum(num) > 10:
#       return True
#    else:
#       False
   
# number = [[1,2,3], [3,4,5],[6,7,8]]

# Sum_of_Num = map(nested,number) #higher order 
# print(list(Sum_of_Num))

"------------------------------------------------------------------"
#Filter Function
# def is_even(num):
#     return num%2 ==0
# number = [1,2,3,4,5,6]
# even_number = filter(is_even, number)
# print(list(even_number))

"-------------------------------------------------------------"
#filter out the words which have length freater than 3
# def filteri(string):
#     if len(string)<4:
#         return True
#     else:
#         return False

# number = ["sami", "dada", "dadagang"]
# length_greater = filter(filteri, number)
# print(list(length_greater))

"-----------------------------------------------------------"
#filter out the dictionary items based on some condition like 'name' key greater than 3
"----------------------------------------------------------"

#reduce function:
from functools import reduce 
# def add(x,y):
#     return x+y

# numbers = [1,2,3,4,5]
# sum_of_numbers = reduce(add,numbers)
# print(sum_of_numbers)
"------------------------------------------------------"
#Find the maximum number from the list using redce function 
def add(x,y):
    if x>y:
        return x
    else:
        return y

numbers = [1,2,3,4,5]
sum_of_numbers = reduce(add,numbers)
print(sum_of_numbers)
