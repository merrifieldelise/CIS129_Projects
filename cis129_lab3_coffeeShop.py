#Author: Elise Merrifield
#CIS129 lab3
#create a text program that calculates the total of a persons coffee shop purchase


#defining variables
CoffeePrice = 5
MuffinPrice = 4

#seting up structure for final print
print("****************************************")
print("My Coffee and Muffin Shop")

#requesting the number of each purchased by the user
CoffeeInput = int(input("Number of coffees bought?\n"))
MuffinInput = int(input("Number of muffins bought?\n"))

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

#pretax price calculation
SubTotal = CoffeeTotal + MuffinTotal

#calculating tax
Tax = SubTotal*0.06

#calculating total
Total = MuffinTotal + CoffeeTotal + Tax

#compleating final print statement
print("****************************************")
print("My Coffee and Muffin Shop Receipt")
#printing coffee info
print(str(CoffeeInput)+ " " + "Coffees at $5 each: $"+ str(CoffeeTotal))
#printing muffin info
print(str(MuffinInput)+ " "+ "Muffins at $4 each: $"+ str(MuffinTotal))
#printing tax info
print("6% Tax: $" +str(Tax))
#adding structure and final total
print("---------")
print("Total: $" + str(Total))
print("****************************************")