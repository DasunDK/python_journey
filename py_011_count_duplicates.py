"""
------------------------------------------------------------
Python Journey - PY-011
Challenge: Count Duplicate Numbers

Objective:
    Count how many different numbers appear more than
    once in a list.

Rules:
    - Use a function
    - Use loops
    - Nested loops are allowed
    - Use conditional statements
    - Do not use set()
    - Do not use count()
    - Do not use collections.Counter
    - Do not use dictionaries for counting
    - Handle multiple duplicates
    - A value should only be counted once

Difficulty:
    🥉 Bronze+

Author:
    Dasun
------------------------------------------------------------
"""


def count_duplicates(numbers):
    # TODO:
    # Think about what variable you need to keep
    # track of the number of duplicated values.

    # TODO:
    # Think about whether you need one loop
    # or two loops.
    #
    # How can you compare one number with the
    # other numbers in the list?

    # TODO:
    # You need to know whether the current number
    # appears more than once.

    # TODO:
    # Be careful!
    #
    # If a number appears 3 or 4 times, it should
    # still only increase your duplicate counter
    # by ONE.

    # TODO:
    # You also need to prevent counting the same
    # duplicated value again later.
    #
    # Example:
    # [10, 10, 20, 20]
    #
    # 10 should be counted once.
    # 20 should be counted once.

    # TODO:
    # Return the number of different duplicated
    # values.

    duplicate_count = 0
    duplicates_found = []
    for i in range(len(numbers)):
        for x in range(len(numbers)):
            if i < x:
                if numbers[i] == numbers[x] and numbers[i] not in duplicates_found:
                    duplicate_count += 1
                    duplicates_found.append(numbers[i])
                    break
    return duplicate_count


if __name__ == "__main__":
    numbers = [10, 20, 10, 30, 20, 40, 20]

    result = count_duplicates(numbers)

    print(f"Number of duplicated values: {result}")
