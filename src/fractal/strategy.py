from random import Random

from fractal.map import Color, Map, Tile


class Strategy:
    def __init__(self, map_: Map) -> None:
        self._map: Map = map_
        self._random: Random = Random()
        self._min_prob = 0.0
        self._max_prob = 1.0

    def iterate(self) -> None:
        self._min_prob = 1.0 / self._map.get_tile_count()
        self._max_prob = 1 - (1.0 / self._map.get_tile_count())

        new_tiles: dict[tuple[int, int], Tile] = {}

        for tile in self._map.get_tiles():
            neighbors = self._map.get_neighbors(tile.x, tile.y)

            if len(neighbors) == 0:
                land_proportion = 0.5
            else:
                land_proportion = sum(
                    1 for n in neighbors if n.color == Color.LAND
                ) / float(len(neighbors))

            land_probability = 0.7 if tile.color == Color.LAND else 0.3
            land_probability += (land_proportion - 0.5) * 0.8
            land_probability = max(
                self._min_prob, min(land_probability, self._max_prob)
            )

            if self._random.random() < land_probability:
                new_color = Color.LAND
            else:
                new_color = Color.SEA

            new_tiles[(tile.x, tile.y)] = Tile(
                tile.x, tile.y, new_color, tile.width, tile.height
            )

        self._map.set_tiles(new_tiles)
