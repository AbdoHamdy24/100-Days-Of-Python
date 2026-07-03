# Prime number checker
def prime_checker(number):
    is_prime = True
    for div in range(2,number):
        if number % div ==0 :
            is_prime = False
    if is_prime:
        print("Prime Number!")
    else:
        print("Not Prime Number!")    
        

n = int(input("Check this number: "))
prime_checker(number=n)