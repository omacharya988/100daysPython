#  FILE:      lAB05_FUNCTION-TtUPLES_DICT.PY
#  FUNCTION:  LAB 4 INFO 1249 Solution
#  DATE:      WEEK 8, W2022
#  ----------------------------------------------------
# Step 1
def withTax(beforeTax):
    return round(beforeTax * 1.13,2)

userInput = float(input("Please enter the price before tax: "))
print("If you purchased",round(userInput,2),"worth of")
print("electronics, the total would be $ ", withTax(userInput))
print("after 13% sales tax.")

#Step 2
def cTof(Celsius):
    return (Celsius * 9/5) + 32

userInput = float(input("Enter a temperature in Celsius: "))
print(userInput, "Celsius equals", cTof(userInput), "Fahrenheit.")

#Step 3
def sInt(investment, rate, time):
    return round(((investment * rate * time) / 100),2)

userInvest = float(input("Please enter your investment: "))
userRate = float(input("What is the interest rate / year in %: "))
userYears = float(input("How many years will it be invested: "))

interest = sInt(userInvest, userRate, userYears)
print("Simple Interest would be", interest)
print("Balance after", userYears, "years will be", userInvest + interest)

#Step 4
def cInt(investment, rate, time):
    balance = investment*(1+rate /100)**time
    return round(balance-investment,2)

userInvest = float(input("Please enter your investment: "))
userRate = float(input("What is the interest rate / year in %: "))
userYears = float(input("How many years will it be invested: "))

interest = cInt(userInvest, userRate, userYears)
print("Compound Interest would be", interest)
print("Balance after", userYears, "years will be", userInvest + interest)

#Step 5
def cPrice(cAge):
    if cAge <= 2:
        return 0.0
    elif cAge <= 13:
        return 7.99
    elif cAge >= 65:
        return 9.99
    else:
        return 12.99

userInput = int(input("What is the customer's age: "))
print("If the customer is ", userInput,
      " the tickets cost $", cPrice(userInput), sep="")

#Step 6
def isPrime(n):
    if n > 1:
        for i in range(2, n//2):  
            if (n % i) == 0: return False
        else: 
            return True
    else:
        return False

userStart = int(input("Please enter a Starting Integer: "))
userEnd = int(input("Please enter a Ending Integer: "))
for x in range(userStart, userEnd+1):
    if isPrime(x): print(x)

#Step 7
def isPalindrome(word):
    rev = ""
    for char in word:    # Rotor
        rev = char + rev # Appending to the front of the string.
    if word.lower() == rev.lower(): # Any string variable has .lower() methods.
       #Rotor -> rotor == rotoR -> rotor    
        return True
    else:
        return False

userInput = input("Please enter a word: ")
print(isPalindrome(userInput))

#Step 8
def ipList(strInput):
    tmpList = strInput.split("/")
    rtnList = tmpList[0].split(".")
    rtnList.append(tmpList[1])
    return rtnList

userInput = input("IPv4 Address and prefix: ")
print("as a List:",ipList(userInput))

# Step 9 - Challenge
#Functions go here. 
# Function calculates average  
def mAvg(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 
  
# Function calculates total average 
def sAvg(student): 
    projects = mAvg(student["projects"]) 
    tests = mAvg(student["tests"]) 
      
    return (round(0.3 * projects + 0.7 * tests,2) ) 
  
# Function to calculate the total 
# average marks of the whole class 
def cAvg(student_list): 
    result_list = [] 
  
    for student in student_list: 
        stud_avg = sAvg(student) 
        result_list.append(stud_avg) 
    return mAvg(result_list) 
  
  
classlist = [] # An empty list that contains Dictionaries which contain lists.
 
# 1. Jack's dictionary entry.
classlist.append ( {	"name" : "Jack Frost", 
         		"projects" : [80, 50, 40, 20], 
	         	"tests" : [75, 82] } )
         
# 2. James's dictionary entry.
classlist.append ( {	"name":"James Potter", 
          		"projects" : [82, 56, 44, 30], 
          		"tests" : [80, 88] } )
  
# 3. Dylan's dictionary entry.
classlist.append ( {	"name" : "Dylan Rhodes", 
          		"projects" : [77, 82, 23, 39], 
         		"tests" : [78, 77] } )
          
# 4. Jessica's dictionary entry.
classlist.append ( {	"name" : "Jessica Stone", 
		         "projects" : [67, 55, 77, 21], 
		         "tests" : [40, 50] } )
         
# 5. Tom's dictionary entry.
classlist.append ( {	"name" : "Tom Hanks", 
		        "projects" : [29, 89, 60, 56], 
		        "tests" : [65, 56] } )

# Main Program Starts here.
# Iterate through the students list 
# and calculate their respective 
# average marks and letter grade

for i in classlist: 
    print(i["name"]) 
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks of %s is : %s \n" %(i["name"],sAvg(i))) 

# Calculate the average of whole class 
class_av = cAvg(classlist) 
  
print( "Class Average is %s" %(class_av)) 

