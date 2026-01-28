# Take input from user: how many Fibonacci numbers to print
n = int(input("Enter a no. : "))

# Initialize first two Fibonacci numbers
a = 0
b = 1

# Print the first two numbers
print(a, b, end=" ")  # end=" " keeps the numbers on the same line

# Loop from 2 to n-1 to calculate the rest of the Fibonacci sequence
for i in range(2, n):
    d = a + b   # Next Fibonacci number is sum of previous two
    a = b       # Update a to the previous number b
    b = d       # Update b to the newly calculated number d
    print(d, end=" ")  # Print the next Fibonacci number




n = int(input(...)) → Read how many numbers to print.

a = 0, b = 1 → Starting numbers of Fibonacci series.

print(a, b, end=" ") → Print first two numbers on the same line.

for i in range(2, n): → Loop to calculate remaining numbers.

d = a + b → Next Fibonacci number.

a = b → Move b to a (shift previous numbers).

b = d → New number becomes b for next iteration.

print(d, end=" ") → Print current Fibonacci number.
