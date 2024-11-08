from random import Random

from map_generator.map import Color, Map, Tile


class Painter:
    def __init__(self, map_: Map) -> None:
        self._map: Map = map_
        self._random: Random = Random()

        self._inertia: float = 0.6
        self._islands_per_iteration: float = 1.0
        self._lakes_per_iteration: float = 1.0

    def paint(self) -> None:
        min_prob = self._islands_per_iteration / self._map.get_tile_count()
        max_prob = 1 - (self._lakes_per_iteration / self._map.get_tile_count())

        new_tiles: dict[tuple[int, int], Tile] = {}

        for tile in self._map.get_tiles():
            neighbors = self._map.get_neighbors(tile.x, tile.y)

            p_land = 0.5
            p_land += self._inertia * ((1 if tile.color == Color.LAND else 0) - 0.5)

            if len(neighbors) == 0:
                land_proportion = 0.5
            else:
                land_proportion = sum(
                    1 for n in neighbors if n.color == Color.LAND
                ) / float(len(neighbors))
            p_land += (land_proportion - 0.5) * (1 - self._inertia)

            p_land = max(min_prob, min(p_land, max_prob))

            if self._random.uniform(0, 1) < p_land:
                new_color = Color.LAND
            else:
                new_color = Color.SEA

            new_tiles[(tile.x, tile.y)] = Tile(
                tile.x, tile.y, new_color, tile.width, tile.height
            )

        self._map.set_tiles(new_tiles)
