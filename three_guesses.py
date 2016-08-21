from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3

while guesses_left != 0:
    print "Guesses left: ", guesses_left
    guess = int(raw_input("Your guess: "))
    print "The random number is: ", random_number
    guesses_left -= 1
    if guess == random_number:
        print "You win!"
        break
else:
    print "You lose."
