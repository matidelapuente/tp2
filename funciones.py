def cantPalabras(unaCadena):
    """Counts the words in a sentence.
    Args:
        unaCadena(str): input string containing a sentence to count its words.
    Returns:
        int: amount of words in the input string."""

    words = unaCadena.split()
    count = 0
    for word in words:
        if not word.isdigit():
            count += 1
    return count

def clean_text(unaCadena): 
    """Removes special characters from a string.
    Args:
        unaCadena (str): input string from which special characters will be removed.
    Returns:
        str: the input string after removing special characters."""
    
    special_char =('.', ',', '"', "'", ';', ':', '-', '!', '(', ')', '+', '/', '@')
    clean_text = unaCadena
    for char in special_char:
        clean_text = clean_text.replace(char,'')
    return clean_text

def isHeterogram(aString):
    """Checks if a string is a Heterogram.
    Args:
        aString (str): input string (word or phrase) to be checked.
    Returns:
        bool: True if the input string is a heterogram, False otherwise."""
    
    letters = set()
    for letter in aString:
        if letter in letters:
            return False
        elif letter.isalpha():
            letters.add(letter.lower())
    return True