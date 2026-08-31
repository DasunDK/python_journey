"""
------------------------------------------------------------
Python Journey - PY-006
Challenge: Find the Position of a Number

Objective:
    Find the position (index) of a target number inside
    a list.

Rules:
    - Use a function
    - Use a loop
    - Use conditional statements
    - Do not use .index()
    - Do not use advanced libraries
    - Return the position of the first matching number

Skills Practiced:
    - Lists
    - Indexes
    - Loops
    - Conditional logic
    - Functions
    - Algorithmic thinking

Difficulty:
    🥉 Bronze

Author:
    Dasun
------------------------------------------------------------
"""


def find_position(numbers, target):
    position = -1
    
    for i in range(len(numbers)):
        if target == numbers[i]:
            position = i
            return position
            
    return position
    # TODO:
    # We need to keep track of the position (index)
    # while going through the list.
    #
    # Remember:
    # Python list indexes start from 0.
    #
    # Example:
    # numbers = [10, 20, 30, 40]
    #
    # index:
    #   0    1    2    3
    #
    # So the position of 30 is 2.


    # TODO:
    # Create a loop that gives you access to BOTH:
    #
    #   1. The index
    #   2. The number
    #
    # Hint:
    # Think about using range() and len().


    # TODO:
    # Inside the loop, compare the current number
    # with the target.
    #
    # If they are equal:
    #     return the current index
    #
    # We only want the FIRST occurrence.


    # TODO:
    # What should the function return if the target
    # does not exist in the list?
    #
    # Hint:
    # You need a value that means:
    # "Not found."


    


if __name__ == "__main__":
    # Example list
    numbers = [15, 42, 8, 23, 42, 91]

    # Number we want to find
    target = 23

    # Call the function
    result = find_position(numbers, target)

    # Display the result
    if result != -1:
        print(f"The number {target} was found at index {result}.")
    else:
        print(f"The number {target} was not found.")