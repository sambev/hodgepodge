def makePalindrome(string):
    """
    Try to make a palidrome out of provided string
    return: the palindrome or -1 if you can't create the palindrome
    """
    the_single = []
    dupes = []
    l_string = [string]
    while l_string:
        c = l_string.pop(0)
        if c not in l_string:
            the_single += c[0]
            # if there is more than one single it isn't a palindrome
            if len(the_single) > 1:
                return -1
            else:
                l_string = [x for x in l_string if x != c]
        else:
            dupes.append(c)
            l_string = [x for x in l_string if x != c]
    
    return string


print makePalindrome('ciivc')
print makePalindrome('racecar')
print makePalindrome('samuel')
