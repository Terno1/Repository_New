# Copyriight unknown 2016
from string import ascii_lowercase as az

def check(text):
    return set(text.lower()).issuperset(set(az))
	
print (check('abc') == False)
print (check('adcdefghijklmnopqrstuvwxyz') == True)
print (check('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == True)
print (check('Quick brown fox jumps over the lazy dog') == True)
