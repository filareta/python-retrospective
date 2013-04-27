class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    TILES = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    MOVES = ('X', 'O')
    WINNER = (("A1", "A2", "A3"), ("B1", "B2", "B3"), ("C1", "C2", "C3"),
              ("A1", "B1", "C1"), ("A2", "B2", "C2"), ("A3", "B3", "C3"),
              ("A1", "B2", "C3"), ("A3", "B2", "C1"))

    def __init__(self):
        self.board = dict.fromkeys(self.TILES)
        self.winner = None
        self.current_move = None

    def set_players_turn(self, move):
        self.player1 = move
        if move == 'X':
            self.player2 = 'O'
        else:
            self.player2 = 'X'

    def __setitem__(self, key, value):
        if key not in self.TILES:
            raise InvalidKey
        if value not in self.MOVES:
            raise InvalidValue
        if self.board[key]:
            raise InvalidMove
        if self.current_move == value:
            raise NotYourTurn
        if not self.current_move:
            self.set_players_turn(value)
        self.current_move = value
        self.board[key] = value

    def __getitem__(self, key):
        if key in self.TILES:
            return self.board[key]

    def search_winner(self, move):
        for triple in self.WINNER:
            if all([self.board[tile] == move for tile in triple]):
                self.winner = move

    def game_status(self):
        self.search_winner(self.player1)
        if self.winner:
            return "{} wins!".format(self.player1)
        self.search_winner(self.player2)
        if self.winner:
            return "{} wins!".format(self.player2)
        if None in self.board.values():
            return "Game in progress."
        else:
            return "Draw!"

    def __str__(self):
        for key in self.board:
            if not self.board[key]:
                self.board[key] = ' '
        return '''
  -------------
3 | {A3} | {B3} | {C3} |
  -------------
2 | {A2} | {B2} | {C2} |
  -------------
1 | {A1} | {B1} | {C1} |
  -------------
    A   B   C  \n'''.format(**self.board)
