
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




fruits = [ 
        {"itemname": "Apples", "cost": 1},
        {"itemname":  "Banana", "cost":1.5},
        {"itemname": "Orange", "cost":.5},
        {"itemname":  "Grapes", "cost": .5}
    ]

#     for index, fruit in enumerate(fruits):
#         print(f"{index} : {fruit["itemname"]}  ${fruit["cost"]}")

#     usercart = []
#     usertotal = 0
#     while True:
#         userinput = input("Buy something by entering the number: ").upper()
#         if userinput == "N":
#             print(usercart)
#             print(f" ${usertotal}")
#             break
#         else:
#             userinput = int(userinput)
#         print(f" You bought {fruits[userinput]["itemname"]}, it costs ${fruits[userinput]["cost"]}")
#         usercart.append(fruits[userinput]["itemname"])
#         usertotal += fruits[userinput]["cost"]


# buystuffthing()

userinput = input()

usercart = [ fruits[userinput]]