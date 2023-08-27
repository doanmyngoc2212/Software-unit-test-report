import random


class GuessNumberGame():

    # Create a random four-digit number to start the game.
    # Output: Integer: The new random number
    def getNewNumber(self):
        newNumber = random.randint(1000, 9999)
        return newNumber

    # Check if the input number valid or not
    # Input: String: Input Number to Guess
    # Output: Boolean: True/False
    def checkValidGuess(self, guessNumberStr):
        if len(guessNumberStr) == 4 and guessNumberStr.isdigit():
            return True
        else:
            return False

    # Compare the input number with the answer
    # Giving hint base on the rules
    # Assume the input guessing number is valid
    # Input: 2 Strings of Input Guessing Number and correct Number
    # Output: String of Hint
    def giveHint(self, guessNumberStr, correctNumberStr):
        hint = ""
        for i in range(4):
            if guessNumberStr[i] == correctNumberStr[i]:
                hint += "O"
            elif guessNumberStr[i] in correctNumberStr:
                hint += "X"
            else:
                hint += "_"
        return hint
    
    # This function run the game
    def runTheGame(self):
        correctNumberStr = str(self.getNewNumber())
        guessCount = 0
        while True:
            guessNumberStr = input("Enter a 4-digit number to guess or enter 0 to quit: ")
            if guessNumberStr == "0":
                break
            if self.checkValidGuess(guessNumberStr):
                guessCount += 1
                if guessNumberStr == correctNumberStr:
                    print("CORRECT! Number of guesses:", guessCount)
                    correctNumberStr = str(self.getNewNumber())
                    guessCount = 0
                else:
                    print("WRONG! Number of guesses:", guessCount)
                    print("Hint:", self.giveHint(correctNumberStr, guessNumberStr))
            else:
                print("Invalid input")        
        print("Thanks for playing!")


if __name__ == '__main__':
    game = GuessNumberGame()
    game.runTheGame()
