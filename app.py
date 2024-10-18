'''# Challenge 1'''
'''x = 6
y = 9
if x % 2 == 0 and y % 2 == 0:
    print("both are even")
elif x % 2 == 0 or 2 == 0:
    print("one is even")
elif y % 2 == 0 or 2 == 0:
    print("one is even")
else:
    print("both are odd")'''
'''# Challenge 2''' 

'''service = input("service")
if service == "bad":
    print("0%")
elif service == "okay":
    print("15%")
elif service == "good":
    print("20%")
else:
    print("25%")'''
 
""" # Challenge 3
a = 45
for i in range(2, a + 1):
    if a % i == 0:
        print(i) """

#Challenge 4

# get 2 numbers

#find smaller number

#loop to smaller number +1

# check if i is a factor of BOTH numbers
""" 
a = 10
b = 25
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        print(i) """

#Mad Libs Project Part

verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
celebrityguest = input("Enter a celebrity: ")
num = input("Enter a number: ")
pluralnoun = input("Enter a plural noun: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")

madlib = f"I was {verb1} {noun1} with {celebrityguest} when {num} {pluralnoun} shot out from the {noun2} and {verb2} my face."
print(madlib)
