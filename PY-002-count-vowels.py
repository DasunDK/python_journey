"""
------------------------------------------------------------
Python Journey - PY-002
Challenge: Count Vowels in a String

Objective:
    Count the number of vowels in a user-entered string.

Rules:
    - Use variables
    - Use a loop
    - Use conditional statements
    - Avoid advanced libraries

Skills Practiced:
    - String traversal
    - Conditional logic
    - Counting
    - Problem solving

Difficulty:
    🥉 Bronze

Author:
    Dasun

------------------------------------------------------------
"""

def count_vowels(user_input):
    vowels = "aeiou"
    count = 0
    for char in user_input.lower():
        if char in vowels:
            count += 1
    return count 

if __name__ == "__main__":
    result = count_vowels(input("Enter a string to count vowels: "))
    print("Number of vowels:", result)