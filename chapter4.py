import random
# # PART 1
#
# number = int(input('Enter a starting number: '))
# count_to = int(input('Enter an ending number: '))
# count_by = int(input('Enter a jumping number: '))
#
#
# print('starting number', str(number))
# print('ending number', str(count_to))
# print('count by number', str(count_by))
#
# for i in range(number, count_to + 1, count_by):
#     print(i)

# PART 2

# message = input('Enter a string: ')
#
# new_message = ''
# index = len(message) - 1
#
# print(message)
# print(new_message)
# print(index)
# for i in message:
#     new_message += message[index]
#     index -= 1
#
# print(new_message)

# PART 3

# word_list = ['python', 'java', 'haskell', 'perl',  'ruby']
# score = 0
#
# while len(word_list):
#     chosen_word = random.choice(word_list)
#     initial_word = chosen_word
#     jumble = ''
#
#     while chosen_word:
#         position = random.randrange(len(chosen_word))
#         jumble += chosen_word[position]
#         chosen_word = chosen_word[:position] + chosen_word[(position + 1):]
#     print(jumble)
#     guess = input('What is your guess? ')
#     clue_used = False
#
#     while guess != initial_word:
#         print('nope, here is a clue. it begins with: ', initial_word[0])
#         guess = input('What is your guess? ')
#         clue_used = True
#
#     word_list.remove(initial_word)
#
#     print('you got it right')
#     if not clue_used:
#         score += 1
#
#     print(score)

# PART 4

word_list = ['banana', 'apple', 'pear', 'grape', 'tomato', 'turnip']
chosen_word = random.choice(word_list)
#print(chosen_word)
print('im thinking of a word, it has ' + str(len(chosen_word)) + ' letters')
letter = input('you may ask me if a particular letter is in a word: ')
guesses = 5

word = ''
while guesses > 0:
    if letter not in chosen_word:
        print('no, letter not in word')
        letter = input('guess another letter ')
        guesses -= 1
    else:
        print('yes, letter in word')
        word = input('what is the word? ')
        break
if word == chosen_word:
    print('well done, you got it')
else:
    print('you really are a dumbass')
