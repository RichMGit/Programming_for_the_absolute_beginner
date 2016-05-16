# Random Access
# Demonstrates string indexing

# import random
#
# word = "index"
# print("The word is: ", word, "\n")
#
# high = len(word)
# low = -len(word)
#
# for i in range(10):
#     position = random.randrange(low, high)
#     print("word[", position, "]\t", word[position])


# print('1 - Exit')
# print('2 - Show scores')
# print('3 - Add scores')
# print('4 - Delete scores')
# print('5 - High score')
#
# scores = []
#
# decision = int(input('Enter a number: '))
# playing = True
#
# while playing:
#     if decision == 1:
#         print('Goodbye')
#         playing = False
#     elif decision == 2:
#         print(scores)
#         decision = int(input('Enter a number: '))
#     elif decision == 3:
#         new_score = int(input('What was the score? '))
#         scores.append(new_score)
#         decision = int(input('Enter a number: '))
#     elif decision == 4:
#         score_to_go = int(input('What score shall we lose? '))
#         if score_to_go in scores:
#             scores.remove(score_to_go)
#             decision = int(input('Enter a number: '))
#
#         else:
#             print('score doesnt exist')
#             decision = int(input('Enter a number: '))
#
#     elif decision == 5:
#         print('HS:' )
#         print(max(scores))
#         decision = int(input('Enter a number: '))
#     else:
#         print('You did not enter a valid number')
#         decision = int(input('Enter a number: '))

#
# names_and_ages_list = [['Rich', 23], ['Paul', 45], ['Ron', 39], ['Simon', 101]]
# print(names_and_ages_list[0][1])

geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque" : "the collection of debris found in computer keyboards.",
        "Link Rot" : "the process by which web page links become obsolete.",
        "Percussive Maintenance" : "the act of striking an electronic device to make it work.",
        "Uninstalled" : "being fired.  Especially popular during the dot-bomb era."}
choice = None
while choice != "0":

    print(
    """
    Geek Translator

    0 - Quit
    1 - Look Up a Geek Term
    2 - Add a Geek Term
    3 - Redefine a Geek Term
    4 - Delete a Geek Term
    """
    )

    choice = input("Choice: ")
    # exit
    if choice == "0":
        print("Good-bye.")

    elif choice == "1":
            lol = input("What lol do you want me to translate?: ")
            if lol in geek:
                definition = geek[lol]
                print("\n", lol, "means", definition)
            else:
                print("\nSorry, I don't know", lol)

    elif choice == "2":
            lol = input("What lol do you want me to add?: ")
            if lol not in geek:
                definition = input("\nWhat's the definition?: ")
                geek[lol] = definition
                print("\n", lol, "has been added.")
            else:
                print("\nThat lol already exists!  Try redefining it.")
