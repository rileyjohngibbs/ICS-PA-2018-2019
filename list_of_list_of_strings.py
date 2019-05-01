"""
Write a function that takes a list of lists of strings, like so:

    [["Riley", "Erik", "Brian"], ["Josh", "Jesse"]]

The function should combine the strings in the following way:
- Strings in the same list should be joined by " OR " and surrounded in parentheses to make one string from each list.
- Once each list has been made into a string, those strings should be joined by " AND ".

The example list of lists of strings should yield:

    "(Riley OR Erik OR Brian) AND (Josh OR Jesse)"

Assume that none of the lists are empty, and that none of the strings are empty either.
"""

def join_list_of_lists_of_strings(list_of_lists_of_strings):
    pass


# These tests should all pass

example_input_1 = [["Riley", "Erik", "Brian"], ["Josh", "Jesse"]]
example_output_1 = "(Riley OR Erik OR Brian) AND (Josh OR Jesse)"
assert join_list_of_lists_of_strings(example_input_1) == example_output_1

example_input_2 = [["Katelin"], ["Stella", "Becca"]]
example_output_2 = "(Katelin) AND (Stella OR Becca)"
assert join_list_of_lists_of_strings(example_input_2) == example_output_2