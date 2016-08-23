from string import ascii_lowercase as az

def check(text):
    return set(text.lower()).issuperset(set(az))
	
print (check('abc') == False)
print (check('adcdefghjiklmnopqrstuvwxyz') == True)
print (check('ABCDEFGHJIKLMOPQRSTUVWXYZ') == True)
