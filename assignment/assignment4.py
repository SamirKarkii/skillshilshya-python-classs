# Assignment 4 
# Task 1: The "FizzBuzz" Classic (Pattern Logic)

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0: #note:python checks from top to buttom
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



# # Task 2: Find the Maximum and Minimum (Array Traversal)
# # Goal: Understand how to keep track of state variables while looping through a list.
# num = [23,45,12,56,89,3,44]
# smallest = num[0]
# largest = num[0]

# for i in num:
#     if i<smallest:
#         smallest = i
#     if i>largest:
#         largest=i

# print('Smallest number in list:',smallest)
# print('largest', largest)


  
# # Task 3: Reverse a Number (Mathematical Loop)
# num = int(input("enter a number you wanna rev: ")) 
# rev_num =0  
# while num>0:
#     digit = num%10
#     rev_num = rev_num*10 +digit
#     num= num//10
# print("reverse number:", rev_num)  












# Task 4: Prime Number Checker (Efficiency Logic)
# Goal: Understand the "break" statement and boolean flags.
# The Problem:Ask the user for a number and determine if it is a Prime Number.
# A prime number is only divisible by 1 and itself.
# Logic: Use a for loop to check if any number from 2 up to the square root of the input divides it perfectly. Use an if/else block to print the final result.


# Task 5: The Fibonacci Sequence (Algorithmic Thinking)
# Goal: Learn how to update multiple variables simultaneously within a loop.
# The Problem:Write a program to generate the first N terms of the Fibonacci sequence.
# The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, ... (Each number is the sum of the two preceding ones).
# Use a loop to calculate the next term and update your "previous" and "current" variables accordingly.
 