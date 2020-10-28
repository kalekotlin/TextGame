from typing import *
from Tile import Tile

class Level:
    def __init__(self, level: List, x: int, y: int):
        self.level: List = level
        self.x: int = x
        self.y: int = y

    def print_level(self):
        c = 0
        for i in range(0, len(self.level)):
            if c == self.x:
                print()
                c = 0

            if isinstance(self.level[0], Tile):
                print(f" {self.level[i].glyph} ", end='')
            else:
                raise Exception("self.level should be set to a list of Tiles.")

            c += 1
