# # # Assignments 3
# # # Task 1: The Grade Book

# # student_scores = {'samir': [40, 50, 45]}
# # # square brackets are used to look up values by keys just like index a[0]
# # score = student_scores['samir']
# # average = sum(score)/len(score)
# # print(average)



# # # Task 2: Inventory Manager

stock = {"apple":10, "bananas":5, "oranges":0 }

if "pears" in stock.keys():
    print("True")

else:
    print("False")

if"bananas" in stock.keys() and stock["bananas"]<5:
     print("Time to restock bananas :)")


# # Task 3: Simple Login System

# users = {"admin":"1234"}
# users["teacher"]= "password789"


# input_user = input("Enter a user: ")
# input_pass = input("Enter pass: ")
# if input_user in users and users[input_user] == input_pass: #in checks dictionary keys
#     print("Access granted")

# else:
#     print("Access denied") 




