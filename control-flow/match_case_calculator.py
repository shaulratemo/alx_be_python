num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is {addition}.")
    case "-":
        subtraction = num1 - num2
        print(f"The result is {subtraction}.")
    case "*":
        product = num1 * num2
        print(f"The result is {product}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1 / num2
            print(f"The result is {division}.")
    case _:
        print(f"Invalid operation {operation}.")