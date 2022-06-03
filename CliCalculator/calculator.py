from calc_art import ascci

def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def division(x, y):
    return x / y

def muliplication(x, y):
    return x * y


operations = {
"+" : add, 
"-": subtraction,
"/": division,
"*": muliplication
}

print(ascci)

def calculator():
    n1 = float(input("choose a number "))

    for symbols in operations:
        print(symbols)

    again = True
    while again:
            function = input("choose one of the operation above ")

            n2 = float(input("next number "))

            calculation_function = operations[function]
            answer = calculation_function(n1, n2)

            print(f"{n1} {function} {n2} = {answer}\n")

            loop = input(f"continue calculating with {answer}? [y] / [n] ") 
            if loop == "y":
                n1 = answer
            else:
                again = False
                calculator()
            
calculator()