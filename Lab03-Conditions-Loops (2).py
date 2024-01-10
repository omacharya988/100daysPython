#Step 1
name1= input("Enter First name: ") 
name2= input("Enter Second name: ") 
print("Here are your names in alphabetical order.")
if name1 < name2:
    print(name1,name2,sep="\n")
else:
    print(name2,name1,sep="\n")

#Step 2
age = int(input("What is the customer's age: "))
if age <= 2:
    price = 0.0
elif age <= 13:
    price = 7.99
elif age >= 65:
    price = 9.99
else:
    price = 12.99
    
if price != 0.0:
    print("If the customer is ", age, " the tickets cost $", price, sep = "")
else:
    print("You're too young to purchase Tickets.")

#Step 3
numb = float(input("Please enter a number: "))
numb = int(round(numb,0))
if numb == 0:
    print("Your number is a zero")
elif numb > 0:
    print("Your number",numb, "is a positive number.")
else:
    print("Your number",numb, "is a negative number.")

#Step 4
start_num = float(input("Please Enter a Starting number: "))
start_num = int(round(start_num,0))

if start_num <= 0:
    print("Please enter a positive number.")
else:
    print("Counting down from", start_num, "to zero.")
    for i in range(start_num, 0, -1):
        print(i,", ",end="")
    print("0.")

#Step 5
word = input("Please Enter a Word: ")
count = 0
for char in word:
  if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'Y':
      count += 1
print("There are ", count, " vowels in the word \"", word, "\".", sep ="")

#Step 6
item = 0
total = 0
count = 0
print("Enter -1 to Finish Your List.")
while item != -1:
    item = float(input("Please enter the items price: "))
    if item == -1: break
    total += item
    count += 1
print("You entered ", count, " items for a total bill of $", round(total,2), ". \nYour average item price was $", round(total/count,2),".", sep="")

#Step 7
dec = int(input("Please enter a Decimal value: "))
result = "" 
num = dec
while num != 0:
    remainder = num % 2 # gives the exact remainder
    num //= 2
    result = str(remainder) + result
print("The binary representation of", dec, "is", result)

#Step 8
binary = input("Please enter a Binary value: ")
result = 0
count = len(binary)-1
for bit in binary:
    result += int(bit)*2**count
    count -= 1
    
print("The Decimal representation of", binary, "is", result)

#Step 9
start = int(input("Please enter the First Number in the Range: "))
end = int(input("Please enter the Last Number in the Range: "))
print("")
for i in range(start,end+1):
    print(i, "is", end=" ")
    if i % 2 == 0:
        print("even", end="")
    else:
        print("odd", end="")
    div_by_3 =False
    if i%3 == 0:
        print(" and is divisable by 3", end="")
        div_by_3 = True
        
    if i%4 == 0:
        if div_by_3:
            print(" and by 4", end= "")
        else:
            print(" and is divisable by 4", end="")    
    print(".",end="\n")

    
