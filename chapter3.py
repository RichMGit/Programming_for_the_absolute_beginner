import random

die_one = random.randrange(6)+1
die_two = random.randrange(6)+1

print(die_one)
print(die_two)
print(die_one + die_two)

number = random.randint(1,3)
print(number)

if number == 1:
    print('number 1')
elif number == 2:
    print('number 2')
else:
    print('number 3')

digit = int(input('Enter a number: '))

while digit >= 4:
    print('number not less than 4')
    digit = int(input('Enter a number: '))
print(str(digit) + ' is less than 4')

# part 2
import random
heads = 0
tails = 0

flip_coin = ['heads', 'tails']

while (heads + tails) < 100:
    flip = random.choice(flip_coin)
    if flip == 'heads':
        heads += 1
    else:
        tails += 1
print(heads)
print(tails)


# part 3

guesses = 5

print('You have 5 guesses, make them count')



chosen_number = random.randint(0, 100)
print(chosen_number)
while guesses > 0:

    guess = int(input('What is your guess? '))
    if guess > chosen_number:
        print('Too high')
        guesses -= 1
    elif guess < chosen_number:
        print('Too low')
        guesses -= 1
    else:
        print('OMG you got it right!!')
        break
