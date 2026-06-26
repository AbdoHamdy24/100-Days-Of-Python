# Leap Year Checker
year = int(input("Which year you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:   
            print("Leap Year!")
        else:
            print("Not Leap Year!")
    else:
        print("Leap Year!")
else:
    print("Not Leap Year!")