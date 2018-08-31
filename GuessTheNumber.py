# Carlos Ortega
# Capstone Lab1
# GuessTheNumber Program
#08/30/18
import random
numberToGuess = random.randint(0, 20)


print("This is a guessing game");
print("Please enter a guess!");

PlayerGuess = input();
PlayerGuess = int(PlayerGuess);

if PlayerGuess == numberToGuess:
        print('Great Job')

elif PlayerGuess >= numberToGuess:
        print('Ups too high')
elif PlayerGuess < numberToGuess:
    print('Almost, too low')







