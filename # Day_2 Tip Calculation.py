# Tip Calculation
print("Welcome to the tip calculator")
bill = float(input("What was the totqal bill? "))
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_bill = float(bill) * (1 + float(tip) / 100) / int(people)
print(f"Each person should pay: {round(total_bill,2)}$")
