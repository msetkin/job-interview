def is_braces_balanced(some_string: str) -> bool:
    """
        is_braces_balanced checks if the input string brace-wise balanced. "Balanced" means, that the number and the
        order of opening and closing brackets are symmetrical. See test-cases for more details.
        :param some_string: input string, can contain opening or closing braces: parentheses, square and curly brackets
        :return: true is the input string is "balanced" and false otherwise
    """
    stack = list()
    helper_dict = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for i in some_string:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif stack[len(stack) - 1] == helper_dict[i]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


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
