fruits = [    
{
   "itemname": "Apples",
   "cost": 1
},
{
    "itemname": "Bananas",
    "cost": 2
},
{
    "itemname":"Orange",
    "cost": 1.5
},
]

for index, item in enumerate(fruits):
    print(index+1,":", item["itemname"], item["cost"])
    print("-----------------------")

usercart = []
while True:
    usersearch = input("What item would you like to purchase?(Use number)(type N to exit): ")
    if usersearch == item["itemname"]:
        usercart.append(usersearch)
        
    elif usersearch == "N":
        print(usercart)
        break
    
   




