"""
------------------------------------------------------------
Python Journey - PY-013
Challenge: Find Common Elements Between Two Lists

Objective:
    Find numbers that appear in both lists.

Rules:
    - Use a function
    - Use loops
    - Create a new result list
    - Do not use set()
    - Do not use intersection()
    - Do not use list comprehensions
    - Do not use external libraries
    - Preserve the order from the first list
    - Do not modify the original lists
    - Add each common number only once

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def find_common_elements(list1, list2):
    # TODO:
    # Create an empty list for the result.

    # TODO:
    # Loop through the first list.

    # TODO:
    # Check if the current number exists
    # in the second list.

    # TODO:
    # Make sure you don't add the same
    # number to the result more than once.

    # TODO:
    # Return the result.

    common_elements = []

    for num in list1:
        if num in list2 and num not in common_elements:
            common_elements.append(num)
    return common_elements


if __name__ == "__main__":
    list1 = [10, 20, 30, 40]
    list2 = [20, 40, 50, 60]

    result = find_common_elements(list1, list2)

    print(f"First list: {list1}")
    print(f"Second list: {list2}")
    print(f"Common elements: {result}")
