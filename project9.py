import random

def higher_lower_game():
    print("Welcome to the Higher or Lower Game!")
    print("Guess if the next number will be higher or lower.")
    
    current_number = random.randint(1, 100)
    print(f"Starting number: {current_number}")
    
    score = 0
    while True:
        guess = input("Will the next number be higher or lower? (h/l): ").lower()
        next_number = random.randint(1, 100)
        
        if guess == 'h' and next_number > current_number:
            print(f"Correct! The next number was {next_number}.")
            score += 1
        elif guess == 'l' and next_number < current_number:
            print(f"Correct! The next number was {next_number}.")
            score += 1
        else:
            print(f"Wrong! The next number was {next_number}.")
            break