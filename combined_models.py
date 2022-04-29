#generic method for developing a list of optimal words given two files of data

alph = ['A','B','C','D',
            'E','F','G','H',
            'I','J','K','L',
            'M','N','O','P',
            'Q','R','S','T',
            'U','V','W','X',
            'Y','Z']

#helpers to reduce redundant code
    #creates lists from the given file (string)
def make_list_from_fileName(file_name):
    this_file = open(file_name).read().splitlines()
    this_list = []
    for line in this_file:
        word = str(line).upper()
        this_list.append(word)
    return this_list

    #sorts a list of words by the sorted starting letters in lol
def sort_low_by_starting_letter(low, lol):
    sorted_low = []

    for letter in lol:
        for word in low:
            if word[0] == letter:
                sorted_low.append(word)
    
    return sorted_low

    #sorts the keys of a dictionary by the values of the dictionary
def sort_dict_keys_by_values(dict): 
    low = []
    lov = []
    sorted_low = []

    for key in dict:
        low.append(key)
        lov.append(dict[key])
    
    lov.sort()

    i=0
    while i < len(dict):
        this_v = lov[i]
        for word in low:
            if (dict[word] == this_v) and (word not in sorted_low):
                sorted_low.append(word)
        i+=1

    return sorted_low

    #sorts a list of words by the values given in a dictionary with all (or some) of the words as keys
def sort_low_by_values_from_dict(low, dict):
    temp_dict = {}

    for word in low:
        temp_dict[word] = dict[word]

    sorted_low = sort_dict_keys_by_values(temp_dict)
    return sorted_low

    #saves the result (a list) to a file (save_to: string)
def save_result(result, save_to):
    save_file = open(save_to, 'w')
    save_file.truncate(0)
    save_file.close()

    save_file2 = open(save_to, "a")
    for word in result:
        save_file2.write(f'{word}\n')

# ------------------------------ MODEL 1 CODE ------------------------------ #

def model1_find_optimal_words(dictionary_fileName, list_of_solutions_fileName):
    global alph

    dictionary = make_list_from_fileName(dictionary_fileName)
    list_of_solutions = make_list_from_fileName(list_of_solutions_fileName)

    # ----- find the number of times every letter is in the list of solutions ----- #
    letter_num_occur_table = {}
    word_per_letter_total_occur = {}
    starting_letter_table = {}
    
    for letter in alph:
        letter_num_occur_table[letter] = 0
        starting_letter_table[letter] = 0

        #count the number of times each letter is in the list of solutions and num times it is the starting letter
    for word in list_of_solutions:
        for letter in alph:
            if word[0] == letter:
                starting_letter_table[letter] += 1

            for l in word:
                if letter == l:
                    letter_num_occur_table[letter] += 1

        #convert to percents to normalize 
    for letter in alph: 
        letter_num_occur_table[letter] = (letter_num_occur_table[letter] / (len(list_of_solutions)*5)) * 100

    # ----- sort the words into lists based on the mean sum(%) ----- #

        #update the word_per_letter
    for word in dictionary:
        word_per_letter_total_occur[word] = 0
        for letter in word:
            word_per_letter_total_occur[word] += letter_num_occur_table[letter]

    #sort based on the sum of probabilities of letters in each word
    sorted_word_by_letter_prob = sort_dict_keys_by_values(word_per_letter_total_occur)

    #split sorted_word_by_letter_prob into 4 brackets
    div_num = len(sorted_word_by_letter_prob)/4
    round(div_num)

    b=[]
    b0=[]
    b1=[]
    b2=[]

    i=0
    while i <= div_num:
        b.append(sorted_word_by_letter_prob[i])
        i+=1
    while i < div_num*2:
        b0.append(sorted_word_by_letter_prob[i])
        i+=1
    while i <= div_num*3:
        b1.append(sorted_word_by_letter_prob[i])
        i+=1
    while i < div_num*4:
        b2.append(sorted_word_by_letter_prob[i])
        i+=1

    # ----- sort the brackets by probability of the correct starting letter in list of solutions ----- #
    sorted_starting_letter_prob = sort_dict_keys_by_values(starting_letter_table)

    b = sort_low_by_starting_letter(b, sorted_starting_letter_prob)
    b0 = sort_low_by_starting_letter(b0, sorted_starting_letter_prob)
    b1 = sort_low_by_starting_letter(b1, sorted_starting_letter_prob)
    b2 = sort_low_by_starting_letter(b2, sorted_starting_letter_prob)

    # ----- Append together ----- #
    model_1_result = []
    model_1_result.extend(b)
    model_1_result.extend(b0)
    model_1_result.extend(b1)
    model_1_result.extend(b2)
    model_1_result.reverse()

    save_result(model_1_result, 'model_1_results.txt')
    
    print(f'--> Saved result from model 1 to \'model_1_results.txt\'')

    return model_1_result


# ------------------------------ MODEL 2 CODE ------------------------------ #

# *borrows some helper functions from model 1

