# Calculator

# Adding
def add(n1, n2):
    return n1 + n2

# Subtracting
def subtract(n1, n2):
    return n1 - n2

# Multipling
def multiply(n1, n2):
    return n1 * n2

# Dividing
def divide(n1, n2):
    return n1 / n2

def calculator():
    num1 = float(input("The first number = "))

    operations = {  "+" : add,
                    "-" : subtract,
                    "*" : multiply,
                    "/" : divide}

    for symbol in operations :
        print(symbol)

    cont = True

    while cont :
        
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("The next number = "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\n")
        if continue_operation == "y":
            num1 = answer
        else:
            cont = False
            print(f"The final answer = {answer}")
            print("#" * 40)
            calculator()
    

calculator()