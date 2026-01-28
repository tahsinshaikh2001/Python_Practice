# Take multiple numbers as input and convert them to a list of integers
nums = list(map(int, input("Enter number: ").split()))

# Initialize variables for largest and second largest
largest = second = float('-inf')  # -inf ensures any number will be larger initially

# Loop through each number in the list
for n in nums:
    # If current number is greater than largest
    if n > largest:
        second = largest   # previous largest becomes second largest
        largest = n       # update largest to current number
    # If current number is greater than second but not equal to largest
    elif n > second and n != largest:
        second = n        # update second largest

# Print the second largest number
print("Second largest:", second)
