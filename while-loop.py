import random;

number = random.randint(1,10);
is_guess_right = False;

print("Welcome to Guess the Number!");
print("The rules are simple. I will think of a number, and you will try to guess it.");
print(number);

while is_guess_right != True:
    guess = input("Guess a number between 1 and 10: ");
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess));
        is_guess_right = True;
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess));