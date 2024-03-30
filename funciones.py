def clean_text(unaCadena): 
    special_char =('.', ',', '"', "'", ';', ':', '-', '!', '(', ')', '+', '/', '@')
    clean_text = unaCadena
    for char in special_char:
        clean_text = clean_text.replace(char,'')
    return clean_text