#mutable data type, which is build and stores key value pairs .


# first = {}
# print(first)
# print(type(first))

#only immutable data type can be dictionary's key and must be unique 




# first_dictionary = {'name':'samir', 'age':26}
# print(first_dictionary.values())
# print(first_dictionary.keys())

# # second_dictionary = {'name':'samir', {'age'}:26}  #hash value change huna sakcha so fetch hudaina list ans sets 
# # print(second_dictionary)

# # first_hash = hash('age')
# # second_hash = hash('age')

# # print(first_hash)
# # print(second_hash)

# print(first_dictionary.items())

# # very important 
# # for key,value in first_dictionary.items():
# #     print(key)
# #     print(value)


# #accessing elements from dictionary
# name = first_dictionary['name']
# print(name)

# #accessing using get() method 
# name = first_dictionary.get('name')
# print(name)
# dict_1={'name':"abcd",'class':23}
# dict_2  ={'age':23,'name':'efgh'}

# print(id(dict_1))
# print(id(dict_2))
# print(dict_1==dict_2)
# print(dict_1 is dict_2)  #checks memory address

# #merging the dictionaries
# #union
# result_dict = dict_1|dict_2
# print(result_dict)

# #upadte merge 
# dict_1.update(dict_2)
# print(dict_1)

# #intersection merge 
# # result1_dict = dict_1 & dict_2
# # print(result1_dict)

# #keyword argument merge 
# result_dicti = {**dict_1,**dict_2}
# print(result_dicti)

#removing keyL value pair 
dict_3 = {'name':'sameer', 'age':21}
# value = dict_3.pop('name')
# print(value)
# print(dict_3)

#pop item 
# value = dict_3.popitem()
# print(value)
# print(dict_3)


#key value 
dict_3['name']= 'samir'
print(dict_3)
