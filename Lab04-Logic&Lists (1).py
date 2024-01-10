#Step 1
start = int(input("Please enter a Starting Integer: "))
end = int(input("Please enter an Ending Integer: "))
for x in range(start,end+1):    # 10 to 25
    if x > 1: 
        for y in range(2, x):   # range (2, 12) = 2 to 11
            if (x % y) == 0:    # 12 / 2 R 0 = True 
                break
        else: 
            print(x)  

#Step 2
num = int(input("Please enter a number: "))
if num > 1:                     #23
   for i in range(2, num//2):   #2 to 11-1(10)
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
else: 
   print(num, "is not a prime number")

#Step 3
word = input("Please enter a word: ")
rev = ""
for char in word:   # Rotor
    rev = char + rev # Appending to the front of the string.
    # rotoR (rev)
if word.lower() == rev.lower(): # Any string variable has .lower() methods.
   #Rotor -> rotor == rotoR -> rotor    
    print(word,"is a Palindrome.")
else:
    print(word,"is not a Palindrome.")

#Step 4
bStr = input("Please enter a Binary Number: ") #1101
bList = [] #empty list
for char in bStr: #Loop through each char in the string "1101"
    bList.append(char) #1st Loop = bList.append("1")
print(bStr,"as a Python List\n", bList)

#Step 5
addy = input("IPv4 Address: ")  # "205.210.49.62"
octets = []                     # New Empty List
temp = ""                       # Empty String
for char in addy:       # Each charater in the input string (above)
    if char != ".":     # 13th loop char = "2"
        temp += char    # temp ("6") = "6" + "2" = "62" (temp)
    else:
        octets.append(int(temp)) # When you hit a "." append int to list
        temp = ""
else:
    octets.append(int(temp))
    temp = ""
print("as a list:", octets)

#Step 6
Powersof2 = []
dec, index = 0, 0
for i in range(8):              # 0 to 7
    Powersof2.insert(0,2**i)    # 2^3(i) = 8  Powersof2 = [8, 4, 2, 1]
binary = input("Please enter a Binary Number: ") #11100111
for i in binary: #Loop through each character in the string. 
    dec += int(i)*Powersof2[index]
    index +=1
print(dec)

#Step 7
cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
print(cards)
num = int(input("Number of cards for this cut: "))
if num > len(cards): print("Number needs to be between 1 and", len(cards))
else:
    newCards = cards[num:] + cards[:num]
    print("Your cards cut at card", num, "would look like this:\n", newCards)

#Step 8
time24 = input("Please enter a time in 24 hour format (hh:mm): ") #21:21
if int(time24[0:2]) > 12: #Slice of index 0 to 1 (First 2 chars)
    time12 = str(int(time24[0:2]) - 12)
    time12 = time12 + time24[2:] + " PM"
elif int(time24[0:2]) == 12: time12 = time24 + " PM"
else: time12 = time24 + " AM"
print(time12)

#Step 9
colours = [ ["Yellow",3], ["Violet",6], ["Red",1], ["Blue",5], ["Orange",2], ["Green",4] ]
print(colours)
swapped = True			              # TRUE to enter the while loop
while swapped:
    swapped = False 		              # No swaps so far
    for i in range(len(colours)-1):	      # We need (6 - 1) comparisons
        if colours[i][1] > colours[i + 1][1]: # compare adjacent elements
            swapped = True
            colours[i], colours[i + 1] = colours[i + 1], colours[i]
# After first pass colours = [ ["Yellow",3], ["Red",1], ["Blue",5], ["Orange",2], ["Green",4], ["Violet",6] ]
# After second pass colours = [ ["Red",1], ["Yellow",3], ["Orange",2], ["Green",4], ["Blue",5], ["Violet",6] ]
# After third pass colours = [ ["Red",1], ["Orange",2], ["Yellow",3], ["Green",4], ["Blue",5], ["Violet",6] ]
# On the forth pass (NO SWAPS) Exit Loop (while swapped:)
print(colours)

#Step 10
valid = [ "0", "1" ]
lBinary = list(input("Please enter a Binary # ")) # list("a10") --> [ "1", "0" ]
# For loop List is = [ "a", "1", "0" ]
for element in lBinary[:]: # [:] means a slice of the entire list (copy)
    if element not in valid:
        lBinary.remove(element) 
print("".join(lBinary))























