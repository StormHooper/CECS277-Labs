# Name: Tyler Pham and Matthew Samar
# Date: 22 August 2023
# Description: Guessing Game. Program generates a random number (unknown to the user) and asks the user to guess the number. The program tells the user 'Too high' or 'Too low' until the user guesses the number.
import random
import check_input


def main():
  print("- Guessing Game -")
  num = random.randint(1, 100)
  guess = check_input.get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
  tries = 1

  while guess != num:
    if guess > num:
      print("Too high!", end=' ')
    else:
      print("Too low!", end=' ')
    guess = check_input.get_int_range("Guess again (1-100): ", 1, 100)
    tries += 1

  if tries > 1:
    print("Correct! You got it in " + str(tries) + " tries.")
  else:
    print("Correct! You got it in " + str(tries) + " try.")


main()
