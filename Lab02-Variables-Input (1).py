#Step 1
print("The square root of 25 is",25**0.5)

#Step 2
print("Decimal 113 in Binary is:",bin(113))

#Step 3
print("The number 3 divides into 7:\n", 7//3,"times with a remainder of",7%3)

#Step 4
print("The other day in Canada it was -15 degrees in Celsius, to an American that would be", (-15*9/5)+32, "degrees in Fahrenheit.")

#Step 5
PI = 3.14159
RAD = 3
AREA = PI * RAD ** 2
print("A circle with a radius of", RAD, "units will cover an area of", AREA, "units squared.")

#Step 6
INVEST = 10000
RATE = 5
TIME = 5
print("With an investment of", INVEST, "at an interest rate of", RATE, "% for", TIME, "units of time.")
print("Simple Interest would be", (INVEST * RATE * TIME) / 100)

#Step 7
INVEST = 10000
RATE = 5
TIME = 5
print("With an investment of", INVEST, "at an interest rate of", RATE, "% for", TIME, "units of time.")
print("Compound Interest would be", int(INVEST * (1 + RATE / 100) ** TIME))

#Step 8
DEC = int(input("Please enter an integer: "))
print("The number", DEC, "in Binary would be", bin(DEC))

#Step 9
B_VALUE = int(input("Please enter a Binary value: "),2)
print("The binary number", bin(B_VALUE), "in Deciaml would be", B_VALUE)

#Step 10
print("Home Brew Bottling Program\n")
print("This program will calculate the number of bottles required to bottle a batch of home brew.\n")
ML_PER_L = 1000
liters = float(input("Enter the total amount of home brew in L: "))
bottle = float(input("Enter the bottle size in millilitres: "))
label = input("Enter a description for your home brew: ")
totalml = liters * ML_PER_L
print("\nYou will need ", int(totalml // bottle), " bottles for your batch of ", label, ".", sep="")
print("There will be", int(totalml % bottle), "ml of", label, "left over, unbottled")




