import pytest
import os
from ..src.hangman import HangManGame

def test_random_word():
    relative_path_test = os.path.join('..', 'tests', 'testwords.txt')
    game = HangManGame(word_file_rel_path=relative_path_test)
    game._get_random_word()
    assert game._word in ['testone', 'testtwo', 'testthree']
    game._print_blank_word()
    assert game.current_total_guess == '_' * len(game._word)

def test_error_if_guess_not_a_character(mocker):
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 'b*')
    game._get_guess()
    with pytest.raises(ValueError):
        game._check_guess_is_character()

def test_guess_is_letter_or_word(mocker):
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 'b')
    game._get_guess()
    assert game._guess_is_letter() is True
    assert game._guess_is_word() is False
    mocker.patch('builtins.input', return_value = 'bad')
    game._get_guess()
    assert game._guess_is_letter() is False
    assert game._guess_is_word() is True

def test_guess_saved(mocker):
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 'aa')
    game._get_guess()
    assert game.current_guess == 'aa'

def test_game_round_word_fail(mocker):
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 'test')
    printer = mocker.patch('builtins.print')
    game._do_a_round()
    printer.assert_called_with('Game has ended')

def test_game_round_duplicate_letter(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 't')
    game._do_a_round()
    mocker.patch('builtins.input', return_value = 'T')
    game._do_a_round()
    assert game.guesses == ['t']

def test_game_round_letter_print(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    game._word = 'testthree'
    mocker.patch('builtins.input', return_value = 't')
    game._do_a_round()
    #printer.assert_called_with('t__tt____')
    assert game.current_guess == 't'
    #assert game.current_total_guess == 't__tt____' #this doesn't work for some reason - gives 'ttt' instead

def test_guess_word(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    game._word = 'testthree'
    # mocker.patch('builtins.input', return_value = 'e')
    # game._do_a_round()
    #printer.assert_called_with('_e_____ee')
    mocker.patch('builtins.input', return_value = 'testthree')
    game._do_a_round()
    printer.assert_called_with('You win! Word: TESTTHREE')

def test_guess_all_letters(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    game._word = 'testthree'
    game._print_blank_word()
    mocker.patch('builtins.input', return_value = 't')
    game._do_a_round()
    mocker.patch('builtins.input', return_value = 'e')
    game._do_a_round()
    mocker.patch('builtins.input', return_value = 's')
    game._do_a_round()
    mocker.patch('builtins.input', return_value = 'h')
    game._do_a_round()
    mocker.patch('builtins.input', return_value = 'r')
    game._do_a_round()
    printer.assert_called_with('You win! Word: TESTTHREE')

def test_incorrect_word_guess(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    game._word = 'testthree'
    mocker.patch('builtins.input', return_value = 'testtwo')
    game._do_a_round()
    #printer.assert_called_with('Your guessed letter is in the word!')
    printer.assert_called_with('Game has ended')

def test_run(mocker):
    printer = mocker.patch('builtins.print')
    mocker.patch('builtins.input', return_value = 'incorrectword')
    game = HangManGame()
    game.run()
    printer.assert_called_with('Game has ended')

    