def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swappedLtr = ""
    if to_swap.isupper():
        swappedLtr = to_swap.lower()
    else:
        swappedLtr = to_swap.upper()

    newStr = ""
    for letter in phrase:
        if letter == to_swap:
            newStr = newStr + swappedLtr
        elif letter == swappedLtr:
            newStr = newStr + to_swap
        else:
            newStr = newStr + letter
    return newStr