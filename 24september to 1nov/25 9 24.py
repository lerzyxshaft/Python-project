from random import randint

class RunGame:
    def __init__(self):
        random_number = randint(1, 100)
        quest = int(input("Guess number between 1 and 100: "))
        while True:
            if quest == random_number:
                print("yeah you guessed it, congrats")
                break
            elif quest > random_number:
                print("Too high, try one more time")
                quest = int(input("Guess again: "))
            elif quest < random_number:
                print("Too low try one more time")
                quest = int(input("Guess again: "))

app = RunGame()
