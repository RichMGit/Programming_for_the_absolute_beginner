import random
# # Hangman
#
# word_list = ['python', 'java', 'perl', 'ruby', 'haskell']
# chosen_word = random.choice(word_list)
# chosen_word_array = []
# already_guessed = []
# print(chosen_word)
#
# for letter in chosen_word:
#     print('_', end= "")
# print('\n')
#
# letter_guessed = input('Guess a letter: ')
#
# if letter_guessed in already_guessed:
#     print("Chose a letter not already guessed")
# correct_letters = []
# lives = 5
#
# while lives > 0:
#     if letter_guessed in already_guessed:
#         print("Chose a letter not already guessed")
#         letter_guessed = input('Guess a letter: ')
#     else:
#         if letter_guessed in chosen_word:
#             print('letter in word')
#             correct_letters.append(letter_guessed)
#             already_guessed.append(letter_guessed)
#             letter_guessed = input('Guess a letter: ')
#         else:
#             print('letter not in word')
#             lives -= 1
#             letter_guessed = input('Guess a letter: ')
#             already_guessed.append(letter_guessed)
# print('Game over')
# print(correct_letters)
#
# for i in chosen_word:
#     chosen_word_array.append(i)
# print(chosen_word_array)


# PART 1

# word_list = ['python', 'java', 'haskell', 'perl', 'ruby']
#
# random.shuffle(word_list)
# print(word_list)
#
# for i in word_list:
#     print(i)

# PART 2

# points = 30
#
# attributes = {'strength' : 0, 'health' : 0, 'wisdom' : 0, 'dexterity' : 0}
#
# print('You have 30 points to spend on 4 attributes')
#
# while points > 0:
#     print('''
#     0 - Quit
#     1 - Spend points
#     2 - Remove points
#     3 - Show remaining points
#     ''')
#     list_choice = int(input('What would you like to do? '))
#     if list_choice == 0:
#         print('Goodbye')
#         break
#     elif list_choice == 1:
#         print(attributes)
#         choose_attribute = input('Choose an attribute: ')
#         points_allocated = int(input('How many points do you want to spend on this? '))
#         if points - points_allocated < 0:
#             print('You do not have enough points for that')
#         else:
#             if choose_attribute in attributes:
#                 attributes[choose_attribute] = points_allocated + attributes[choose_attribute]
#                 points = points - points_allocated
#                 print(attributes)
#             else:
#                 print('term does not exist')
#                 choose_attribute = input('Choose an attribute: ')
#                 print(attributes)
#     elif list_choice == 2:
#         choose_attribute = input('Choose an attribute: ')
#         if choose_attribute in attributes:
#             remove_points = int(input('How many points would you like to remove? '))
#             if attributes[choose_attribute] - remove_points < 0:
#                 print('You cant remove this many points')
#             else:
#                 attributes[choose_attribute] = attributes[choose_attribute] - remove_points
#                 points = points + remove_points
#             print(attributes)
#     elif list_choice == 3:
#         print('You have ' + str(points) + ' left')
#     else:
#         print('invalid choice')

# PART 3

# son_father = {'Henry the 8th' : 'Henry the 7th', 'Romeo Beckham' : 'David Beckham', 'Terry Owen' : 'Michael Owen'}
#
# daddy_name = input('Enter a name of a male: ')
#
# print(daddy_name + ' is the son of ' + son_father[daddy_name])
