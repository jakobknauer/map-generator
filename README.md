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
