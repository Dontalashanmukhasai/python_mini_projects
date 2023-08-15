def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("enter your first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
   
    while should_continue:
       operation_symbol = input("pick an operation:")
       num2 = float(input("enter the next number?: "))
       calculator_function = operations[operation_symbol]
       answer = calculator_function(num1,num2)

       print(f"{num1} {operation_symbol} {num2} = {answer}")
       if input(f"Type 'yes' to continue with the {answer} or Type 'no' to restart the calculation:" ) == "yes":
           num1 = answer
       else:
           should_continue = False
           calculator()
calculator()
