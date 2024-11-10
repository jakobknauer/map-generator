import tomllib
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from typing import Any


@dataclass
class OutputConfig:
    directory: Path
    file_prefix: str
    optimize: bool
    visible_borders: bool


@dataclass
class GenerationConfig:
    preset: str
    num_iterations: int
    inertia: float
    islands_per_iteration: float
    lakes_per_iteration: float


@dataclass
class Config:
    output: OutputConfig
    generation: GenerationConfig

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Config":
        output = OutputConfig(
            directory=Path(data["output"]["directory"]),
            file_prefix=str(data["output"]["file_prefix"]),
            optimize=bool(data["output"]["optimize"]),
            visible_borders=bool(data["output"]["visible_borders"]),
        )

        generation = GenerationConfig(
            preset=str(data["generation"]["preset"]),
            num_iterations=int(data["generation"]["num_iterations"]),
            inertia=float(data["generation"]["inertia"]),
            islands_per_iteration=float(data["generation"]["islands_per_iteration"]),
            lakes_per_iteration=float(data["generation"]["lakes_per_iteration"]),
        )

        return Config(output, generation)

    @staticmethod
    def from_toml_file(file: PathLike) -> "Config":
        with open(file, "rb") as fp:
            data = tomllib.load(fp)
        return Config.from_dict(data)
