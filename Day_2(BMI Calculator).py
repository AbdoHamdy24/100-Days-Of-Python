height = input("Enter your height in m :")
weight = input("Enter your weight in kg :")

BMI = float(weight) / (float(height) ** 2)          # Calculate the Body Mass Index
print("The Result of your BMI = " + str(BMI))       # Print the result

if BMI <= 18.5 :
    
    underweight = 22 - BMI
    targetweight = float(underweight) * (float(height) ** 2)        # Weight you need to gain.
    print("You are Underweightted")
    print(" You need to gain weight " + str(targetweight) + " kg. ") 

elif BMI  > 18.5 and BMI < 25 :
    print("Perfect, You are Healthy Weight.")

else:
    
    overweight = BMI - 22
    targetweight2 = float(overweight) * float(height) ** 2          # Weight you need to lose.
    print("You are Overweightted.")
    print("You need to lose weight " + str(targetweight2) + " kg. ")
