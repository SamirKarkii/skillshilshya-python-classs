#recursive functions
#fibonacci

# def fabonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fabonacci(n-1)+fabonacci(n-2)

# print(fabonacci(4))



# def sum_natural(n):
#     if n==1:
#         return n
#     else:
#         return n + sum_natural(n-1)
# print(sum_natural(5))

# def smallest(lst):
   
#     if len(lst) == 1:
#         return lst[0]

    
#     min_of_rest = smallest(lst[1:])
#     return lst[0] if lst[0] < min_of_rest else min_of_rest
# numbers = [5, 2, 9, 1, 7]
# print(smallest(numbers)) 

a = [1,2,3,44,55,21,12]
print(max(a))
