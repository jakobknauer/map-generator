from fractal.io import write_map_to_file
from fractal.map import Color, Map, Tile
from fractal.strategy import Strategy


def main_cli():
    print("Hello, World!")

    map_ = Map()

    strategy = Strategy(map_)

    # Continent surrounded by sea
    # map_.add_tile(Tile(0, 0, Color.SEA))
    # map_.add_tile(Tile(0, 1, Color.SEA))
    # map_.add_tile(Tile(0, 2, Color.SEA))
    # map_.add_tile(Tile(0, 3, Color.SEA))
    # map_.add_tile(Tile(1, 0, Color.SEA))
    # map_.add_tile(Tile(1, 1, Color.LAND))
    # map_.add_tile(Tile(1, 2, Color.LAND))
    # map_.add_tile(Tile(1, 3, Color.SEA))
    # map_.add_tile(Tile(2, 0, Color.SEA))
    # map_.add_tile(Tile(2, 1, Color.LAND))
    # map_.add_tile(Tile(2, 2, Color.LAND))
    # map_.add_tile(Tile(2, 3, Color.SEA))
    # map_.add_tile(Tile(3, 0, Color.SEA))
    # map_.add_tile(Tile(3, 1, Color.SEA))
    # map_.add_tile(Tile(3, 2, Color.SEA))
    # map_.add_tile(Tile(3, 3, Color.SEA))

    # Continent in the west, big island on the left
    map_.add_tile(Tile(0, 0, Color.SEA))
    map_.add_tile(Tile(0, 1, Color.SEA))
    map_.add_tile(Tile(0, 2, Color.SEA))
    map_.add_tile(Tile(0, 3, Color.SEA))
    map_.add_tile(Tile(1, 0, Color.SEA))
    map_.add_tile(Tile(1, 1, Color.LAND))
    map_.add_tile(Tile(1, 2, Color.LAND))
    map_.add_tile(Tile(1, 3, Color.SEA))
    map_.add_tile(Tile(2, 0, Color.SEA))
    map_.add_tile(Tile(2, 1, Color.SEA))
    map_.add_tile(Tile(2, 2, Color.SEA))
    map_.add_tile(Tile(2, 3, Color.SEA))
    map_.add_tile(Tile(3, 0, Color.LAND))
    map_.add_tile(Tile(3, 1, Color.LAND))
    map_.add_tile(Tile(3, 2, Color.LAND))
    map_.add_tile(Tile(3, 3, Color.LAND))

    # Sea on the left, land on the right
    # map_.add_tile(Tile(0, 0, Color.SEA))
    # map_.add_tile(Tile(1, 0, Color.LAND))

    ITERATIONS = 7
    WIDTH = 4
    HEIGHT = 4

    with open("out/map_0.svg", "w") as fp:
        write_map_to_file(map_, fp, WIDTH, HEIGHT, optimize=True)

    for i in range(1, 1 + ITERATIONS):
        print(f"Iteration {i}")
        map_.split(2)
        strategy.iterate()

        with open(f"out/map_{i}_simplified.svg", "w") as fp:
            write_map_to_file(map_, fp, WIDTH * (2**i), HEIGHT * (2**i), optimize=True)
