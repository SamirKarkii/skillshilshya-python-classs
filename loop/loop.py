# count =1
# while count<=5:
#     print(count)
#     count +=1

#break
#pass
#continue 


# for i in range (10):
#     print(i)
#     if i%2 ==0:
#         print(f'even number {i} "')
#         continue
#     print(f'odd number:{i}')


# for i in range(1,10):
   

#     if i%2==0:
#         print(i)
#         break

# a = [1, 2, 3, 4, None,2,5]

# for i in a:
#     if i ==None:
#         print("Invalid")
#         break
#     print(i)

# a = [1,2,3,4,None , 2, 5]
# for i in a:
#     if i==1:
#         continue
#     print(i)



# num = [2,3,4,5,6]
# sum = 0
# for i in num:
#     sum = sum+i
# print(sum)


# num = [1,2,3,4,5]
# infinite_low_number = float('inf')
# infinite_high_number = float('-inf')

# for i in num:
#     if i<infinite_low_number:
#         infinite_low_number=i
#     if i>infinite_high_number:
#         infinite_high_number=i

# print(infinite_low_number)
# print(infinite_high_number)

# lising = [["ram", "shyam", "hari", "samir", "gaara"]]

# for index in range(len(lising[0])):
#     lising[0][index] = lising[0][index][::-1]

# print(lising)


listing = [["ram", "shyam", "hari", "samir"]]
for i in range(len(listing[0])):
    listing[0][i]=listing[0][i][::-1]
print(listing)