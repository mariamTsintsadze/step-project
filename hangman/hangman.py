import random

hangman_graphics = [
    '''
     _______
    |/      |
    |      
    |     
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |     
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       |
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       |
    |      / 
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       |
    |      / \ 
    |     
    |______|
    '''
]

def display_hangman(tries):
    print(hangman_graphics[6 - tries])  

#თამაშის დონეები
easy_words = ['cat', 'dog', 'fish', 'bird']
medium_words = ['apple', 'banana', 'cherry', 'grape']
hard_words = ['pineapple', 'watermelon', 'strawberry', 'blueberry']

#ვირჩევთ დონეს
def choose_difficulty():
    print("Choose Difficulty Level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")


difficulty = choose_difficulty()
#რენდომულად გვანიჭებს ცდების რაოდენობას თითოეულ დონეზე
if difficulty == 1:
    words = easy_words
    number_of_tries = random.randint(8, 10)
elif difficulty == 2:
    words = medium_words
    number_of_tries = random.randint(5, 8)
else:
    words = hard_words
    number_of_tries = random.randint(3, 5)

#სიტყვას მოცემული სირთულის ლისტიდან რენდომულად ვირჩევთ
chosen_word = words[random.randint(0, len(words)-1)]

#ჩაფიქრებული სიტყვა ტირეებით ისახება
hidden_word = ['_'] * len(chosen_word)
wrong_guesses = []
correct_guesses = []
guesses = 0

while number_of_tries > 0 and '_'  in hidden_word:
    print(' '.join(hidden_word)) # gamosaxuleb defisebit
    print(f'{number_of_tries} tries left:')
    print(f'Incorrect guesses: {", ".join(wrong_guesses)}')

    #6 ცდიდად იწყება ჰენგმენის დახატვა
    if number_of_tries <= 6:
        display_hangman(number_of_tries)

    try:
        guess = input("Enter the letter or word: ").lower()
        print()

        #მოწმდება ერთი ასო შეყავს თუ მტელი სიტყვა
        if (len(guess) != 1 and len(guess) != len(chosen_word)) or not guess.isalpha():
            raise ValueError("Please enter a valid single letter.")
        

        if guess in correct_guesses or guess in wrong_guesses:
            print("you already guessed that letter.")
            continue
        
        if guess == chosen_word:
            correct_guesses.append(guess)
            guesses += 1
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess[i]:
                    hidden_word[i] = guess[i]
        elif guess in chosen_word:
            correct_guesses.append(guess)
            guesses += 1
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    hidden_word[i] = guess
        else:
            number_of_tries -= 1
            #არასწორ მცდელობებს ინახავს 
            wrong_guesses.append(guess)
            print(f"Wrong guess! Tries left: {number_of_tries}")

    except ValueError as e:
        print(e)
        continue

if '_' not in hidden_word:
    print(f"Congratulations! you guessed the word {chosen_word}")
    print(f"You guessed the word in {guesses} tries.")
else:
    print(f"Game Over! The word was: {chosen_word}")




