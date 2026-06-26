# The love calculator
print("#" * 31)
print("Welcome to the love calculator!")
print("#" * 31)

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()

fullname = lower_name1 + lower_name2

T = fullname.count("t")
R = fullname.count("r")
U = fullname.count("u")
E = fullname.count("e")

L = fullname.count("l")
O = fullname.count("o")
V = fullname.count("v")
E = fullname.count("e")

letter1 = T + R + U + E
letter2 = L + O + V + E

score = int(str(letter1) + str(letter2))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score < 50) or (score > 40):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")    