def model2_find_optimal_words(dictionary_fileName, letters_per_round_fileName, guesses_per_round_fileName, numGuesses_per_round_fileName):
    global alph

    dictionary = make_list_from_fileName(dictionary_fileName)
    dictionary_no_dupes = []
    temp_letters_per_round = open(letters_per_round_fileName).read().splitlines()
    temp_guesses_per_round = open(guesses_per_round_fileName).read().splitlines()
    temp_numGuesses_per_round = open(numGuesses_per_round_fileName).read().splitlines()
    letters_per_round = []
    guesses_per_round = []
    numGuesses_per_round = []

    #fix dictionary_no_dupes
    for word in dictionary:
        if word not in dictionary_no_dupes:
            dictionary_no_dupes.append(word)
    
    #fill letters_per_round
    for line in temp_letters_per_round:
        sow = str(line)
        lst = sow.split(' ')
        lst.remove('')
        letters_per_round.append(lst)
    
    #fill numGuesses_per_round
    for line in temp_numGuesses_per_round:
        num = str(line)
        if num == 'X': numGuesses_per_round.append(7)
        else: 
            num2 = int(line)
            numGuesses_per_round.append(num2)

    #create dic of avg SR of each letter from letters_per_round 
    #and numGuesses_per_round
    letter_avg_SR_dict = {} 
    temp_num_occur_dict = {}

    for letter in alph:
        letter_avg_SR_dict[letter] = 0
        temp_num_occur_dict[letter] = 0

    i=0
    while i < len(numGuesses_per_round)-1:
        this_num_guesses = numGuesses_per_round[i]
        these_letters = letters_per_round[i]

        for letter in these_letters:    
            letter_avg_SR_dict[letter] += this_num_guesses
            temp_num_occur_dict[letter] +=1
        i+=1

    for letter in alph:
        this_num = letter_avg_SR_dict[letter]
        this_num_occur = temp_num_occur_dict[letter]

        if this_num_occur != 0:
            letter_avg_SR_dict[letter] = this_num/this_num_occur

    #fill guesses_per_round 
    for line in temp_guesses_per_round:
        sow = str(line)
        lst = sow.split(' ')
        lst.remove('')
        guesses_per_round.append(lst)

    all_words_dict = {}

    #update the num_occur value in all_words_dict
    for word in dictionary_no_dupes:
        c = 0
        for w in dictionary:
            if w == word:
                c += 1
        
        all_words_dict[word] = {'num_occur':c, 'avg_num_guesses':0}

    #update the avg_num_guesses value in all_words_dict
    i = 0
    for numGuesses in numGuesses_per_round:
        round = guesses_per_round[i]
        for word in round:
            all_words_dict[word]['avg_num_guesses'] += numGuesses
        i+=1

    for word in all_words_dict:
        this_avg = all_words_dict[word]['avg_num_guesses']
        all_words_dict[word]['avg_num_guesses'] = this_avg / all_words_dict[word]['num_occur']

    #create a dict with just words and corresponding avg_num_guesses to use helper fn
    #   and reduce redundant code
    temp_dict = {}
    for word in all_words_dict:
        temp_dict[word] = all_words_dict[word]['avg_num_guesses']


    # ----- create lists sorted by the sum of success rates of each letter ----- #
    word_sum_letter_prob_dict = {}

    for word in dictionary_no_dupes:
        word_sum_letter_prob_dict[word] = 0

    for word in dictionary_no_dupes:
        lol = []
        for l in word:
            lol.append(l)
    
        for letter in lol:
            word_sum_letter_prob_dict[word] += letter_avg_SR_dict[letter]

    sorted_low_by_sum_letters = sort_dict_keys_by_values(word_sum_letter_prob_dict)
    
    div_num = len(sorted_low_by_sum_letters)/4

    b=[]
    b0=[]
    b1=[]
    b2=[]

    i=0
    while i <= div_num:
        b.append(sorted_low_by_sum_letters[i])
        i+=1
    while i < div_num*2:
        b0.append(sorted_low_by_sum_letters[i])
        i+=1
    while i <= div_num*3:
        b1.append(sorted_low_by_sum_letters[i])
        i+=1
    while i < div_num*4:
        b2.append(sorted_low_by_sum_letters[i])
        i+=1

    # ----- sort brackets from above by avg num guesses per WORD ----- #
    b = sort_low_by_values_from_dict(b, temp_dict)
    b0 = sort_low_by_values_from_dict(b0, temp_dict)
    b1 = sort_low_by_values_from_dict(b1, temp_dict)
    b2 = sort_low_by_values_from_dict(b2, temp_dict)

    # ----- append together in order ----- # 
    model_2_result = []
    model_2_result.extend(b)
    model_2_result.extend(b0)
    model_2_result.extend(b1)
    model_2_result.extend(b2)

    save_result(model_2_result, 'model_2_results.txt')

    print(f'--> Saved result from model 2 to \'model_2_results.txt\'')

    return model_2_result

model1_find_optimal_words('dictionary.txt', 'answers.txt')
model2_find_optimal_words('guesses_data.txt', 'letters_guessed_per_round.txt', 'guesses_per_round.txt', 'num_guesses_data.txt')
