# from dataclasses import dataclass
from typing import List, Tuple

# @dataclass
class Ship:
    def __init__(self, size: int, coordinates: List[Tuple[int, int]]):
        self.size = size
        self.coordinates = coordinates
        self.hits = []  # Простая инициализация
    # size: int
    # coordinates: List[Tuple[int,int]]
    # hits: List[Tuple[int,int]] = None
    
    # def __post_init__(self):
    #     self.hits = []
        
    def is_sunk(self) -> bool:
        return len(self.hits) == self.size
    