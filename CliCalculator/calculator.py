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