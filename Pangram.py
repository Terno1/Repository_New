alphabet ='abcdefghhijklmnopqrstuvwxyz'

def check(text):
    return set(text.lower()).issuperset(set(alphabet))
print (check('abc'))
