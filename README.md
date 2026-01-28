# Armstrong Number Program in Python

This program checks whether a given number is an **Armstrong number** or not.

---

## What is an Armstrong Number?

An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of the cubes of its digits.  

**Example:**  
- `153` → 1³ + 5³ + 3³ = 153 ✅ Armstrong number  
- `123` → 1³ + 2³ + 3³ = 36 ❌ Not an Armstrong number  

---

## Python Code

```python
n = int(input("Enter a number : "))

rev = 0
org = n
while n > 0:
    d = n % 10
    rev = rev + d**3
    n = n // 10

if org == rev:
    print("Armstrong")
else:
    print("Not an Armstrong")



**How It Works**

1)Take input number n and store original in org.

2)Initialize rev = 0 to keep sum of cubes of digits.

3)Loop through each digit:

d = n % 10 → get last digit

rev = rev + d**3 → add cube of digit to sum

n = n // 10 → remove last digit

4)Compare rev with original number org:

If equal → print "Armstrong"

Else → print "Not an Armstrong"
