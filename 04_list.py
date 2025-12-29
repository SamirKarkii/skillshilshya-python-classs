# is list memory suff or insuff? pre allocate va hunxha just like cash so ..
# first_list = []
# print(type(first_list))

# middle of element 
# a = [1,2,3]
# print(a[1])
# print(a[2])
# print(a[0])
# print(a[::-1]) 

my_list = [1,2,3,4]
#adding element ------
#append - add to the end 
# my_list.append("end item")

# #insert at index 1 
# my_list.insert(1, "new item at 1")
# print((len(my_list)))
# # print(my_list)

# # insert as append
# my_list.insert(4,5)            #incase of printing directily it gives none as result 
# print((my_list))

# inner_list = [1,2,45,3]

# # print(my_list+inner_list)     #after concad diff memory address
# my_list.extend(inner_list)
# print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

print(my_list.index(1))

my_list.clear()
print(my_list)


# always take first occurance 
print(my_list.index(0))
my_list.remove(4)
print(my_list)

# remove ko ne ghar ma her !
#pop
value = my_list.pop()
print(my_list)


# always take first occurance
#interms of element also work for duplicate 