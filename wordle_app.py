#A wordle application that uses the same dictionary as the New York Times online game 'Wordle'
#DATA FROM EACH ROUND IS STORED IN:
# 1.) ALL guesses is 'guesses_data.txt'
#     -> a list of guesses per round is 'guesses_per_round.txt'
# 2.) number of guesses to solve is 'num_guesses_data.txt
# 3.) number of times they guessed each letter is 'letters_guessed_per_round.txt'
#**These lists (guesses_per_round, num_guesses_data, letters_guessed_per_round)
#   will include the same number of indexes because each round adds a line to each list 
#   so can be copy/pasted side by side and each row will correspond to a round

import random
from random import randint

#import the wordle dictionary & convert to a list
dictFile = open('dictionary.txt').read().splitlines()
answersFile = open('answers.txt').read().splitlines()

wordleDictionary = []
for word in dictFile:
    word = str(word)
    wordleDictionary.append(word.lower())

possible_solutions = []
for word in answersFile:
    word = str(word)
    possible_solutions.append(word.lower())

#display a welcome message & wait for yes/no from user, respond accordingly
print('\n\n\n' + open('welcome_message.txt').read())
print('\n' + open('instructions.txt').read())

#initialize all the needed variables
numTimesPlayed = 0
guesses = []
guessed_already_lol = []
numGuesses = 0
solution = possible_solutions[randint(0, len(possible_solutions) - 1)]
guessed_correct_letters = ['_','_','_','_','_']
solution_letters = []
remaining_letters1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
remaining_letters2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
remaining_letters3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

k=0
while k <= 4:
   solution_letters.append(solution[k])
   k+=1

#check_ready(string)
#function to check if the user replied with yes or no to a previous statement
#if no, quits the program
def check_ready(resp):
    if resp == 'yes':
        if numTimesPlayed == 0:
            print('Great! Here we go.')  
            initialize()
        else: 
            print(f'Great! Here we go for round {numTimesPlayed + 1}.')
            save()
            reset()
            initialize()

    elif resp == 'no':
         print('Sorry to see you go!')
         save()
         quit()
    else: 
        print('Please say yes or no.')
        check_ready(input().lower())

#wrong_guess(string)
#performs all the actions that update data when the user makes an incorrect guess
def wrong_guess(guess):
    global guessed_correct_letters
    global solution
    global solution_letters
    global numGuesses

    guessed_letters = []

    #create a list of the letters of the word that the player guessed
    j = 0
    while j <= len(guess) - 1:
        guessed_letters.append(guess[j])
        j+=1
   
    #temp variable to save in guessed_lol at the end w/o changing guessed_letters
    guessed_letters_temp = guessed_letters
    
    #check if/where the letters are in the solution and update variables accordingly
    i = 0
    while i <= len(guessed_letters) - 1:
        this_letter = guessed_letters[i]
        
        #if this_letter is at the exact spot in solution_letters 
        # -> make guessed_correct_letters & guessed_letters_temp reflect this
        if this_letter == solution_letters[i]:
            guessed_letters_temp[i] = this_letter
            guessed_correct_letters[i] = solution_letters[i]
            
            # {nested within if this_letter is at the exact spot in solution_letters} 
            # if guessed_correct_letters already includes this_letter with '*'
            # -> reset this index in guessed_correct_letters to '_'
            if this_letter + '*' in guessed_correct_letters:
                guessed_correct_letters[guessed_correct_letters.index(solution_letters[i] + '*')] = '_'
                
        #else if this_letter is not at the right spot in solution_letters BUT it is in solution_letters at a different index
        # -> add this_letter with '*' to the right index in guessed_correct_letters
        # -> add this_letter with '*' to the right index in guessed_letters_temp          
        elif this_letter != solution_letters[i] and this_letter in solution_letters:
            guessed_letters_temp[i] = this_letter + '*'
            
            if this_letter + '*' in guessed_correct_letters and guessed_correct_letters[i] != f'{this_letter}*':
                rem = guessed_correct_letters.index(this_letter + '*')
                guessed_correct_letters[rem] = '_'
            if not this_letter in guessed_correct_letters: 
                guessed_correct_letters[i] = this_letter + '*'
        
        #else if this_letter is not in solution letters at all
        # -> update the remaining letters lists and remove this_letter from whichever list it is in (if at all)   
        # -> make guessed_letters_temp reflect this    
        elif not this_letter in solution_letters: 
                guessed_letters_temp[i] = f'/{this_letter}/'
                #update this index of guessed_correct_letters to be blank if there isnt a correct letter there already
                if guessed_correct_letters[i] == '_' or '*' in guessed_correct_letters[i]:
                    guessed_correct_letters[i] = '_'
                    
                #if the incorrect letter is in the first list of remaining letters
                if this_letter in remaining_letters1:
                    index = remaining_letters1.index(this_letter)
                    remaining_letters1[index] = '_'
                #if it's in the second list 
                elif this_letter in remaining_letters2:
                    index = remaining_letters2.index(this_letter)
                    remaining_letters2[index] = '_'
                #if its in the third list
                elif this_letter in remaining_letters3:
                    index = remaining_letters3.index(this_letter)
                    remaining_letters3[index] = '_'    
        i+=1
        
        
    def prnt(lst):
        n = 1
        print('\nGuessed already:')
        for g in lst:
            print(f'{n}. {g}')
            n+=1
            
    #prompt next guess
    if numGuesses <= 5:
        print(f'\n----------+----------\nIncorrect :( \n{6 - numGuesses} guesses remaining!\n')
    elif numGuesses == 6:
        numGuesses += 1
        print(f'\n----------+----------\nAll guesses used! The answer was: {solution}. \n----------+----------\n\nDo you want to play again?')
        check_ready(input().lower())
        
    #add guessed_letters_temp to guessed_already_lol
    guessed_already_lol.append(guessed_letters_temp)
    
    #output
    prnt(guessed_already_lol)
    print(f'\nRemaining letters: \n{remaining_letters1}\n  {remaining_letters2}\n     {remaining_letters3}')
    print('\n\nKnown: ' + format(guessed_correct_letters) + '\n----------+----------\n')
    
    capture_guess(input().lower())
    
    

