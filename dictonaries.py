fruits = [ 
    {"itemname": "Apples", "cost": 1},
    {"itemname":  "Banana", "cost":2},
    {"itemname": "Orange", "cost":3}
]

for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit["itemname"]}  ${fruit["cost"]}")

usercart = []
while True:
    userinput = int(input("Buy something by entering the number: "))
    print(f" You bought {fruits[userinput]["itemname"]}, it costs ${fruits[userinput]["cost"]}")
    usercart.append(fruit["itemname"])
    if userinput == "N":
        print(usercart)
        break
