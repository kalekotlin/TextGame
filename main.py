from Level import Level
from Tile import Tile

def main():
    mountain = Tile("^", True)
    water = Tile("~", True)
    grass = Tile(".", False)

    level_list = [
        mountain, mountain, mountain, water, mountain,
        mountain, grass, grass, water, mountain,
        mountain, grass, grass, water, water,
        mountain, grass, grass, grass, water,
        grass, grass, grass, grass, mountain
    ]

    level = Level(level_list, 5, 5)
    level.print_level()


main()
