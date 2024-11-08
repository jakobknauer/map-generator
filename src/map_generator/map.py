from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class Color(Enum):
    SEA = 0
    LAND = 1


@dataclass
class Tile:
    x: int
    y: int
    color: Color
    width: int = 1
    height: int = 1


class Map:
    def __init__(self) -> None:
        self._tiles: dict[tuple[int, int], Tile] = {}

    @staticmethod
    def build_monocolored(color: Color, *, width: int, height: int) -> "Map":
        map_ = Map()
        for x in range(width):
            for y in range(height):
                map_.add_tile(Tile(x, y, color))
        return map_

    def add_tile(self, tile: Tile) -> None:
        self._tiles[tile.x, tile.y] = tile

    def get_tiles(self) -> Iterable[Tile]:
        return self._tiles.values()

    def set_tiles(self, tiles: dict[tuple[int, int], Tile]) -> None:
        self._tiles = tiles

    def split(self, n: int) -> None:
        self._tiles = {
            (new_x := tile.x * n + x, new_y := tile.y * n + y): Tile(
                x=new_x, y=new_y, color=tile.color
            )
            for tile in self._tiles.values()
            for x in range(n)
            for y in range(n)
        }

    def get_tile(self, x: int, y: int) -> Tile:
        return self._tiles[(x, y)]

    def get_neighbors(self, x: int, y: int) -> list[Tile]:
        candidates = (
            self._find_tile(x - 1, y),
            self._find_tile(x + 1, y),
            self._find_tile(x, y - 1),
            self._find_tile(x, y + 1),
        )
        return [c for c in candidates if c]

    def _find_tile(self, x: int, y: int) -> Tile | None:
        return self._tiles.get((x, y), None)

    def get_width(self) -> int:
        return max(x for (x, _) in self._tiles) - min(x for (x, _) in self._tiles) + 1

    def get_height(self) -> int:
        return max(y for (_, y) in self._tiles) - min(y for (_, y) in self._tiles) + 1

    def get_tile_count(self) -> int:
        return len(self._tiles)
