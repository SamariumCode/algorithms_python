

def isomorphic(s, t):
    """
    Determines whether two strings `s` and `t` are isomorphic.

    Two strings are isomorphic if the characters in one string can be replaced 
    to get the other string. Each character must map to exactly one character, 
    and no two characters may map to the same character.

    Parameters:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if `s` and `t` are isomorphic, False otherwise.

    Examples:
        >>> isomorphic('egg', 'add')
        True
        >>> isomorphic('foo', 'bar')
        False
        >>> isomorphic('paper', 'title')
        True
        >>> isomorphic('fow', 'baa')
        False
    """
    if len(s) != len(t) : return False
    
    dict = {}
    set_values = set()
    
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_values: return False
            dict[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dict[s[i]]!= t[i]: return False
            
    return True


print(isomorphic('fow', 'baa'))
