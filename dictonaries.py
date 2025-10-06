
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

# spots = int(input("How many parking spots: "))
# yesterday = input("WHat is yesterdays: ")
# today = input("What is todays: ")

# output = 0 #counter
# for spot in range(spots): # 0-># of spots
#     if yesterday[spot] == today[spot] and yesterday[spot]!= ".":
#         output +=1
    
# print(output)
    
    

import random
import time


def spinrow():
    numbers = ["1","2","3","4","5"]
    result = []
    for number in range(3):
        result.append(random.choice(numbers))
    return result
def printrow(row):
    print(" : ".join(row))
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "1":
            return bet * 5
        elif row[0] == "2":
            return bet * 8
        elif row[0] == "3":
            return bet * 10
        elif row[0] == "4":
            return bet * 15
        elif row[0] == "5":
            return bet * 20
    return 0
        
        

def main():
    balance = 100

    print(" Welcome to number slots!")
    print("-------------------------")
    print("Numbers:1-5 inclusive")

    while balance > 0:
        print(f"Your balance: ${balance}")
        bet = input(" How much would you like to bet? :")
        if not bet.isdigit():
            print("Invalid bet amount")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue
        if bet <= 0:
            print("Bet must be greater than 0!")
            continue
        balance -= bet

        row = spinrow()
        text = "Spinning..."
        for period in range(text.count(".")):
            print(text)
            time.sleep(.5)
            text = text[:-1]
        printrow(row)

        payout = get_payout(row, bet)
        if payout >= 150:
            print("*********************************")
            print("RNGESUS WOOOO WOOO ")
            print(f" YOU HAVE WON ${payout}!!!!")
            print("*********************************")
        elif payout >= 100:
            print("GRAND WINNER!!!!")
            print(f" YOU HAVE WON ${payout}!!!")
        elif payout >=50:
            print("GREAT WIN!! ")
            print(f" YOU HAVE WON ${payout}!!")
        elif payout > 0:
            print(" WINNER!")
            print(f" YOU HAVE WON ${payout}!")
        else:
            print(" Aw man you didnt win :/ ")
        balance += payout
if __name__ == '__main__':
    main()






