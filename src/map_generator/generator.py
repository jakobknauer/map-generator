from typing import Callable

from map_generator.map import Color, Map, Tile
from map_generator.painter import Painter


def generate_land_and_sea(
    preset: str, num_iterations: int, output_callback: Callable[[int, Map], None]
) -> Map:
    map_ = _get_preset(preset)
    painter = Painter(inertia=0.6, islands_per_iteration=1.0, lakes_per_iteration=1.0)

    output_callback(0, map_)
    for iteration in range(1, 1 + num_iterations):
        print(f"Iteration {iteration}")

        map_.split(2)
        painter.paint(map_)

        output_callback(iteration, map_)

    return map_


def _get_preset(preset: str) -> Map:
    map_ = Map()

    if preset == "big_island":
        map_.add_tile(Tile(0, 0, Color.SEA))
        map_.add_tile(Tile(0, 1, Color.SEA))
        map_.add_tile(Tile(0, 2, Color.SEA))
        map_.add_tile(Tile(0, 3, Color.SEA))
        map_.add_tile(Tile(1, 0, Color.SEA))
        map_.add_tile(Tile(1, 1, Color.LAND))
        map_.add_tile(Tile(1, 2, Color.LAND))
        map_.add_tile(Tile(1, 3, Color.SEA))
        map_.add_tile(Tile(2, 0, Color.SEA))
        map_.add_tile(Tile(2, 1, Color.LAND))
        map_.add_tile(Tile(2, 2, Color.LAND))
        map_.add_tile(Tile(2, 3, Color.SEA))
        map_.add_tile(Tile(3, 0, Color.SEA))
        map_.add_tile(Tile(3, 1, Color.SEA))
        map_.add_tile(Tile(3, 2, Color.SEA))
        map_.add_tile(Tile(3, 3, Color.SEA))
    elif preset == "island_and_shore":
        # Continent in the east, big island in the west
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
    elif preset == "sea_and_land":
        # Sea on the left, land on the right
        map_.add_tile(Tile(0, 0, Color.SEA))
        map_.add_tile(Tile(1, 0, Color.LAND))
    else:
        raise ValueError(f"Unknown preset '{preset}'.")

    return map_
