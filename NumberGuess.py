"""

This program will allow a user to guess a number that the dice will roll. 
If they guess higher than the dice, they'll get a message to tell them they've won.
If its lower than the dice roll, they'll lose.

"""

from random import randint

from time import sleep

def get_user_guess():
  guess = int(input("Guess a number.... "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
  	print ("This value is higher than the value allowed")
  else:
    print ("Rolling...")
    sleep(2)
    print ("The first roll is: %d" % first_roll)
    sleep(1)
    print ("The second roll is: %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print ("The result is....")
    sleep(1)
    if guess > total_roll:
      print ("You've won!")
    else:
        print ("Sorry, you lost")

roll_dice(6)
