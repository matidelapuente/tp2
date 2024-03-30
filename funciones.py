def cantPalabras(unaCadena):
    words = unaCadena.split()
    count = 0
    for word in words:
        if not word.isdigit():
            count += 1
    return count

def clean_text(unaCadena): 
    special_char =('.', ',', '"', "'", ';', ':', '-', '!', '(', ')', '+', '/', '@')
    clean_text = unaCadena
    for char in special_char:
        clean_text = clean_text.replace(char,'')
    return clean_text

def isHeterogram(aString):
    letters = set()
    for letter in aString:
        if letter in letters:
            return False
        elif letter.isalpha():
            letters.add(letter.lower())
    return True