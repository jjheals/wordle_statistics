#function to test models 
from numpy import average
from combined_models import make_list_from_fileName, save_result
from random import randint
import sys

def testing_fn(optimal_words_filename, solutions_file_name, save_to, num_rounds):

    sys.setrecursionlimit(round(num_rounds*2.5))

    optimal_words = make_list_from_fileName(optimal_words_filename)
    solutions = make_list_from_fileName(solutions_file_name)
    global num_rounds_to_play; num_rounds_to_play = num_rounds

    #make sure all the solutions are in the optimal words file, add randomly if not
    # --> adding in randomly preserves the accuracy of the model, because there is an equal chance that
    #     the word is inserted at any point in the list
    for word in solutions:
        if word not in optimal_words:
            rand = randint(1, len(optimal_words) - 1)
            optimal_words.insert(rand, word)

    global num_guesses; num_guesses = 0
    global total_num_guesses; total_num_guesses = []
    global this_solution; this_solution = solutions[randint(0,len(solutions) -1)]
    global remaining_words; remaining_words = optimal_words.copy()

    def initialize_new_round():
        global num_guesses
        global remaining_words
        global this_solution

        num_guesses = 0
        remaining_words = optimal_words.copy()
        this_solution = solutions[randint(0,len(solutions) -1)]

    def result_found():

        global total_num_guesses
        global num_guesses
        global this_solution
        global remaining_words
        global num_rounds_to_play

        
        total_num_guesses.append(num_guesses)
        print(f'round: {len(total_num_guesses)} -- solution: {this_solution} -- num_guesses: {num_guesses}')

        if len(total_num_guesses) >= num_rounds_to_play:
            avg_num_guesses = average(total_num_guesses) 
            print(f'average number of guesses for {num_rounds} rounds: {avg_num_guesses}')
            sys.exit()
        else: 
            initialize_new_round()
            testing_loop()

    #test list of optimal words
    def testing_loop():
        global this_solution
        global remaining_words
        global num_guesses

        for word in optimal_words:

            if word in remaining_words:
                if word == this_solution:
                    result_found()

                else:
                        remaining_words.remove(word)
                        #check all the current word's statuses and update the discount words list accordingly 
                        i=0
                        while i < 5:
                            #if the letter is no where in the solution
                            # --> remove all words containing this letter
                            if word[i] not in this_solution:
                                this_letter = word[i]
                                for w in remaining_words:
                                    if this_letter in w:
                                            remaining_words.remove(w)
                            #else if the current word's corrent letter is the same as the solutions current letter
                            # --> remove all words where this is not true
                            elif word[i] == this_solution[i]:
                                for w in remaining_words:
                                    if word[i] != w[i]:
                                        remaining_words.remove(w)
                            #else if the current word's current letter is not the same as the solution's current letter 
                            #      but is in the solution somewhere else
                            # --> remove all words that have the current word's current letter in the same index
                            elif word[i] in this_solution: 
                                for w in remaining_words:
                                    if word[i] == w[i]:
                                        remaining_words.remove(w)

                            i+=1
                        num_guesses += 1

    testing_loop()

testing_fn('model_1_results.txt', 'answers.txt', 'testing_results_model_1.txt', 100)