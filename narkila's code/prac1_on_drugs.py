
user_input = input("Enter a math problem: ")

parts = user_input.split()

print(len(parts))
for i in range(len(parts)):
    print(f"{parts[i]}")


if len(parts) != 3:
    print("Invalid input. The input should have exactly three parts.")
else:
    operand1 = float(parts[0])
    operator = parts[1]
    operand2 = float(parts[2])
    
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            print("Error: Division by zero is not allowed.")
            exit()
        result = operand1 / operand2
    else:
        print("Invalid operator. Supported operators are +, -, *, /.")
        exit()
    

    print(f"The result of {operand1} {operator} {operand2} is: {result}")