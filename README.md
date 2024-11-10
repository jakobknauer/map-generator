# Quick Start

## Install

1. Clone the repository
    ```bash
    git clone https://github.com/jakobknauer/map-generator
    ```

2. Switch to main directory
    ```bash
    cd map-generator
    ```

3. (Optional, but recommended) Create and activate a virtual environment by your favorite means

4. Install the package
    ```bash
    pip install .
    ```

As an alternative to steps 3 and 4, use [pipx](https://pipx.pypa.io/stable/) to make the program available globally
```bash
pipx install .
```

## Run

1. (Optional) Adapt `conf/conf.toml`

2. Execute
    ```bash
    mapgen conf/conf.toml
    ```

3. Check the output in the directory specified in `conf/conf.toml` (by default `./out`)


# Examples

See [the examples folders](examples) for the iterative refinement of a map.

The following config was used for generating these files:

```toml
[output]
directory = "examples"
file_prefix = "map_"
optimize = true
visible_borders = false


[generation]
preset = "island_and_shore"
num_iterations = 7

inertia = 0.5
islands_per_iteration = 5.0
lakes_per_iteration = 1.0
```

# Algorithm and Configuration

The generation is based on a grid of square tiles, each of which is colored as either land or sea.
Starting from a preset (see [presets.py](src/map_generator/presets.py) for available presets), the map is iteratively refined.
In each iteration, all tiles are first split into four new tiles of the same color, which are then randomly repainted.

The random distribution is biased towards the current color of the tile, as well as those of its neighbors. That is, a land tile surrounded by land tiles is very likely to remain a land tile. The `inertia` config parameter controls the weight of the tile's color, as opposed to the tile's neighbors' colors. A low value of `inertia` will thus lead to more "rugged" coastlines, as the sea neighbor tiles of a land tile gain influence, and vice versa.

The config parameters `islands_per_iteration` and `lakes_per_iteration` influence the algorithm by creating lower and upper bounds for the probability of each tile becoming or staying land or sea. For example, the higher the value of `lakes_per_iteration`, the more likely it is that even land tiles completely surrounded by other land tiles turn into sea tiles (or perhaps more appropriately in this case, "lake tiles").
