import typing

import svg

from fractal.map import Color, Map, Tile
from fractal.quadtree import Quadtree

_COLORS = {Color.SEA: "cyan", Color.LAND: "green"}
_TILE_SIZE = 10


def write_map_to_file(
    map_: Map, fp: typing.TextIO, width: int, height: int, *, optimize: bool = False
) -> None:
    if optimize:
        quadtree = Quadtree(map_)
        tiles = quadtree.get_tiles()

        n_before = map_.get_tile_count()
        n_after = len(tiles)
        percentage_saved = (n_before - n_after) / float(n_before)
        print(
            f"Quadtree reduced tile count from {n_before} to {n_after} (-{percentage_saved:.2%})"
        )
    else:
        tiles = map_.get_tiles()

    write_tiles_to_file(tiles, fp, width, height)


def write_tiles_to_file(
    tiles: list[Tile], fp: typing.TextIO, width: int, height: int
) -> None:
    elements: list[svg.Rect] = []

    for tile in tiles:
        rect = svg.Rect(
            x=tile.x * _TILE_SIZE,
            y=tile.y * _TILE_SIZE,
            width=tile.width * _TILE_SIZE,
            height=tile.height * _TILE_SIZE,
            fill=_COLORS.get(tile.color),
            stroke="black",
        )
        elements.append(rect)

    canvas = svg.SVG(
        width=width * _TILE_SIZE, height=height * _TILE_SIZE, elements=elements
    )

    fp.write(str(canvas))
