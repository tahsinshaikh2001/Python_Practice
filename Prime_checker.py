# Take input number from the user
n = int(input("Enter a number: "))

# Numbers less than 2 are not prime
if n < 2:
    print(n, "is not prime")
else:
    # Assume number is prime initially
    flag = True

    # Check divisibility from 2 up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:   # If n is divisibl
