#find_optimal_words_1({list of string}, {list of string})
#Given a list of words of possible answers to choose from and a list of all possible words, determine which words are the best to choose for guesses

# STEPS USED:
# 1.) find the top 5 letters that occur in the list of possible answers
# 2.) find the words in the full dictionary that do not contain any of these letters and remove them
# 3.) sort the remaining words in the full dictionary into lists by the number of top letters that the word contians
# 4.) find the number of times each letter is the first letter in the possible answers list
# 5.) sort the values from step (4) in order of most times starting letter -> least times starting letter
# 6.) sort the lists from step (3) by whether they start with the letter that occurs the most as a starting letter in the possible answers
#           --> example: if list of words in step (3) == {crate, block, aroma, mince ...} 
#                        and the sorted list of # times starting letter == {b:5, a:3, c:2, m:1}
#                           ** The resulting list would be: {block, aroma, crate, mince}
# 7.) combine the newly modified lists (4 total) into a list of optimal words, retaining their orders
#           --> example: if list_5_top_letters == [block, aroma, crate, mince]
#                           list_4_top_letters == [black, apire, crash, money]
#                           list_3/2/1_top_letters == [...]
#                               ** The resulting list would be [block, aroma, crate, mince, black, aspire, crash, money]
# --> The list from step (7) is the list of optimal words 

from find_letters import find_letters

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def find_optimal_words_1(loa_file_given, dict_file_given):
    global alph
    
    loa_file = open(loa_file_given).read().splitlines()
    dict_file = open(dict_file_given).read().splitlines()
    
    # ----- Creates a list of the most common letters in the given file of possible answers ----- # 
    loa = []
    for line in loa_file:
        word = str(line)
        loa.append(word.lower())

    sorted_num_letters_in_ans = find_letters(loa_file_given, 'list')
    tmp = find_letters(loa_file_given, 'list')
    sorted_num_letters_in_ans.sort(reverse=True)
    
    alph_sorted = []
    
    i=0
    while i <=25:
        this_index = tmp.index(sorted_num_letters_in_ans[i])
        alph_sorted.append(alph[this_index])
        i+=1
    
    # ----- Finds words in the given dictionary file that contain the most number of the most common letters ----- # 
    #Step 1.) find words that contain every top 5 letters and words that do NOT contain ANY of the top 5 letters (if any, base case)
    #         --> these words will either eliminate or pick the best/worst words to guess by picking words that optimize the chance of
    #             guessing a correct letter (whether in the right place or not)
    
    top_5_letters = []

    #dictionary_to_search is the FULL dictionary that we will iterate through, and is NOT modified at all to keep an original copy of the dictionary
    dictionary_to_search = []
    #modified_dictionary_to_search is a modified version of the full dictionary that can be mutated to remove/reorganize words
    #starts as an exact copy of dictionary_to_search
    modified_dictionary_to_search = []
    sorted_optimal_words = []
    
    #convert the dictionary_to_search_tmp file into the dictionary_to_search lists
    for word in dict_file:
        dictionary_to_search.append(word.lower())
        modified_dictionary_to_search.append(word.lower())
    
    #take the top 5 letters from alph_sorted and put them into their own list to keep organized
    i=0
    while i < 5:
        top_5_letters.append(alph_sorted[i])
        i += 1
    
    #find words in full dictionary that do not contain any of the top 5 letters and remove them from modified_dictionary_
    for word in dictionary_to_search:
        c=0
        for letter in top_5_letters:
            if letter in word:
                c+=1
        
        if c == 0:
            modified_dictionary_to_search.remove(word)
    
    #correspond to # of top letters in e/a word --> c_5 = all 5 letters, ... , c_1 = 1 letter
    c_5 = []
    c_4 = []
    c_3 = []
    c_2 = []
    c_1 = []
    
    #iterate through modified_dictionary_ and sort words according to the number of times the top letters appear
    for word in modified_dictionary_to_search:
        c=0
        for letter in top_5_letters:
            if letter in word:
                c+=1
        if c == 5: c_5.append(word)
        if c == 4: c_4.append(word)
        if c == 3: c_3.append(word)
        if c == 2: c_2.append(word)
        if c == 1: c_1.append(word)    
         
    # find the letter that the most possible solutions start with 
    #       -> maximizes chance of getting the first letter of the word correct
    num_times_first_table = {
           'a': 0,
           'b': 0, 
           'c': 0,
           'd': 0,
           'e': 0,
           'f': 0,
           'g': 0,
           'h': 0,
           'i': 0,
           'j': 0,
           'k': 0,
           'l': 0,
           'm': 0,
           'n': 0,
           'o': 0,
           'p': 0,
           'q': 0,
           'r': 0,
           's': 0,
           't': 0,
           'u': 0,
           'v': 0,
           'w': 0,
           'x': 0,
           'y': 0,
           'z': 0,
           }
    
    for word in loa:
        starting_letter = word[0]
        num_times_first_table[starting_letter] += 1
    
    num_times_first_list = []
    num_times_first_list2 = []
    k = 0
    while k < 26:
        num_times_first_list.append(num_times_first_table[alph[k]])
        num_times_first_list2.append(num_times_first_table[alph[k]])

        k+=1
    
    for val in num_times_first_list:
        c = num_times_first_list.count(val)
        if c > 1:
            ind = num_times_first_list.index(val)
            num_times_first_list[ind] += 1
            num_times_first_list2[ind] +=1
            
    tmp_num_times_first = num_times_first_list 
    tmp_num_times_first.sort(reverse=True)
    sorted_num_times_first = tmp_num_times_first
        
    sorted_num_times_first_letters = []
    
    p = 0
    while p < 26:
        n = sorted_num_times_first[p]
        index = num_times_first_list2.index(n)
        sorted_num_times_first_letters.append(alph[index])
        p+=1
    
    #helper function to sort the given list of words (low) based on the already sorted list of letters (lol)
    #sorts low into order of starting letter, starting with index 0 of lol 
    def find_words_start_with(lol, low):
        for letter in lol:
            for word in low:
                if word[0] == letter:
                   rem_index = low.index(word)
                   del(low[rem_index])
                   low.insert(0, word)
        low.reverse()
        return low

    #update the lists that contain words w/ X amount of top letters 
    c_52 = find_words_start_with(sorted_num_times_first_letters, c_5)
    c_42 = find_words_start_with(sorted_num_times_first_letters, c_4)
    c_32 = find_words_start_with(sorted_num_times_first_letters, c_3)
    c_22 = find_words_start_with(sorted_num_times_first_letters, c_2)
    c_12 = find_words_start_with(sorted_num_times_first_letters, c_1)

    #append all these lists together in order:
    # ALL lists are previously sorted and are in order of most common *starting* letter
    # --> sorted list of words w/ all 5 most common letters is first
    # --> sorted list of words w/ 4/5 most common letters is next
    # --> ... 
    optimal_words = []
    optimal_words.extend(c_52)
    optimal_words.extend(c_42)
    optimal_words.extend(c_32)
    optimal_words.extend(c_22)
    optimal_words.extend(c_12)

    return optimal_words

              
            
    
    
    
print(find_optimal_words_1('answers.txt', 'dictionary.txt'))