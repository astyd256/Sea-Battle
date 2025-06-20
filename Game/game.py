from board import Board
from ship import Ship

class Game:
    def __init__(self):
        self.player_board = Board()
        self.ai_board = Board #????
        self.current_turn = "player" #или ai
        self.__ships_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    def start_game(self):
        """Put ships for the player and AI"""
        #TODO: Add custom ship placement
        pass
    
    def _place_default_ships(self, board: Board, is_ai: bool = False):
        for size in self.__ships_sizes:
            board.place_ships_randomly(Ship(size,))