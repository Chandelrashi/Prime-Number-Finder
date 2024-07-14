def is_prime(num):
    # Function to check if a number is prime or not
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_number_between(start, end):
    # Function to find prime numbers between two numbers
    # Check if the inputs are valid
    if not (isinstance(start, int) and isinstance(end, int) and start > 0 and end > 0):
        return []

    # Swap the numbers if start > end
    if start > end:
        start, end = end, start

    # Find the prime numbers between start and end (inclusive)
    prime_list = []
    for num in range(start, end+1):
        if is_prime(num):
            prime_list.append(num)

    return prime_list

# Get input from the user
def main():
    try:
        num1 = int(input("Enter the first positive integer: "))
        num2 = int(input("Enter the second positive integer: "))
        
        # Check if the inputs are valid positive integers
        if num1 <= 0 or num2 <= 0:
            print("Invalid input. Please enter positive integers only.")
            return

        # Find the prime numbers
        prime_list = prime_number_between(num1, num2)

        # Output the prime numbers
        if prime_list:
            print(f"The prime numbers between {num1} and {num2} are:")
            for i, prime in enumerate(prime_list, 1):
                print(prime, end=" ")
                if i % 10 == 0:
                    print()
        else:
            print("No prime numbers found in the given range.")

    except ValueError:
        print("Invalid input. Please enter positive integers only.")

# Execute the main function if the script is run as the main program
if __name__ == "__main__":
    main()
