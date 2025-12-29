# #arithmatic operations 
# #addition operators 
# a = 1
# b = 2
# c = a+b
# print(c)

# #subtraction
# # d = a-b
# # print(d)

# # #multiplication 
# # e = a*b
# # print(e)

# # #division
# # # e = a/0
# # # print(e)

# # #modulus (remainder )
# # e =a%b
# # print(e)

# #floor division
# e = a//b
# print(e)

# #exponential 
# e = a**b
# print(e)

"""Comparision(relational )operators"""

# c = a!=b #not equals to 
# print(c)

# c = a ==b  #equals to
# print(c)

# c = a>b
# print(c)

# c = a<b 
# print(c)

'logical operators '
# a = True
# b = False
# c = a and b
# print(c)

# d = a or b
# print(d)

# listing = [1,2,3,4]
# setting = {4,5,6,9}
# # #only in case of empt , it reads a false , if value then always tru

# # if listing and setting:
# #     print("True")
# # else:
# #     print("False")


# # #task two (important )
# # listing = [1,23,4]
# # if not listing:
# #     print("true")
# # else:
# #     print("false")

# if not listing and not setting:
#     print("TRUE")

# else:
#     print("FALSE")

# #assignment operator 
# a = 10
# a+=20
# print(a)

# a-=10
# print(a)

# a*=5
# print(a)

# a/=5
# print(a)

# a%=0
# print(a)


# a=5
# a**=5
# print(a)

# #float division
# a=5
# a//=5
# print(a)

'''Membership Operators '''

# a =10
# b =20
# c = a in b  #only using with iterable
# print (c)

# a=10
# b=20
# c = a not in b
# print(c)


# a = [1,2,3,4]
# if 1 in a:
#     print("True ")
# else:
#     print(False)

#use in operator in dictionary 
#keys or values to check membership

a = {'name':'samir', 'age':21}
if 'name' in a.keys():
    print("True")
else:
    print(False)

#in terms of string:
string_value = "python"
if 'p' in string_value:
    print("True")
else:
    print("False")