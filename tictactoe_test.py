import pytest
from tictactoe import *


@pytest.fixture
def play_first():
    return 1, 1


@pytest.fixture
def play_second():
    return 1, 0


@pytest.fixture
def play_third():
    return 0, 0


@pytest.fixture
def play_fourth():
    return 2, 0


@pytest.fixture
def play_fifth():
    return 2, 2


# PLAYER X
def test_play_x_case_vide(play_first):
    board = TicTacToe()
    assert board.play_x(play_first) is True
    assert board.board[play_first[0]][play_first[1]] == -1


def test_play_x_case_o(play_first):
    board = TicTacToe()
    board.play_o(play_first)
    assert board.play_x(play_first) is False
    assert board.board[play_first[0]][play_first[1]] == 1


def test_play_x_case_x(play_first):
    board = TicTacToe()
    board.play_x(play_first)
    assert board.play_x(play_first) is False
    assert board.board[play_first[0]][play_first[1]] == -1


# PLAYER O
def test_play_o_case_vide(play_first):
    board = TicTacToe()
    assert board.play_o(play_first) is True
    assert board.board[play_first[0]][play_first[1]] == 1


def test_play_o_case_x(play_first):
    board = TicTacToe()
    board.play_x(play_first)
    assert board.play_o(play_first) is False
    assert board.board[play_first[0]][play_first[1]] == -1


def test_play_o_case_o(play_first):
    board = TicTacToe()
    board.play_o(play_first)
    assert board.play_o(play_first) is False
    assert board.board[play_first[0]][play_first[1]] == 1


# FIN DU MATCH
def test_win_match(play_first, play_second, play_third, play_fourth, play_fifth):
    board = TicTacToe()
    board.play_o(play_first)
    board.play_x(play_second)
    board.play_o(play_third)
    board.play_x(play_fourth)
    board.play_o(play_fifth)
    assert board.win_match() == 3


def test_end_match(play_first, play_second, play_third, play_fourth, play_fifth):
    board = TicTacToe()
    board.play_o(play_first)
    board.play_x(play_second)
    board.play_o(play_third)
    board.play_x(play_fourth)
    board.play_o(play_fifth)
    assert board.end_match() == "Joueur O a gagné"