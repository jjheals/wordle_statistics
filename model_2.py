#The basis for model 2
#Overview: 
#   Take the list of all words players guessed and sort it into a list of optimal words 
#   based on the success rate of each word's individual letters (letters contained in words)
#   with high success rates) and the average success rate of the word itself. 

#       **Sorted FIRST by # top 5 successful letters because this is a more general solution
#           THEN sorted by the average success rate of the word itself as a "tie breaker" b/w 
#           words with the same # of top 5 successful letters 


def model2(filename_of_all_words, filename_of_num_guesses_data, filename_of_guessed_wordsPR, filename_of_guessed_lettersPR):

    file_all_words = open(filename_of_all_words).read().splitlines()
    file_num_guessesPR = open(filename_of_num_guesses_data).read().splitlines()
    file_guessed_wordsPR = open(filename_of_guessed_wordsPR).read().splitlines()
    file_guessed_lettersPR = open(filename_of_guessed_lettersPR).read().splitlines()

    alph = ['A','B','C','D',
            'E','F','G','H',
            'I','J','K','L',
            'M','N','O','P',
            'Q','R','S','T',
            'U','V','W','X',
            'Y','Z']
    
    #convert all the files into lists 
    #all words (dictionary used)
    all_words = []
    nodupes_all_words = []

    for line in file_all_words:
        word = str(line)

        all_words.append(word)
        
        if word not in nodupes_all_words:
            nodupes_all_words.append(word)

    #num guesses to solve
    num_guesses = []

    for line in file_num_guessesPR:
        num = str(line)
        if num == 'X': num_guesses.append(7)
        else: 
            num2 = int(line)
            num_guesses.append(num2)

    #guessed words per round
    guessed_wordsPR = []

    for line in file_guessed_wordsPR:
        sow = str(line)
        lst = sow.split(' ')
        lst.remove('')
        guessed_wordsPR.append(lst)
  

    #guessed letters per round
    guessed_lettersPR = []

    for line in file_guessed_lettersPR:
        this_round = str(line)
        this_round_list = this_round.split(' ')
        while '' in this_round_list:
            this_round_list.remove('')
        guessed_lettersPR.append(this_round_list)
            
    print(f'all_words: \n{all_words} \nnum_guesses: \n{num_guesses} \nguessed_wordsPR: \n{guessed_wordsPR} guessed_lettersPR: \n{guessed_lettersPR}')

    letter_success_rate_table = {
           'A': {'avg_guesses':0 , 'num_occur':0},
           'B': {'avg_guesses':0 , 'num_occur':0}, 
           'C': {'avg_guesses':0 , 'num_occur':0},
           'D': {'avg_guesses':0 , 'num_occur':0},
           'E': {'avg_guesses':0 , 'num_occur':0},
           'F': {'avg_guesses':0 , 'num_occur':0},
           'G': {'avg_guesses':0 , 'num_occur':0},
           'H': {'avg_guesses':0 , 'num_occur':0},
           'I': {'avg_guesses':0 , 'num_occur':0},
           'J': {'avg_guesses':0 , 'num_occur':0},
           'K': {'avg_guesses':0 , 'num_occur':0},
           'L': {'avg_guesses':0 , 'num_occur':0},
           'M': {'avg_guesses':0 , 'num_occur':0},
           'N': {'avg_guesses':0 , 'num_occur':0},
           'O': {'avg_guesses':0 , 'num_occur':0},
           'P': {'avg_guesses':0 , 'num_occur':0},
           'Q': {'avg_guesses':0 , 'num_occur':0},
           'R': {'avg_guesses':0 , 'num_occur':0},
           'S': {'avg_guesses':0 , 'num_occur':0},
           'T': {'avg_guesses':0 , 'num_occur':0},
           'U': {'avg_guesses':0 , 'num_occur':0},
           'V': {'avg_guesses':0 , 'num_occur':0},
           'W': {'avg_guesses':0 , 'num_occur':0},
           'X': {'avg_guesses':0 , 'num_occur':0},
           'Y': {'avg_guesses':0 , 'num_occur':0},
           'Z': {'avg_guesses':0 , 'num_occur':0},
           }

    word_success_rate_table = { }

    #fill in letter_success_rate_table and word_success_rate_table
    i=0
    while i < len(num_guesses):
        this_low = guessed_wordsPR[i]
        this_lol = guessed_lettersPR[i]
            
        this_num_guesses = num_guesses[i]

        for letter in this_lol:
            letter_success_rate_table[letter]['avg_guesses'] += this_num_guesses
            letter_success_rate_table[letter]['num_occur'] += 1
        
        for word in this_low:

            if not word in word_success_rate_table:
                word_success_rate_table[word] = {'avg_guesses':0 , 'num_occur':0}

            word_success_rate_table[word]['avg_guesses'] += this_num_guesses
            word_success_rate_table[word]['num_occur'] += 1

        i+=1
    
    for l in alph:
        if letter_success_rate_table[l]['num_occur'] != 0:
            letter_success_rate_table[l]['avg_guesses'] = letter_success_rate_table[l]['avg_guesses']/letter_success_rate_table[l]['num_occur']
    
    for word in nodupes_all_words:
        if word_success_rate_table[word]['num_occur'] != 0:
            word_success_rate_table[word]['avg_guesses'] = word_success_rate_table[word]['avg_guesses']/word_success_rate_table[word]['num_occur']

    print(f'letter_success_table: \n{letter_success_rate_table}')    
    print(f'word_success_rate_table: \n{word_success_rate_table}')
        
    #make a list of the top 5 most successful letters
    l1 = ''
    l2 = ''
    l3 = ''
    l4 = ''
    l5 = ''

    min1 = 7
    min2 = 7
    min3 = 7
    min4 = 7
    min5 = 7

    i = 0
    while i < 26:
        this_letter = alph[i]
        this_avg_guesses = letter_success_rate_table[this_letter]['avg_guesses']

        if letter_success_rate_table[this_letter]['num_occur'] != 0:
            if  this_avg_guesses < min1:
                min1 = this_avg_guesses
                l1 = this_letter

            elif this_avg_guesses < min2:
                min2 = this_avg_guesses
                l2 = this_letter

            elif this_avg_guesses < min3:
                min3 = this_avg_guesses
                l3 = this_letter
        
            elif this_avg_guesses < min4:
                min4 = this_avg_guesses
                l4 = this_letter
        
            elif this_avg_guesses < min5:
                min5 = this_avg_guesses
                l5 = this_letter

        i+=1

    top_5_letters = [l1,l2,l3,l4,l5]

    c_5 = []
    c_4 = []
    c_3 = []
    c_2 = []
    c_1 = []
    c_0 = []

    for word in nodupes_all_words:
        c = 0

        for letter in top_5_letters:
            if letter in word:
                c+=1
        
        if c == 0: c_0.append(word)
        if c == 1: c_1.append(word)
        if c == 2: c_2.append(word)
        if c == 3: c_3.append(word)
        if c == 4: c_4.append(word)
        if c == 5: c_5.append(word)

    
    print(f'\nc_0: \n{c_0}\nc_1: \n{c_1}\nc_2: \n{c_2}\nc_3: \n{c_3}\nc_4: \n{c_4}\nc_5: \n{c_5}')
    print(f'\ntop_5_letters: \n{top_5_letters}')

    def sort_words_by_success(low):
        tmp_words = []
        sorted_words = []
        tmp_values = []
        tmp_values_sorted = []

        for word in nodupes_all_words:
            if word in low:
                tmp_words.append(word)
                tmp_values.append(word_success_rate_table[word]['avg_guesses'])
                tmp_values_sorted.append(word_success_rate_table[word]['avg_guesses'])
            
        tmp_values_sorted.sort(reverse=True)
        
        for n in tmp_values_sorted:
            index = tmp_values.index(n)
            this_word = tmp_words[index]

            sorted_words.append(tmp_words[index])
            tmp_values.remove(n)
            tmp_words.remove(this_word)

        return sorted_words

    c_5 = sort_words_by_success(c_5)
    c_4 = sort_words_by_success(c_4)
    c_3 = sort_words_by_success(c_3)
    c_2 = sort_words_by_success(c_2)
    c_1 = sort_words_by_success(c_1)
    c_0 = sort_words_by_success(c_0)

    print(f'\nc_0: \n{c_0}\nc_1: \n{c_1}\nc_2: \n{c_2}\nc_3: \n{c_3}\nc_4: \n{c_4}\nc_5: \n{c_5}')

    optimal_words = []
    optimal_words.extend(c_5)
    optimal_words.extend(c_4)
    optimal_words.extend(c_3)
    optimal_words.extend(c_2)
    optimal_words.extend(c_1)
    optimal_words.extend(c_0)


    print(f'\n\nFINAL LIST OF OPTIMAL WORDS: \n{optimal_words}')
    return optimal_words

model2('guesses_data.txt', 'num_guesses_data.txt','guesses_per_round.txt', 'letters_guessed_per_round.txt')

