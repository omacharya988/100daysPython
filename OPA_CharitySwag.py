# Program:      OPA_CharitySwag.py
# Date:         Jan 02, 2001
# Author:       Om Prakash Acharya(Student #1100244)
# Description:  Calculates the number of swag items that may be purchased with funds budgeted.
#               This is he solution to coding assignment#1.
print("SWAG Budget Program")
print("\n")

# Print an explanation for the user explaining what the program will do as shown on the console output below
print("This program will calculate how many SWAG Items may be purchased for a company from the money budgeted.")
print("\n")
# Ask the user to enter the description (string) of the SWAG Item and store this value as a string
Items = str ( input("Enter a description of the SWAG item: "))

# Ask the user to enter the purchase price (before tax) of each SWAG Item and store this value as a float. 
Price = float ( input ("Enter the purchase price of each SWAG Item before tax: $"))

#Ask the user to enter the total amount of money raised and store this value as a float.
total = float( input ("Enter the total amount of money budgeted: $"))
print("\n")
# Declare a float variable called HST_RATE and assign it the value 0.13 (13%). 
HST_RATE = 0.13
# Calculate the purchase price of each SWAG Item WITH tax and save this to a variable of type float.
HST_RATE = Price * 1.13
HST_RATE = round(HST_RATE,2)
# Calculate the number of SWAG Items that can be purchased by dividing the total amount of money budgeted
# by the price of each SWAG Item (with tax).
Number_Of_Items = int(total / HST_RATE)
# Calculate the total price of all SWAG Items by multiplying the number of Items by the price with tax for each.
Total_Price = float(Number_Of_Items * HST_RATE)
# Calculate the leftover money after the purchase of the SWAG Items
Left_Money = float(total - Total_Price)
Left_Money = round(Left_Money,2)
print("With the total funds budgeted of $",str(total)," the company can buy ",str(Number_Of_Items)," Pens at $",str(HST_RATE)," each (including 13% HST) for a total of $",str(Total_Price),". There would still be $",str(Left_Money)," leftover.",sep ="")





