# Pizza Order
print("Welcome to Python Pizza Deliveries!")

print("#" * 40)
print("Small Pizza: 15$")
print("Medium Pizza: 20$")
print("Large Pizza: 25$")
print("Perreroni for Small Pizza: + 2$")
print("Perreroni for Medium Pizza: + 3$")
print("Extra cheese for any size Pizza: + 1$")
print("#" * 40)

size = input("What size Pizza do you want? S , M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
    
elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
    
elif size == "L":
    price = 25 
    if add_pepperoni == "Y":
        price += 3
else:
    print("Invalid Size!")

if extra_cheese == "Y":
        price += 1
print(f"Your final bill: {price}$")