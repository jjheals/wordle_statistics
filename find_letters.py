#Script to find num times a letter occurs in the given file

# finds the amount of times every letter occurs in the dictionary 
#consumes the name of a file {string} and an optional output type {string} 
#output type is one of: 'table', 'list'
#output type defaults to table if no argument given
def find_letters(file_, output_type='table'):
    
    this_file = open(file_).read().splitlines()
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    this_list = []
    

    this_letters = {
           'a': {'num_occur': 0},
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
    
    for line in this_file:
        word = str(line)
        this_list.append(word.lower())
        
    #iterate through the dictionary 
    for word in this_list:
        
        #for loop inside for loop - 
        #    - (for each word in dictionary) iterate through the alphabet (alph)
        #      and count the number of times the current letter appears in the word 
        #    - update 'letters' table accordingly
        for letter in alph:
            c = word.count(letter)
            this_letters[letter]['num_occur'] += c
     
    if output_type == 'table':
             return this_letters    
    elif output_type == 'list':
        prnt_list = []
        for l in alph:
            prnt_list.append(this_letters[l]['num_occur'])
        return prnt_list


