import os
import random

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'random_words.txt')
output = {}
#choice = ''
def choice_of_word():
    with open(filename,'r') as rw_list:
        lines = rw_list.readlines()
        choice = random.choice(lines)
        return choice

def store_word_in_dict():
    letter_dict = {}
    count = 0
    to_hide = choice_of_word()
    for letter in to_hide[:-1]:
        letter_dict[count] = letter
        count += 1
    return letter_dict

# print(store_word_in_dict())

def check_user_input(guess):
    count = 0
    correct_guess = {}
    wrong_guess = 0
    stored_values = []
    for entry in store_word_in_dict().values():
        stored_values.append(entry)
        if guess == entry:
            correct_guess[count] = guess 
        # else:
        #     wrong_guess += 1
        count += 1
    return correct_guess, count, stored_values

#print(check_user_input('e'))

# def hide_word(guess):
#     fcall = check_user_input(guess)
#     count = fcall[1]
#     correct_guess = fcall[0]
#     corr_g_key = list(fcall[0].keys())
#     corr_g_value = list(fcall[0].values())
#     letter_list = fcall[2]
#     output = []
#     counter = 0
#     if len(correct_guess) > 0: 
#         print(corr_g_key[0], corr_g_value[0])
#         for entry in letter_list:
#             if corr_g_key[0] == counter:
#                 output.append(corr_g_value[0])
#             else:
#                 output.append(' _ ')
#             counter += 1 
#     else: 
#         print('no luck, this guess was wrong')
#     return letter_list, output, corr_g_key

# print(hide_word('e'))

def hide_word(guess):
    fcall = check_user_input(guess)
    count = fcall[1]
    correct_guess = fcall[0]
    corr_g_key = list(fcall[0].keys())
    corr_g_value = list(fcall[0].values())
    letter_list = fcall[2]
    counter = 0
    if len(correct_guess) > 0: 
        print(correct_guess)
        #print(corr_g_key[0], corr_g_value[0])
        for entry in letter_list:
            if corr_g_key[0] == counter:
                output[counter] = corr_g_value[0]
            elif counter not in output:
                output[counter] = ' _ '
            counter += 1 
    else:
        print('no luck, this guess was wrong')
    
print(hide_word('e'), hide_word('a'), hide_word('o'))

print(output)