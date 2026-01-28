# Take input from the user (string input)
n = input("Enter here: ")

# Create an empty dictionary to store character frequency
f = {}

# Loop through each character in the input string
for i in n:
    # If character already exists in dictionary
    if i in f:
        f[i] += 1    # increase its count
    else:
        f[i] = 1     # first occurrence, set count to 1

# Print the frequency of each character
print(f)
