from math import ceil, floor

from map_generator.map import Color, Map, Tile


class _Node:
    def __init__(self, x: int, y: int, width: int, height: int, map_: Map):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._map = map_

        self._uniform_color: Color | None = None
        self._children: tuple["_Node", ...]

        self._set_uniform_color()
        if not self._uniform_color:
            self._init_children()

    def _set_uniform_color(self) -> None:
        first_color: Color | None = self._map.get_tile(self._x, self._y).color

        for x in range(self._x, self._x + self._width):
            for y in range(self._y, self._y + self._height):
                c = self._map.get_tile(x, y).color
                if c != first_color:
                    self._uniform_color = None
                    return

        self._uniform_color = first_color

    def _init_children(self) -> None:
        x, y, width, height = self._x, self._y, self._width, self._height
        map_ = self._map

        if width == 1 and height == 1:
            self._children = tuple()
        elif width == 1:
            self._children = (
                _Node(x, y, width, floor(height / 2), map_),
                _Node(x, y + floor(height / 2), width, ceil(height / 2), map_),
            )
        elif height == 1:
            self._children = (
                _Node(x, y, floor(width / 2), height, map_),
                _Node(x + floor(width / 2), y, ceil(width / 2), height, map_),
            )
        else:
            self._children = (
                _Node(x, y, floor(width / 2), floor(height / 2), map_),
                _Node(
                    x + floor(width / 2), y, ceil(width / 2), floor(height / 2), map_
                ),
                _Node(
                    x, y + floor(height / 2), floor(width / 2), ceil(height / 2), map_
                ),
                _Node(
                    x + floor(width / 2),
                    y + floor(height / 2),
                    ceil(width / 2),
                    ceil(height / 2),
                    map_,
                ),
            )

    def generate_tiles(self, output: list[Tile]) -> None:
        if self._uniform_color:
            tile = Tile(
                self._x, self._y, self._uniform_color, self._width, self._height
            )
            output.append(tile)
        else:
            for child in self._children:
                child.generate_tiles(output)


class Quadtree:
    def __init__(self, map_: Map):
        self._root: _Node = _Node(0, 0, map_.get_width(), map_.get_height(), map_)

    def get_tiles(self) -> list[Tile]:
        output: list[Tile] = []
        self._root.generate_tiles(output)
        return output
