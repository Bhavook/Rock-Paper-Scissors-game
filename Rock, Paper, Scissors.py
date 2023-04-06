import random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
         print("computer: ",computer)
         print("player: ",player)
         print("Tie!")
    elif player == "rock":
         if computer == "paper":
             print("computer: ", computer)
             print("player: ", player)
             print("you lose!")
         if computer == "scissors":
             print("computer: ", computer)
             print("player: ", player)
             print("you Win!")
    elif player == "scissors":
         if computer == "rock":
             print("computer: ", computer)
             print("player: ", player)
             print("you lose!")
         if computer == "paper":
             print("computer: ", computer)
             print("player: ", player)
             print("you Win!")
    elif player == "paper":
         if computer == "scissors":
             print("computer: ", computer)
             print("player: ", player)
             print("you lose!")
         if computer == "rock":
             print("computer: ", computer)
             print("player: ", player)
             print("you Win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")

def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("---------------")
        print(key)
        for i in options[questions_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key).guess)
        questions_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------")
    print("RESULTS")
    print("---------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions))) * 100
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
