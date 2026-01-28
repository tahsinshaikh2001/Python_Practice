# Initialize an empty list to store unique elements
o = []

# Original list with possible duplicates
n = [1, 2, 3, 4, 4]

# Loop through each element in the original list
for i in n:
    # If element is not already in the unique list, add it
    if i not in o:
        o.append(i)

# Print the list with duplicates removed
print(o)
