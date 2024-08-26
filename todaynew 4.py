def calculator():
    
    x = float(input("Enter the base number (x): "))
    n = float(input("Enter the exponent or second number (n): "))
    
    
    print("\nChoose an operation:")
    print("1. Power (x^n)")
    print("2. Addition (x + n)")
    print("3. Subtraction (x - n)")
    print("4. Multiplication (x * n)")
    print("5. Division (x / n)")
    
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    
    if choice == '1':
        result = pow(x, n)
        operation = "Power"
    elif choice == '2':
        result = x + n
        operation = "Addition"
    elif choice == '3':
        result = x - n
        operation = "Subtraction"
    elif choice == '4':
        result = x * n
        operation = "Multiplication"
    elif choice == '5':
        if n != 0:
            result = x / n
            operation = "Division"
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid choice! Please select a valid operation."
    
    return {operation} {x} and {n} is: {result}
print(calculator())
