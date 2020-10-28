from typing import *


class Tile:
    def __init__(self, glyph: str, enable_collision: bool):
        self.glyph: str = glyph
        self.enable_collision: bool = enable_collision
