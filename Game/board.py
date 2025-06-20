from ship import Ship
# from dataclasses import dataclass
from typing import List, Tuple

class Board():
    def __init__(self, size: int = 10):
        self.size = size # size of the field  i.e. board 10x10
        self.ships: List[Ship] = [ ]
        self.shots: set[Tuple[int, int]] = set() # log of shots in the game
    
    def find_available_spots(self, ship_size: int) -> list[list[tuple[int, int]]]:
        #checking rows
        available_spots = []
        for y in range(self.size):
            for x in range(ship_size - 1, self.size - ship_size + 1):
                if all(self.is_cell_empty(x + i, y) for i in range(ship_size)):
                    available_spots.append([(x + i, y) for i in range(ship_size)])
        #checking columns
        for x in range(self.size):
            for y in range(ship_size - 1, self.size - ship_size + 1):
                if all(self.is_cell_empty(x, y + i) for i in range(ship_size)):
                    available_spots.append([(x, y + i) for i in range(ship_size)])
        return available_spots
                   
    
    def place_ships_randomly(self, ship: Ship) -> bool:
        """Добавляет корабль на поле, если он не пересекается с другими."""
                                
        return True
        