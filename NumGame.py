import random
correct_number = random.randint(0, 100)
attempt = 0

print("ONE to HUNDRED")
print("Guess the Number")
print()

while True:
  guess_input = input("What is your guess? (Enter a negative number to quit): ")

  if float(guess_input) < 0:
    print("Game has stopped. Better luck next time!")
    break

  if guess_input.isdigit():
    guess_number = int(guess_input)
  else:
    print("Please enter a valid number.")
    continue

  attempt += 1

  if guess_number > correct_number:
    print("Too high!")
  elif guess_number < correct_number:
    print("Too low!")
  else:
    print("Congratulations! You win!")
    print("It took you", attempt, "attempts.")
    break

print(f"Number of attempts: {attempt}")
print("Thanks to @yanagalenko154 for coding help")