def is_palindrome(word):
    """
    This function confirm if a word or a phrase is a polidrome 

    Args: 
        The word or the phrase that will check if is a polindrome, if is not a str instance directly return false.

    return: 
        boolean: True if is a palindrome, false in other case, of the arg is not a str instance directly return false.

    """
    if not isinstance(word, str):
        return False
    word = str(''.join(e for e in word if e.isalnum()).lower()) 
    return word == word[::-1] 
