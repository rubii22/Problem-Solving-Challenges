# 🔹 Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.

def reverse_string(s: str) -> str:
    return s[::-1]  # Return the reversed string

# Test the function
input_string = "Artificial Intelligence is the future of technology!"
output_string = reverse_string(input_string)

print("Original String:", input_string)
print("Reversed String:", output_string)



# # 🔹 Problem 2: Count Vowels in a String
# Write a function that takes a string as input and returns the reversed string.

def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
    count = 0  # Initialize count to 0
    
    for char in s.lower():  # Convert the string to lowercase and iterate through each character
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment the count if it is a vowel
    
    return count  # Return the total count of vowels

# # Testing the function with different inputs

print(count_vowels("Apple"))  # Output: 2
print(count_vowels("Artificial Intelligence"))  # Output: 10
print(count_vowels("PYTHON"))  # Output: 1
print(count_vowels("Hello World"))  # Output: 3


# 🔹 Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns 
# the sum of its digits.

# ✅ Approach 1: Using String Conversion

def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n)) # Convert number to 
# string, iterate, and sum up digits.

# Testing the function
print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(56789))  # Output: 35
print(sum_of_digits(0))  # Output: 0
print(sum_of_digits(99999))  # Output: 45

# ✅ Approach 2: Using Modulus & Division

def sum_of_digits(n: int) -> int:
    total = 0  # Initialize sum to 0
    while n > 0:  # Loop until the number becomes 0
        total += n % 10  # Extract the last digit and add to sum
        n //= 10  # Remove the last digit
    return total  # Return the final sum

# Testing the function
print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(56789))  # Output: 35
print(sum_of_digits(0))  # Output: 0
print(sum_of_digits(99999))  # Output: 45

