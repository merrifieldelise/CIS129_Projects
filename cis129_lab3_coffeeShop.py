#Author: Elise Merrifield
#CIS129 lab3
#create a text program that calculates the total of a persons coffee shop purchase


#defining variables
CoffeePrice = 5
MuffinPrice = 4

#new variable prices
CakePopPrice = 3
FizzyJuicePrice = 5

#seting up structure for final print
print("****************************************")
print("My Coffee and Muffin Shop")

#requesting the number of each purchased by the user
CoffeeInput = int(input("Number of coffees bought?\n"))
MuffinInput = int(input("Number of muffins bought?\n"))
#inputs for new items
CakePopInput = int(input("Number of cake pops bought?\n"))
FizzyJuiceInput = int(input("Number of fizzy juices bought?\n"))

#more structure for final print
print("****************************************")
#inserting a new line between print statements
print("\n")

#using if else statement to get CoffeeTotal
if CoffeeInput > 0:
    CoffeeTotal = CoffeePrice * CoffeeInput
else:
    CoffeeTotal = 0

#using if else to calculate Muffin total
if MuffinInput > 0:
    MuffinTotal = MuffinPrice * MuffinInput
else:
    MuffinTotal = 0

#Creating cake pop total
if CakePopInput > 0:
    CakePopTotal = CakePopPrice * CakePopInput
else:
    CakePopTotal = 0

#Creating FizzyJuiceTotal
if FizzyJuiceInput > 0:
    FizzyJuiceTotal = FizzyJuicePrice * FizzyJuiceInput
else:
    FizzyJuiceTotal = 0

#pretax price calculation, adding new variables
SubTotal = CoffeeTotal + MuffinTotal + CakePopTotal + FizzyJuiceTotal

#calculating tax
Tax = SubTotal*0.06

#calculating total, also adding new variables
Total = MuffinTotal + CoffeeTotal + CakePopTotal + FizzyJuiceTotal + Tax

#compleating final print statement
print("****************************************")
print("My Coffee and Muffin Shop Receipt")
#printing coffee info
print(str(CoffeeInput)+ " " + "Coffees at $5 each: $"+ str(CoffeeTotal))
#printing muffin info
print(str(MuffinInput)+ " "+ "Muffins at $4 each: $"+ str(MuffinTotal))
#printing cake pop info
print(str(CakePopInput)+" "+ "Cake Pops at $3 each: $"+ str(CakePopTotal))
#printing fizzy juice info
print(str(FizzyJuiceInput)+ " "+ "Fizzy Juices at $5 each: $"+ str(FizzyJuiceTotal))
#printing tax info
print("6% Tax: $" +str(Tax))
#adding structure and final total
print("---------")
print("Total: $" + str(Total))
print("****************************************")