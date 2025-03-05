# Author: Elise Merrifield
# CIS129 lab5
# Part 3 - Bottle Return Program

#step one declare variables
payout_per_bottle = .10
NBR_OF_DAYS = 7
keep_going = "y"

#step two Loop to run program again
while keep_going == "y":
    # set variables that need to reset after each session
    total_bottles = 0
    today_bottles =0
    total_payout = 0
    counter = 1

    # step 3 code to set values of variables
    for counter in range(1, NBR_OF_DAYS + 1):
        #get each days number of bottles and calculate total bottles for the week
        today_bottles = int(input(f'Enter number of bottles for day #{counter}: '))
        total_bottles += today_bottles
        #calculate total payout
        total_payout = total_bottles * payout_per_bottle
        #code to print totals
    print(f'\nThe total number of bottles collected is: {total_bottles}')
    print(f'The total payout for the bottles collected is: ${total_payout: .1f}')
    #ask if user would like to run again
    print("Do you want to want to enter another week's worth of data?")
    keep_going = input("(Enter y or n): ")


