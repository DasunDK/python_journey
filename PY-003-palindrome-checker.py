"""
------------------------------------------------------------
Python Journey - PY-003
Challenge: Palindrome Checker

Objective:
    Determine whether a user-entered word is a palindrome
    without using Python's reverse shortcuts.

Rules:
    - Use variables
    - Use loops
    - Return True or False from a function
    - Do not use [::-1] or reversed()

Skills Practiced:
    - Functions
    - String comparison
    - Loops
    - Conditional statements
    - Logical thinking

Difficulty:
    🥉 Bronze

Author:
    Dasun
------------------------------------------------------------
"""

def reverse_string(user_input):
    reversed_string = ""
    
    for i in range(len(user_input) -1, -1, -1):
        reversed_string += user_input[i]
       
    return reversed_string
        
def check_palindrome(user_input):
    reversed_string = reverse_string(user_input)
    
    if reversed_string == user_input:
        return "This is a palindrome word"
    else:
        return "This is not a palindrome word!"

if __name__ == "__main__":
    user_input = str(input("Enter a word to check palindrome: ")).casefold()
    print(user_input)
    result = check_palindrome(user_input)
    print (result)