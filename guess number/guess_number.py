import random

def random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def play_game(min_number, max_number):
    random_num = random_number(min_number, max_number)  
    attempts = []  
    guess = None

    print(f"Guess the number between {min_number} and {max_number}!")

    while guess != random_num:
        try:
            guess = int(input("Enter your guess: "))
            attempts.append(guess) 
             
            #მოცემულ ზღვარს ცდება თუ არა
            if not min_number <= guess <= max_number:
                print("Number out of range!")

            #მინიშნებების მიწოდება
            if guess < random_num:
                print("Enter a larger number.")
            elif guess > random_num:
                print("Enter a smaller number.")
            else:
                print(f"Congrats! You guessed the number {random_num} correctly in {len(attempts)} attempts.")
                print(f"Your attempts were: {attempts}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    #ქვედა ზღვარის შეყვანა
    while True:
        try:
            min_number = int(input("Enter a minimum number: "))
            break
        except ValueError:
            print("Invalid input for minimum number. Please enter a valid number.")

    # ზედა ზღვარი შეყვანა
    while True:
        try:
            max_number = int(input("Enter a maximum number: "))
            if max_number > min_number:
                break
            else:
                print("Maximum number must be greater than the minimum number.")
        except ValueError:
            print("Invalid input for maximum number. Please enter a valid number.")

    # თამაშის დაწყება
    play_game(min_number, max_number)

    # სურს თუ არა გაგრძელება
    continue_game = input("Do you want to continue the game? (yes/no): ").strip().lower()
    if continue_game != "yes":
        print("Thanks for playing! Goodbye!")
        break
