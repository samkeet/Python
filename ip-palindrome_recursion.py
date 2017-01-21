def removeWhite(s):
    """
    removing spaces and punctuation from given string
    """
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_string = ""
    for char in s:
        if char in alpha:
            new_string = new_string + char
    return new_string

def isPal(s):
    """
    palindrome checker using recursion
    """
    s = removeWhite(s)
    strlen = len(s)
    if s == "":
        return True
    elif s[0] == s[strlen-1]:
        return isPal(s[1:strlen-1])
    else:
        return False