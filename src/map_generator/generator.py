from typing import Callable

from map_generator.config import GenerationConfig
from map_generator.map import Map
from map_generator.painter import Painter
from map_generator.presets import get_preset


def generate_land_and_sea(config: GenerationConfig, output_callback: Callable[[int, Map], None]) -> Map:
    map_ = get_preset(config.preset)
    painter = Painter(
        inertia=config.inertia,
        islands_per_iteration=config.islands_per_iteration,
        lakes_per_iteration=config.lakes_per_iteration,
    )

    output_callback(0, map_)
    for iteration in range(1, 1 + config.num_iterations):
        print(f"Iteration {iteration}")

        map_.split(2)
        painter.paint(map_)

        output_callback(iteration, map_)

    return map_
