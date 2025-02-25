# Author: Elise Merrifield
# CIS129 lab4
# Part 4 - Python Code, Calculate bonus amounts for the store and employees

# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt = "What were the monthly sales?" # prompt will be a string literal


# This code is to get monthly sales
monthlySales = float(input(prompt))

# This code determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code gets the percent increase in sales
salesIncrease = float(input("Please enter the increase in sales in decimal format."))
salesIncrease = salesIncrease / 100

# This code determines the employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus info
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')
