# Initialize counter for vowels
count = 0

# Take input from user and convert to lowercase
m = input("Enter a string: ").lower()

# Loop through each character in the string
for i in m:
    # Check if the character is a vowel
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1   # Increment counter if vowel found

# Print the total number of vowels
print(f"Vowels in {m} are", count)



Explaination:


count = 0 → Initialize a counter for vowels.

m = input(...).lower() → Read string from user and convert to lowercase so comparison is easy.

for i in m: → Loop through each character in the string.

if i == "a" or ... or i == "u": → Check if the character is a vowel.

count += 1 → Increment the vowel counter.

print(...) → Display total number of vowels.