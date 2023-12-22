from typing import Tuple

# En utilisant la méthode du test-driven development, écrire une classe qui permet de jouer au tic-tac-toe.
# La classe doit permettre de:
# 1. Au joueur X de jouer
# 2. Au joueur O de jouer
# 3. De savoir si la partie est terminée.
# 4. De savoir qui à gagné la partie.


class TicTacToe:

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.playerX = -1
        self.playerO = 1
        self.final_score = 3

    def play_x(self, position: Tuple[int, int]):
        x = position[0]
        y = position[1]
        if self.board[x][y] == 0:
            self.board[x][y] = self.playerX
            return True
        return False

    def play_o(self, position: Tuple[int, int]):
        x = position[0]
        y = position[1]
        if self.board[x][y] == 0:
            self.board[x][y] = self.playerO
            return True
        return False

    def win_match(self):
        for horizontal in range(0, 3):
            score = 0
            for line in range(0, 3):
                score += self.board[horizontal][line]
            if score == self.final_score or abs(score) == self.final_score:
                return score
        for vertical in range(0, 3):
            score = 0
            for column in range(0, 3):
                score += self.board[vertical][column]
            if score == 3 or abs(score) == 3:
                return score
        score = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if score == 3 or abs(score) == 3:
            return score
        score = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if score == 3 or abs(score) == 3:
            return score
        for x in range(0, 3):
            for y in range(0, 3):
                if self.board[x][y] == 0:
                    return self.final_score + 1
        return score

    def end_match(self):
        score = self.win_match()
        if score == self.final_score:
            return "Joueur O a gagné"
        if score == self.final_score * -1:
            return "Joueur X a gagné"
        if score == self.final_score + 1:
            return "Partie nulle"
        return "Terminez la partie"

