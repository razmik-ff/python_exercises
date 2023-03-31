def alphabets():
    import string
    alphabet = list(string.ascii_lowercase)
    dict_alpha = {k: v for k, v in enumerate(alphabet, 1)}
    return dict_alpha
    



print(alphabets())