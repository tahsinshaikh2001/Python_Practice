# Initialize variable to store the reversed number
rev = 0

# Take input number from the user
n = int(input("Enter a number: "))

# Store the original number for later display
org = n

# Loop until all digits are processed
while n > 0:
    d = n % 10          # Get the last digit of n
    rev = rev * 10 + d  # Add last digit to the reversed number
    n //= 10            # Remove last digit from n

# Print original and reversed number
print(f"Original number: {org}, Reversed: {rev}")
