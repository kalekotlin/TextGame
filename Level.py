from typing import *


class Level:
    def __init__(self, level: List, x: int, y: int):
        self.level: List = list
        self.x: int = x
        self.y: int = y

    def print_level(self):
        for i in range(0, len(self.level)):
            if i % self.x:
                print("\n")
            print(self.level[i])
