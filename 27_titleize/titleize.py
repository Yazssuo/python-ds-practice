def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    seperated = phrase.split()
    newPhrase = ""

    for word in seperated:
        for letter in word:
            if letter == word[0]:
                newPhrase = newPhrase + (letter.upper())
            else:
                newPhrase = newPhrase + (letter.lower())
        if word != seperated[len(seperated)-1]:
            newPhrase = newPhrase + " "
    return newPhrase