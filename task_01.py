import string

def is_palindrome(s):
    clean_s = str(s).lower()
    chars = string.punctuation + string.whitespace
    for char in chars:
        clean_s = clean_s.replace(char, '')
    return clean_s == clean_s[::-1]
