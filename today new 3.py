def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_composite():
    """Count prime and composite numbers from user input."""
    prime_count = 0
    composite_count = 0

    numbers = input("Enter numbers separated by spaces: ")
    number_list = map(int, numbers.split())

    for number in number_list:
        if is_prime(number):
            prime_count += 1
        elif number > 1:
            composite_count += 1

    print(f"Total Prime Numbers: {prime_count}")
    print(f"Total Composite Numbers: {composite_count}")


count_prime_composite()
