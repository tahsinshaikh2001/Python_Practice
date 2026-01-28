# List of numbers
nums = [1, 2, 2, 3, 1]

# Empty dictionary to store frequency of each number
freq = {}

# Loop through each number in the list
for n in nums:
    # If number already exists in dictionary
    if n in freq:
        freq[n] += 1   # increase its count by 1
    else:
        freq[n] = 1    # first time seeing this number, set count to 1

# Print the frequency dictionary
print(freq)