def check_guess(guess):
    global solution 
    global numGuesses

    numGuesses += 1

    if guess.lower() == solution:
        print(f'\nCongratulations! The word was {solution}\n' + 'Do you want to play again?')
        check_ready(input().lower())

    else: return False

def capture_guess(guess):
    global guesses

    if len(guess) != 5:
        print('Incorrect number of letters! Try again with 5 letters.')
        capture_guess(input().lower())

    if guess not in wordleDictionary:
        print('Word not recognized. Please try another word.')
        capture_guess(input().lower())

    guesses.append(guess.lower())

    if not check_guess(guess):
        wrong_guess(guess)

def initialize():
    global numTimesPlayed
    
    numTimesPlayed += 1
    print('Choosing a word ...')
    print('Alright, take your best guess!')
    capture_guess(input().lower())

def reset():
    global guesses
    global numGuesses
    global solution
    global solution_letters
    global guessed_correct_letters
    global remaining_letters1
    global remaining_letters2
    global remaining_letters3
    global guessed_already_lol
    
    guesses = []
    numGuesses = 0
    solution = possible_solutions[randint(0, len(possible_solutions) - 1)]
    guessed_correct_letters = ['_','_','_','_','_']
    guessed_already_lol = []
    solution_letters = []
    remaining_letters1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    remaining_letters2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    remaining_letters3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    #create a list that holds each letter of the solution
    solution_letters = []
    k=0
    while k <= 4:
       solution_letters.append(solution[k])
       k+=1

def save():
    global guesses
    
    lol = []
    list_of_guesses_file = open("guesses_data.txt", "a")
    guesses_per_round_file = open("guesses_per_round.txt", "a")
    for g in guesses:
        list_of_guesses_file.write(f'\n{g}')
        guesses_per_round_file.write(f'{g} ')
        for l in g:
            lol.append(l)
    
    num_guesses_file = open("num_guesses_data.txt", "a")
    if numGuesses <=6:
        num_guesses_file.write(f'\n{numGuesses}')
    else: num_guesses_file.write('\nX')
    
    list_of_letters_file = open("letters_guessed_per_round.txt", "a")
    list_of_letters_file.write('\n')
    for l in lol:
        list_of_letters_file.write(f'{l} ')
    
if numTimesPlayed == 0:
    check_ready(input().lower())




