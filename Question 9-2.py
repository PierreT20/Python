string = input('Enter your string: ')
def vowels():
    vowels = 0
    for i in range(len(string)):
        if string[i] in 'aeiou':
            vowels = vowels + 1
    return vowels

def consonants():
    consonants = 0
    for i in range(len(string)):
        if string[i] in 'bcdfghjklmnpqrstvwxyz':
            consonants = consonants + 1
    return consonants

print('The string you entered includes ',vowels(),'vowels and',consonants(),'constants')
