"""
------------------------------------------------------------
Python Journey - PY-001
Challenge: Reverse Characters

Objective:
    Reverse a string entered by the user without using
    Python shortcuts like [::-1] or reversed().

Rules:
    - Use variables
    - Use a loop
    - Do not use built-in reverse shortcuts

Skills Practiced:
    - User input
    - Loops
    - String manipulation
    - Logical thinking

Difficulty:
    🥉 Bronze

Author:
    Dasun

Date:
    2026-07-17
------------------------------------------------------------
"""

def reverse_string(user_input):
    reversed_string = ""
    for i in range(len(user_input) -1, -1, -1):
        reversed_string += user_input[i]
    return reversed_string

if __name__ == "__main__":
    result = reverse_string(input("Enter a string to reverse: "))
    print("Reversed string:", result)
