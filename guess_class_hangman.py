class Guess():
    def __init__ (self, letter:str):
        self.letter = letter
        self.correctness = False 

    def check_correctness(self, letter):
        if letter in word:
            self.correctness = True 
            print('indeed, that letter is correct.')
        else: 
            print('nope, that was a dud.')