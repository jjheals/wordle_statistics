#Script to find num times a letter occurs in the dictionary

letters = {'a': {'num_occur': 0},
           'b': {'num_occur': 0}, 
           'c': {'num_occur': 0},
           'd': {'num_occur': 0},
           'e': {'num_occur': 0},
           'f': {'num_occur': 0},
           'g': {'num_occur': 0},
           'h': {'num_occur': 0},
           'i': {'num_occur': 0},
           'j': {'num_occur': 0},
           'k': {'num_occur': 0},
           'l': {'num_occur': 0},
           'm': {'num_occur': 0},
           'n': {'num_occur': 0},
           'o': {'num_occur': 0},
           'p': {'num_occur': 0},
           'q': {'num_occur': 0},
           'r': {'num_occur': 0},
           's': {'num_occur': 0},
           't': {'num_occur': 0},
           'u': {'num_occur': 0},
           'v': {'num_occur': 0},
           'w': {'num_occur': 0},
           'x': {'num_occur': 0},
           'y': {'num_occur': 0},
           'z': {'num_occur': 0}
           }

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

file_ = open('dictionary.txt').read().splitlines()

wordleDictionary = []

for line in file_:
    word = str(line)
    wordleDictionary.append(word.lower())

print('----------------------------------------+---------------------------------------- \n' + 
      'The dictionary being used: \n\n' + format(wordleDictionary) + 
      '\n\n ----------------------------------------+----------------------------------------\n')

# finds the amount of times every letter occurs in the dictionary 
def find_letters():
    
    #iterate through the dictionary 
    for word in wordleDictionary:
        
        #for loop inside for loop - 
        #    - (for each word in dictionary) iterate through the alphabet (alph)
        #      and count the number of times the current letter appears in the word 
        #    - update 'letters' table accordingly
        for letter in alph:
            c = word.count(letter)
            letters[letter]['num_occur'] += c

print('letters table before: \n' + format(letters) + 
      '\n\n ----------------------------------------+----------------------------------------\n')

find_letters()

print('letters table after: \n' + format(letters) + 
      '\n\n ----------------------------------------+----------------------------------------\n')
        
