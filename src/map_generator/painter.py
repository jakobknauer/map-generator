from random import Random
from typing import Any

from map_generator.map import Color, Map, Tile


class Painter:
    def __init__(
        self,
        *,
        inertia: float = 1.0,
        islands_per_iteration: float = 0.0,
        lakes_per_iteration: float = 0.0,
        seed: Any = None
    ) -> None:
        self._random: Random = Random(seed)

        self._inertia: float = inertia
        self._islands_per_iteration: float = islands_per_iteration
        self._lakes_per_iteration: float = lakes_per_iteration

    def paint(self, map_: Map) -> None:
        min_prob = self._islands_per_iteration / map_.get_tile_count()
        max_prob = 1 - (self._lakes_per_iteration / map_.get_tile_count())

        new_tiles: dict[tuple[int, int], Tile] = {}

        for tile in map_.get_tiles():
            neighbors = map_.get_neighbors(tile.x, tile.y)

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

        map_.set_tiles(new_tiles)
