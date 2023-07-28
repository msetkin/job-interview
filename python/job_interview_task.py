def is_braces_balanced(input_string: str) -> bool:
    """
        is_braces_balanced checks if the input string brace-wise balanced. "Balanced" means, that the number and the
        order of opening and closing brackets are symmetrical. See test-cases for more details.
        :param input_string: input string, can contain opening or closing braces: parentheses, square and curly brackets.
        :return: true is the input string is "balanced" and false otherwise
    """
    # your solution goes here
    return True

# TEST CASES:
assert is_braces_balanced('({[]})')
assert is_braces_balanced('(()){}')
assert is_braces_balanced('')
assert not is_braces_balanced('({[}])')
assert not is_braces_balanced('({[}]))))')
assert not is_braces_balanced('}{][)(')
assert not is_braces_balanced('}{][)](')
assert not is_braces_balanced('(((({{{{{')
assert not is_braces_balanced(']]])}}})}}}}')
print("TESTS PASSED")
