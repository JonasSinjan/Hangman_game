import pytest
import os
from ..src.hangman import HangManGame

def test_random_word():
    relative_path_test = os.path.join('..', 'tests', 'exam', 'testwords.txt')
    game = HangManGame(word_file_rel_path=relative_path_test)
    game._get_random_word()
    assert game._word in ['testone', 'testtwo', 'testthree']
    assert game.current_total_guess == '_' * len(game._word)

def test_error_if_guess_not_a_character(mocker):
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 'b*')
    game._get_guess()
    with pytest.raises(RuntimeError):
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
    assert printer.called_with('Game has ended')

def test_game_round_duplicate_letter(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    mocker.patch('builtins.input', return_value = 't')
    game._do_a_round()
    mocker.patch('builtins.input', return_value = 'T')
    game._do_a_round()
    assert printer.called_with('You have already guessed this')
    assert game.guesses == ['t']

def test_game_round_letter_print(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    game.word = 'testthree'
    mocker.patch('builtins.input', return_value = 't')
    game._do_a_round()
    #assert printer.called_with('Your guessed letter is in the word!')
    assert printer.called_with('t__tt____')
    mocker.patch('builtins.input', return_value = 'e')
    game._do_a_round()
    assert printer.called_with('te_tt__ee')
    mocker.patch('builtins.input', return_value = 'testthree')
    game._do_a_round()
    assert printer.called_with('You win!: testthree')

def test_incorrect_word_guess(mocker):
    printer = mocker.patch('builtins.print')
    game = HangManGame()
    game.word = 'testthree'
    mocker.patch('builtins.input', return_value = 'testtwo')
    game._do_a_round()
    #assert printer.called_with('Your guessed letter is in the word!')
    assert printer.called_with('Game has ended')

def test_run(mocker):
    printer = mocker.patch('builtins.print')
    mocker.patch('builtins.input', return_value = 'incorrectword')
    game = HangManGame()
    game.run()
    assert printer.called_with('Game has ended')

    