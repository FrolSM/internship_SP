import string

def count_words(s):
    clean_string = str(s).lower()
    chars = string.punctuation
    for char in chars:
        clean_string = clean_string.replace(char, '')

    res_dict = {}
    for word in clean_string.split():
        if word in res_dict:
            res_dict[word] += 1
        else:
            res_dict[word] = 1

    return res_dict
