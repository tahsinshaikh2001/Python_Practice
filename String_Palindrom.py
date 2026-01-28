# Take string input from the user and convert it to lowercase
# (so comparison is case-insensitive)
n = input("enter a string: ").lower()

# Store the original string
org = n

# Reverse the string using slicing
rev = n[::-1]

# Compare original string with reversed string
if org == rev:
    print("Palindrome")      # same forwards and backwards
else:
    print("Not Palindrome")  # different when reversed
