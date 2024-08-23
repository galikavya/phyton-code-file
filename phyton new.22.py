def calculate_tax(income):
    if income < 150000:
        tax = 0
    elif 150000 < income <= 300000:
        tax = (income - 150000) * 0.10
    elif 300000 < income <= 500000:
        tax = (150000 * 0.10) + (income - 300000) * 0.20
    else:
        tax = (150000 * 0.10) + (200000 * 0.20) + (income - 500000) * 0.30
    return tax

income = float(input("Enter your taxable income: ₹"))
tax = calculate_tax(income)
print(f"The tax on an income of ₹{income} is: ₹{tax:.2f}")
