from math import ceil, floor

from fractal.map import Color, Map, Tile


class _Node:
    def __init__(self, x: int, y: int, width: int, height: int, map_: Map):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._map = map_
        self._uniform_color: Color | None = None
        self._uniform_color_set = False

        self._children: list["_Node"]

        if width == 1 and height == 1:
            self._children = []
        elif width == 1:
            self._children = [
                _Node(x, y, width, floor(height / 2), map_),
                _Node(x, y + floor(height / 2), width, ceil(height / 2), map_),
            ]
        elif height == 1:
            self._children = [
                _Node(x, y, floor(width / 2), height, map_),
                _Node(x + floor(width / 2), y, ceil(width / 2), height, map_),
            ]
        else:
            self._children = [
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
            ]

    def get_uniform_color(self) -> Color | None:
        if self._uniform_color_set:
            return self._uniform_color

        if len(self._children) == 0:
            self._uniform_color = self._map.get_tile(self._x, self._y).color
        else:
            all_colors: set[Color | None] = set(
                child.get_uniform_color() for child in self._children
            )
            if len(all_colors) == 1:
                self._uniform_color = next(iter(all_colors))
            else:
                self._uniform_color = None

        return self._uniform_color

    def generate_tiles(self, output: list[Tile]) -> None:
        uniform_color = self.get_uniform_color()
        if uniform_color:
            tile = Tile(self._x, self._y, uniform_color, self._width, self._height)
            output.append(tile)
        else:
            for child in self._children:
                child.generate_tiles(output)


class Quadtree:
    def __init__(self, map_: Map):
        self._root: _Node = _Node(
            0, 0, map_.get_width() + 1, map_.get_height() + 1, map_
        )

    def get_tiles(self) -> list[Tile]:
        output: list[Tile] = []
        self._root.generate_tiles(output)
        return output
