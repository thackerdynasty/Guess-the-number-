from main import *
print("Well,", name, ", I am thinking of a number between 1 and 20.")
def game():
	global Guesses
	answer = int(input("Can you guess it? "))
	if answer < number:
		print("Your guess is too low.")
		Guesses += 1
		game()
	elif answer > number:
		print("Your guess is too high.")
		Guesses += 1
		game()
	else:
		if answer == number:
			Guesses += 1
			print("Congratulations! You guessed the number in", Guesses, "Guesses!")
game()
#jfieefwewf
