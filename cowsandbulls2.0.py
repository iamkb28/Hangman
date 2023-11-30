import random
    
def load_words(difficulty: int) -> list[str]:
    filenames = ["","words_list/4.words.txt", "words_list/5.words.txt", "words_list/6.words.txt"]
    return [line.strip() for line in open(filenames[difficulty])]

def start_word(difficulty: int):
    best_starts = [[], ['TRIP', 'SEAT', 'CAST'], ['PLANK', 'CRUST', 'CHOMP', 'FLESH', 'GRIND'], ['STRAIN', 'PLANES', 'TABLET']]
    return random.choice(best_starts[difficulty])

def common_letters(word1: str, word2: str) -> int:
    count = 0
    for letter in set(word1):
        if letter in word2:
            count += 1
    return count

def select(num: int, word1: str, word2: str) -> bool:
    return common_letters(word1, word2) == num

def filter_words(words: list[str], word: str, common_letters: int) -> list[str]:
    return list(filter(lambda x: select(common_letters, word, x), words ))

def has_unique_letters(word: str) -> bool:
    return all([word.count(char) == 1 for char in word])

def computer_word(words: list[str]) -> str :
    return random.choice([word for word in words if has_unique_letters(word)])

def isvalid_input(word: str, length: int) -> bool:
    return len(word) == length and word.isalpha()

def game():
    print ("Chose a Game Mode: \n1)Easy\n2)Medium\n3)Difficult\n")
    choice = int(input())
    words = load_words(choice)
    player = random.choice([1,2])
    secret_word = computer_word(words)
    comp_guess = start_word(choice)
    num_of_letters = choice + 3
    while True:
        if player == 1:
            user_guess = input("Your turn: ").upper()
            while(not isvalid_input(user_guess, num_of_letters)):
                user_guess = input("Enter valid guess: ").upper()
            print(common_letters(user_guess, secret_word))
            if user_guess == secret_word :
                return "Correct Guess\nUser Wins!"
            player = 2
    
        if player == 2:
            print("Computer's turn :\n" + comp_guess)
            com_let = int(input())
            words = filter_words(words, comp_guess, com_let)
            if com_let == num_of_letters:
                ask = input("Is this the right word?(Y/n): ")
                if ask.lower() == 'y':
                    print("Correct Guess\nComputer Wins!")
                    return "The computer's word was " + secret_word
                else:
                    words.remove(comp_guess)
            player = 1
            comp_guess = computer_word(words)
        
print(game())


    
