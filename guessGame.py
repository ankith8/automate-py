# This is the Guesss the number game
import random
print('Hello ! What is your name?')
name = input()
secretNumber = random.randint(1,20)
print("Well, "+name+", I'm thinking of a number between 1 and 20.")
print('But you have only 6 attempts')
for guesstaken in range(1,7):
   print('Take a Guess.')
   guess = int(input())
   if guess < secretNumber:
        print('Your guess is too low')
   elif guess > secretNumber :
        print('Your guess is too high')
   else:
        break # This is a corrent guess!
if guess == secretNumber:
    print('good job!')
    print('You took '+ str(guesstaken)+" guesses.")
else:
    print('Nope the number I was thinking of was '+str(secretNumber))
