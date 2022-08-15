def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    tracker = []
    for char in parens:
        if char == "(":
            tracker.append(char)
        elif char == ")":
            if len(tracker) > 0:
                tracker.pop()
            else:
                return False
    return True if len(tracker) == 0 else False
