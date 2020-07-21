'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    n1 = len(word)
    n2 = len('th')

    # base case
    if n1 == 0 or n1 < n2:
        return 0
    
    # Recursive Case
    # Checking if the first
    # substring matches
    elif word[0: n2] == 'th':
        return 1 + count_th(word[n2 - 1:])

    # Otherwise, return the count  
    # from the remaining index 
    else:
        return count_th(word[n2 - 1:])


print(count_th('abcthefthghith'))
