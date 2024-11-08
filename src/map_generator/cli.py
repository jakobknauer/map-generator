from pathlib import Path

from map_generator.generator import generate_land_and_sea
from map_generator.io import write_map_to_file
from map_generator.map import Map


def main_cli():
    print("Hello, World!")

    num_iterations = 7
    output_dir = Path("out")

    def output_callback(iteration: int, map_: Map) -> None:
        output_file = output_dir / f"map_{iteration}.svg"
        with open(output_file, "w") as fp:
            write_map_to_file(map_, fp, optimize=True)

    generate_land_and_sea(
        preset="island_and_shore",
        num_iterations=num_iterations,
        output_callback=output_callback,
    )
