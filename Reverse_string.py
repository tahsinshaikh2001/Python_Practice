# Take input string from the user
n = input("Enter a string: ")

# Initialize an empty string to store the reversed string
rev = ""

# Loop through each character in the original string
for ch in n:
    rev = ch + rev  # Prepend the character to 'rev' to reverse the order

# Print the reversed string
print(rev)
