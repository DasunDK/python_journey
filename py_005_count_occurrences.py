"""
------------------------------------------------------------
Python Journey - PY-005
Challenge: Count Occurrences of a Number

Objective:
    Count how many times a specific number appears in a list.

Rules:
    - Use a function
    - Use a loop
    - Use conditional statements
    - Do not use .count()
    - Do not use advanced libraries

Skills Practiced:
    - Lists
    - Loops
    - Conditional logic
    - Counters
    - Functions
    - Algorithmic thinking

Difficulty:
    🥉 Bronze

Author:
    Dasun
------------------------------------------------------------
"""


def count_occurrences(numbers, target):
    # TODO:
    # Create a variable to keep track of how many times
    # the target number appears.
    count = 0
    # Hint:
    # Start the counter at 0.
    
    
    # TODO:
    # Loop through every number in the list.
    for  num in numbers:
        if target == num:
            count += 1
    # Ask yourself:
    # "How can I check each number one by one?"
    
    
    # TODO:
    # Inside the loop, check whether the current number
    # is equal to the target number.
    #
    # If they are equal, increase your counter by 1.
    
    
    # TODO:
    # After the loop finishes, return the counter.
    return count
    

if __name__ == "__main__":
    # Example list of numbers
    numbers = [2, 5, 2, 8, 2, 9, 5]

    # The number we want to count
    target = 2

    # Call your function and store the result
    result = count_occurrences(numbers, target)

    # Display the result
    print(f"The number {target} appears {result} times.")