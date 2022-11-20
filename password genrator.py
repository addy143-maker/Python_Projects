import random
from string import punctuation 

#function for shuffling all the character of the string 
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)
#character to Add to the pasword code 
uppercaseletter1 = chr(random.randint(65,90))
uppercaseletter2 = chr(random.randint(65,90))
lowercaseletter1 = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punctuationSign1 = chr(random.randint(32,152))
punctuationSign2 = chr(random.randint(32,152))
#shuffleling all the character 
password = uppercaseletter1 + uppercaseletter2 + lowercaseletter1 + lowercaseletter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

#printing the output 
print(password)