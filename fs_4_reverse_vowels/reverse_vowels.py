def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    new_s = list(s)
    vowels = []
    indexes = []
    for index in range(len(new_s)):
        if new_s[index] in ['a','e','i','o','u']:
            print("Found vowel!")
            vowels.append(new_s[index])
            indexes.append(index)
    reversed_vowels = vowels[::-1]
    new_string = []
    for i in range(len(new_s)):
        if i in indexes:
            new_string.append(reversed_vowels[i])
        else:
            new_string.append(new_s[i])
    new_string_act = ""
    new_string_act.join(new_string)
    return new_string_act
    
    
