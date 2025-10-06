
#Part 1 of dictionary
# fruits = [ 
#     {"itemname": "Apples", "cost": 1},
#     {"itemname":  "Banana", "cost":2},
#     {"itemname": "Orange", "cost":3}
# ]

# for index, fruit in enumerate(fruits):
#     print(f"{index} : {fruit["itemname"]}  ${fruit["cost"]}")

# usercart = []
# while True:
#     userinput = input("Buy something by entering the number: ").upper()
#     if userinput == "N":
#         print(f"You bought: {usercart}")
#         break
#     else:
#         userinput = int(userinput)
#     print(f" You bought {fruits[userinput]["itemname"]}, it costs ${fruits[userinput]["cost"]}")
#     usercart.append(fruits[userinput]["itemname"])




# fruits = [ 
#         {"itemname": "Apples", "cost": 1},
#         {"itemname":  "Banana", "cost":1.5},
#         {"itemname": "Orange", "cost":.5},
#         {"itemname":  "Grapes", "cost": .5}
#     ]


# for index, fruit in enumerate(fruits):
#         print(f"{index+1} : {fruit["itemname"]}  ${fruit["cost"]}")

# usercart = []
# usertotal = 0
# while True:
#     userinput = input("What would you like to buy?:")
#     for fruit in fruits:
#         if fruit["itemname"] == userinput:
#             print(f"Added {userinput} to your cart! added ${fruit["cost"]} to your total!")
#             usercart.append(f" {userinput} -- ${fruit["cost"]}")
#             usertotal += fruit["cost"]
#     if userinput == "N":
#         for item in usercart:
#             print(item)
#             print("----------")
#         print(f" Your total is ${usertotal} ")
#     else: 
#          print("Please correct your spelling!")
#     # else:
#     #     userinput = int(userinput)
#     #     print(f" You bought {fruits[userinput]["itemname"]}, it costs ${fruits[userinput]["cost"]}")
#     #     usercart.append(fruits[userinput]["itemname"])
#     #     usertotal += fruits[userinput]["cost"]



#     # TEST TEST
#     # usercart = []

#     # while True:

#     #     userinput = input(":")
#     #     for fruit in fruits:
#     #         if fruit["itemname"] == userinput:
#     #             print(userinput)
#     #             usercart.append(userinput)
#     #         if userinput == "N":
#     #             print(usercart)
#     #             break

spots = int(input("How many parking spots: "))
yesterday = input("WHat is yesterdays: ") 
# Array("abc") // List["abc","2"]
# yesterday[0]

today = input("What is todays: ")

output = 0 #counter
for spot in range(spots): # 0-># of spots 
    if yesterday[spot] == today[spot] and yesterday[spot]!= ".":
        output +=1 
    
print(output)
    


    








