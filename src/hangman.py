import os
from random import randint

class HangManGame:

    def __init__(self, word_file_rel_path: str =  os.path.join('..', 'resources/words.txt')):
        self._word = ''
        self._round = 0
        self._word_file_rel_path = word_file_rel_path
        self._end_game = False
        self.guesses = []
        self.current_guess = ''
        self.current_total_guess = ''
        
    def _get_random_word(self):
        file_path = os.path.join(os.path.dirname(__file__), self._word_file_rel_path)
        with open(file_path) as file:
            words = file.readlines()
        
        words = [word.strip('\n') for word in words]
        random_slice = randint(0,len(words)-1)
        self._word = words[random_slice]

    def _print_blank_word(self):
        self.current_total_guess = '_' * len(self._word)
        print(f"{self.current_total_guess.upper()}")
        
    def _check_guess_is_character(self):
        if not self.current_guess.isalpha():
            raise ValueError('Guess must be a character')
        
    def _guess_is_letter(self):
        if len(self.current_guess) == 1:
            return True
        else:
            return False
        
    def _guess_is_word(self):
        if len(self.current_guess) > 1:
            return True
        else:
            return False
        
    def _get_guess(self):
        self.current_guess = input("Make your next guess: ").lower()

    def _check_if_already_guessed(self):
        if len(set(self.guesses)) != len(self.guesses):
            print("You have already guessed this")
            self.guesses.pop()
            self._round -= 1

    def _make_new_current_total_guess(self):
        char_positions = [pos for pos, char in enumerate(self._word) if char == self.current_guess]
        for pos in char_positions:
            self.current_total_guess = self.current_total_guess[:pos] + str(self.current_guess) + self.current_total_guess[pos+1:]
        
    def _check_if_new_guess_wins(self):
        if self.current_total_guess == self._word:
            print(f'You win! Word: {self.current_total_guess.upper()}')
            self._end_game = True
        else:
            print(f"{self.current_total_guess.upper()}")

    def _make_guess_with_letter(self):
        self.guesses.append(self.current_guess)
        self._check_if_already_guessed()
        if self.current_guess in self._word:
            self._make_new_current_total_guess()
            self._check_if_new_guess_wins()
        else:
             print(f'{self.current_total_guess.upper()}')

    def _make_guess_with_word(self):
        if self._word == self.current_guess:
                print(f"You win! Word: {self.current_guess.upper()}")
        else:
                print("Game has ended")
        self._end_game = True

    def _do_a_round(self):
        self._get_guess()
        self._check_guess_is_character()
        if self._guess_is_word():
            self._make_guess_with_word()
        elif self._guess_is_letter():
            self._make_guess_with_letter()
            
    def run(self):
        self._get_random_word()
        self._print_blank_word()
        while self._round <= 12 and not self._end_game:
            self._do_a_round()
            self._round += 1
        if self._round > 12:
            print("Game has ended, exceeded round limit of 12.")

if __name__ == '__main__':

    game = HangManGame()
    game.run()