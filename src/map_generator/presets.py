from map_generator.map import Color, Map, Tile


def get_preset(preset: str) -> Map:
    map_: Map

    if preset == "big_island":
        # A 2x2 island centered on a 4x4 map
        map_ = Map.build_monocolored(Color.SEA, width=4, height=4)
        map_.get_tile(1, 1).color = Color.LAND
        map_.get_tile(1, 2).color = Color.LAND
        map_.get_tile(2, 1).color = Color.LAND
        map_.get_tile(2, 2).color = Color.LAND
    elif preset == "island_and_shore":
        # Continent shore in the east, 1x2 island in the west
        map_ = Map.build_monocolored(Color.SEA, width=4, height=4)
        map_.get_tile(1, 1).color = Color.LAND
        map_.get_tile(1, 2).color = Color.LAND
        map_.get_tile(3, 0).color = Color.LAND
        map_.get_tile(3, 1).color = Color.LAND
        map_.get_tile(3, 2).color = Color.LAND
        map_.get_tile(3, 3).color = Color.LAND
    elif preset == "sea_and_land":
        # Sea on the left, land on the right
        map_.add_tile(Tile(0, 0, Color.SEA))
        map_.add_tile(Tile(1, 0, Color.LAND))
    else:
        raise ValueError(f"Unknown preset '{preset}'.")

    return map_
