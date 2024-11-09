import sys
from pathlib import Path

from map_generator.config import Config
from map_generator.generator import generate_land_and_sea
from map_generator.io import write_map_to_file
from map_generator.map import Map


def main_cli() -> None:
    config = Config.from_toml_file(Path(sys.argv[1]))
    config.output.output_dir.mkdir(parents=True, exist_ok=True)

    def output_callback(iteration: int, map_: Map) -> None:
        output_file = config.output.output_dir / f"{config.output.output_prefix}{iteration}.svg"
        with open(output_file, "w") as fp:
            write_map_to_file(map_, fp, optimize=True)

    generate_land_and_sea(config.generation, output_callback)
