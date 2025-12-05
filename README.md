# scheme-convertor

Convert Minecraft schematics and 3D models to Multicraft/Minetest WorldEdit commands.

> Fork of [multi-nono/3D-Model-To-world.edit-command-minetest-W.E-](https://github.com/multi-nono/3D-Model-To-world.edit-command-minetest-W.E-)

## Features

- Convert `.schem`, `.nbt`, `.litematic` files to WorldEdit commands
- Convert 3D models (`.obj`, `.stl`) via voxelization
- Web-based GUI and Python CLI options

## Quick Start

### Web GUI
Open `schem_converter.html` in a browser, drop a file, and click "Convert".

### Python CLI
```bash
pip install nbtlib trimesh numpy

# For schematics
python schem.py <input_file>

# For 3D models
python model_to_cmd.py
```

## Files

| File | Description |
|------|-------------|
| `schem_converter.html` | Web-based converter |
| `schem.py` | Schematic converter (CLI) |
| `model_to_cmd.py` | 3D model converter |
| `block_mapping.js` | Block name mappings |
