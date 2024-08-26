def calculate_pow(x, n):
    return x ** n

def calculate_add(x, n):
    return x + n

def calculate_sub(x, n):
    return x - n

def calculate_mul(x, n):
    return x * n

def calculate_div(x, n):
    if n != 0:
        return x / n
    else:
        return "Division by zero is not allowed!"

def main():
    print("Choose the operation:")
    print("1. Power (x^n)")
    print("2. Addition (x + n)")
    print("3. Subtraction (x - n)")
    print("4. Multiplication (x * n)")
    print("5. Division (x / n)")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    x = float(input("Enter the value of x: "))
    n = float(input("Enter the value of n: "))
    
    if choice == '1':
        print(f"{x} raised to the power of {n} is {calculate_pow(x, n)}")
    elif choice == '2':
        print(f"The sum of {x} and {n} is {calculate_add(x, n)}")
    elif choice == '3':
        print(f"The difference between {x} and {n} is {calculate_sub(x, n)}")
    elif choice == '4':
        print(f"The product of {x} and {n} is {calculate_mul(x, n)}")
    elif choice == '5':
        print(f"The division of {x} by {n} is {calculate_div(x, n)}")
    else:
        print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
