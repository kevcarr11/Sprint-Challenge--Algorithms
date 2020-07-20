'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  
    # base case
    if len(word) == 0:
        return
    first, rest = word[0], word[1:]
    if first is 't' and word[1] is 'h':
        print('hit')
        return 1 + count_th(rest)
    else:
        return count_th(rest)

  
count_th('abcthefthghith')