import sys
import os
import nbtlib
import math

def read_varint(stream):
    """Read a VarInt from a stream (byte iterator)."""
    value = 0
    shift = 0
    while True:
        try:
            byte = next(stream)
        except StopIteration:
            raise EOFError("Unexpected end of stream while reading VarInt")
        
        value |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            break
        shift += 7
    return value

def load_schem(file_path):
    """Load a Sponge .schem file."""
    print(f"Loading .schem file: {file_path}")
    try:
        nbt_file = nbtlib.load(file_path)
        # nbtlib.load returns a File object which is itself the root compound
        root = nbt_file
        
        width = int(root['Width'])
        height = int(root['Height'])
        length = int(root['Length'])
        
        palette = root['Palette']
        block_data = root['BlockData']
        
        # Create reverse palette: int_id -> block_name
        rev_palette = {int(v): k for k, v in palette.items()}
        
        blocks = []
        
        # BlockData is a byte array of VarInts
        # We need to iterate through the bytes and decode VarInts
        # The order is usually Y, Z, X
        
        # Convert byte array to an iterator for VarInt reading
        # nbtlib ByteArray is a sequence of ints (signed or unsigned? usually signed in python struct, but here we treat as bytes)
        # We need to ensure we treat them as unsigned bytes (0-255)
        byte_stream = iter([b if b >= 0 else b + 256 for b in block_data])
        
        for y in range(height):
            for z in range(length):
                for x in range(width):
                    try:
                        block_id = read_varint(byte_stream)
                        if block_id in rev_palette:
                            name = rev_palette[block_id]
                            # Skip air
                            if name != "minecraft:air" and name != "air":
                                blocks.append((x, y, z, name))
                    except EOFError:
                        break
                        
        return blocks
    except Exception as e:
        print(f"Error loading .schem: {e}")
        return []

def load_nbt(file_path):
    """Load a Vanilla Structure .nbt file."""
    print(f"Loading .nbt file: {file_path}")
    try:
        nbt_file = nbtlib.load(file_path)
        # nbtlib.load returns a File object which is itself the root compound
        root = nbt_file
        
        # Check for required fields
        if 'palette' not in root or 'blocks' not in root:
            # Some NBT files might have 'palettes' (plural) if they contain multiple palettes
            if 'palettes' in root:
                print("Multi-palette NBT detected. Using the first palette.")
                palette = root['palettes'][0]
            else:
                print("Invalid .nbt structure format: missing 'palette' or 'blocks'")
                return []
        else:
            palette = root['palette']
            
        block_list = root['blocks']
        
        blocks = []
        
        for b in block_list:
            pos = b['pos']
            state = int(b['state'])
            
            if state < len(palette):
                block_state = palette[state]
                # block_state is a Compound, usually has 'Name' and 'Properties'
                if 'Name' in block_state:
                    name = block_state['Name']
                    if name != "minecraft:air" and name != "air":
                        blocks.append((int(pos[0]), int(pos[1]), int(pos[2]), name))
                
        return blocks
    except Exception as e:
        print(f"Error loading .nbt: {e}")
        return []

def load_litematic(file_path):
    """Load a .litematic file (Basic support)."""
    print(f"Loading .litematic file: {file_path}")
    print("Warning: .litematic support is experimental. Complex bit-packing might not be fully supported.")
    try:
        nbt_file = nbtlib.load(file_path)
        # nbtlib.load returns a File object which is itself the root compound
        root = nbt_file
        
        if 'Regions' not in root:
            print("Invalid .litematic format: missing 'Regions'")
            return []
            
        regions = root['Regions']
        blocks = []
        
        for region_name, region in regions.items():
            print(f"Processing region: {region_name}")
            # Each region has Position (x,y,z), Size(x,y,z), BlockStatePalette, BlockStates
            
            # This requires complex bit unpacking logic similar to Minecraft chunks
            # For now, we will skip implementation to avoid incorrect data
            print(f"Skipping region {region_name}: Litematic bit-unpacking not yet implemented.")
            
        return blocks
    except Exception as e:
        print(f"Error loading .litematic: {e}")
        return []

# Minecraft to Multicraft Block Mapping
BLOCK_MAPPING = {
    # === 基本ブロック ===
    "minecraft:air": None,
    "minecraft:stone": "default:stone",
    "minecraft:granite": "default:stone",
    "minecraft:polished_granite": "default:stone",
    "minecraft:diorite": "default:stone",
    "minecraft:polished_diorite": "default:stone",
    "minecraft:andesite": "default:stone",
    "minecraft:polished_andesite": "default:stone",
    "minecraft:grass_block": "default:dirt_with_grass",
    "minecraft:grass": "default:dirt_with_grass",
    "minecraft:dirt": "default:dirt",
    "minecraft:coarse_dirt": "default:dirt",
    "minecraft:podzol": "default:dirt",
    "minecraft:cobblestone": "default:cobble",
    
    # === 木材 ===
    "minecraft:planks": "default:wood",
    "minecraft:oak_planks": "default:wood",
    "minecraft:spruce_planks": "default:pine_wood",
    "minecraft:birch_planks": "default:birch_wood",
    "minecraft:jungle_planks": "default:junglewood",
    "minecraft:acacia_planks": "default:acacia_wood",
    "minecraft:dark_oak_planks": "default:wood",
    
    # === 原木 ===
    "minecraft:log": "default:tree",
    "minecraft:oak_log": "default:tree",
    "minecraft:spruce_log": "default:pine_tree",
    "minecraft:birch_log": "default:birch_tree",
    "minecraft:jungle_log": "default:jungletree",
    "minecraft:acacia_log": "default:acacia_tree",
    "minecraft:dark_oak_log": "default:tree",
    
    # === 葉 ===
    "minecraft:leaves": "default:leaves",
    "minecraft:oak_leaves": "default:leaves",
    "minecraft:spruce_leaves": "default:pine_needles",
    "minecraft:birch_leaves": "default:birch_leaves",
    "minecraft:jungle_leaves": "default:jungleleaves",
    "minecraft:acacia_leaves": "default:acacia_leaves",
    "minecraft:dark_oak_leaves": "default:leaves",
    "minecraft:leaves2": "default:acacia_leaves",
    
    # === 砂・砂利 ===
    "minecraft:sand": "default:sand",
    "minecraft:red_sand": "default:redsand",
    "minecraft:gravel": "default:gravel",
    "minecraft:sandstone": "default:sandstone",
    "minecraft:chiseled_sandstone": "default:sandstonecarved",
    "minecraft:smooth_sandstone": "default:sandstonesmooth",
    "minecraft:red_sandstone": "default:redsandstone",
    
    # === 鉱石 ===
    "minecraft:gold_ore": "default:stone_with_gold",
    "minecraft:iron_ore": "default:stone_with_iron",
    "minecraft:coal_ore": "default:stone_with_coal",
    "minecraft:diamond_ore": "default:stone_with_diamond",
    "minecraft:emerald_ore": "default:stone_with_emerald",
    "minecraft:lapis_ore": "default:stone_with_bluestone",
    "minecraft:redstone_ore": "default:stone_with_bluestone",
    "minecraft:copper_ore": "default:stone_with_copper",
    "minecraft:quartz_ore": "default:quartz_ore",
    
    # === 鉱石ブロック ===
    "minecraft:gold_block": "default:goldblock",
    "minecraft:iron_block": "default:steelblock",
    "minecraft:diamond_block": "default:diamondblock",
    "minecraft:emerald_block": "default:emeraldblock",
    "minecraft:lapis_block": "default:stone",
    "minecraft:coal_block": "default:coalblock",
    "minecraft:copper_block": "default:copperblock",
    "minecraft:quartz_block": "default:quartz_block",
    "minecraft:chiseled_quartz_block": "default:quartz_chiseled",
    "minecraft:quartz_pillar": "default:quartz_pillar",
    
    # === レンガ・石材 ===
    "minecraft:brick_block": "default:brick",
    "minecraft:bricks": "default:brick",
    "minecraft:stonebrick": "default:stonebrick",
    "minecraft:stone_bricks": "default:stonebrick",
    "minecraft:mossy_stone_bricks": "default:stonebrickmossy",
    "minecraft:cracked_stone_bricks": "default:stonebrickcracked",
    "minecraft:chiseled_stone_bricks": "default:stonebrickcarved",
    "minecraft:mossy_cobblestone": "default:mossycobble",
    "minecraft:nether_brick": "default:brick",
    
    # === ガラス ===
    "minecraft:glass": "default:glass",
    "minecraft:glass_pane": "default:glass",
    "minecraft:stained_glass": "default:glass",
    "minecraft:white_stained_glass": "default:glass_white",
    "minecraft:orange_stained_glass": "default:glass_orange",
    "minecraft:magenta_stained_glass": "default:glass_magenta",
    "minecraft:light_blue_stained_glass": "default:glass_cyan",
    "minecraft:yellow_stained_glass": "default:glass_yellow",
    "minecraft:lime_stained_glass": "default:glass_green",
    "minecraft:pink_stained_glass": "default:glass_pink",
    "minecraft:gray_stained_glass": "default:glass_grey",
    "minecraft:light_gray_stained_glass": "default:glass_grey",
    "minecraft:cyan_stained_glass": "default:glass_cyan",
    "minecraft:purple_stained_glass": "default:glass_violet",
    "minecraft:blue_stained_glass": "default:glass_blue",
    "minecraft:brown_stained_glass": "default:glass_brown",
    "minecraft:green_stained_glass": "default:glass_dark_green",
    "minecraft:red_stained_glass": "default:glass_red",
    "minecraft:black_stained_glass": "default:glass_black",
    
    # === 羊毛 ===
    "minecraft:wool": "wool:white",
    "minecraft:white_wool": "wool:white",
    "minecraft:orange_wool": "wool:orange",
    "minecraft:magenta_wool": "wool:magenta",
    "minecraft:light_blue_wool": "wool:cyan",
    "minecraft:yellow_wool": "wool:yellow",
    "minecraft:lime_wool": "wool:green",
    "minecraft:pink_wool": "wool:pink",
    "minecraft:gray_wool": "wool:grey",
    "minecraft:light_gray_wool": "wool:grey",
    "minecraft:cyan_wool": "wool:cyan",
    "minecraft:purple_wool": "wool:violet",
    "minecraft:blue_wool": "wool:blue",
    "minecraft:brown_wool": "wool:brown",
    "minecraft:green_wool": "wool:dark_green",
    "minecraft:red_wool": "wool:red",
    "minecraft:black_wool": "wool:black",
    
    # === テラコッタ ===
    "minecraft:hardened_clay": "default:hardened_clay",
    "minecraft:terracotta": "default:hardened_clay",
    "minecraft:white_terracotta": "hardened_clay:white",
    "minecraft:orange_terracotta": "hardened_clay:orange",
    "minecraft:magenta_terracotta": "hardened_clay:magenta",
    "minecraft:light_blue_terracotta": "hardened_clay:cyan",
    "minecraft:yellow_terracotta": "hardened_clay:yellow",
    "minecraft:lime_terracotta": "hardened_clay:green",
    "minecraft:pink_terracotta": "hardened_clay:pink",
    "minecraft:gray_terracotta": "hardened_clay:grey",
    "minecraft:light_gray_terracotta": "hardened_clay:grey",
    "minecraft:cyan_terracotta": "hardened_clay:cyan",
    "minecraft:purple_terracotta": "hardened_clay:violet",
    "minecraft:blue_terracotta": "hardened_clay:blue",
    "minecraft:brown_terracotta": "hardened_clay:brown",
    "minecraft:green_terracotta": "hardened_clay:dark_green",
    "minecraft:red_terracotta": "hardened_clay:red",
    "minecraft:black_terracotta": "hardened_clay:black",
    "minecraft:stained_hardened_clay": "default:hardened_clay",
    
    # === コンクリート ===
    "minecraft:concrete": "concrete:concrete",
    "minecraft:white_concrete": "concrete:concrete_white",
    "minecraft:orange_concrete": "concrete:concrete_orange",
    "minecraft:magenta_concrete": "concrete:concrete_magenta",
    "minecraft:light_blue_concrete": "concrete:concrete_cyan",
    "minecraft:yellow_concrete": "concrete:concrete_yellow",
    "minecraft:lime_concrete": "concrete:concrete_green",
    "minecraft:pink_concrete": "concrete:concrete_pink",
    "minecraft:gray_concrete": "concrete:concrete_grey",
    "minecraft:light_gray_concrete": "concrete:concrete_grey",
    "minecraft:cyan_concrete": "concrete:concrete_cyan",
    "minecraft:purple_concrete": "concrete:concrete_violet",
    "minecraft:blue_concrete": "concrete:concrete_blue",
    "minecraft:brown_concrete": "concrete:concrete_brown",
    "minecraft:green_concrete": "concrete:concrete_dark_green",
    "minecraft:red_concrete": "concrete:concrete_red",
    "minecraft:black_concrete": "concrete:concrete_black",
    
    # === その他ブロック ===
    "minecraft:bedrock": "default:stone",
    "minecraft:water": "default:water_source",
    "minecraft:flowing_water": "default:water_flowing",
    "minecraft:lava": "default:lava_source",
    "minecraft:flowing_lava": "default:lava_flowing",
    "minecraft:sponge": "sponge:sponge",
    "minecraft:obsidian": "default:obsidian",
    "minecraft:glowstone": "default:glowstone",
    "minecraft:ice": "default:ice",
    "minecraft:packed_ice": "default:packedice",
    "minecraft:snow": "default:snowblock",
    "minecraft:snow_block": "default:snowblock",
    "minecraft:snow_layer": "default:snowblock",
    "minecraft:clay": "default:clay",
    "minecraft:cactus": "default:cactus",
    "minecraft:bookshelf": "shelf:bookshelf",
    "minecraft:slime": "bluestone_stickyblocks:slimeblock",
    "minecraft:slime_block": "bluestone_stickyblocks:slimeblock",
    "minecraft:melon": "farming_plants:watermelon_fruit",
    "minecraft:melon_block": "farming_plants:watermelon_fruit",
    "minecraft:pumpkin": "farming_plants:pumpkin_fruit",
    "minecraft:hay_block": "farming:straw",
    
    # === 機能ブロック ===
    "minecraft:chest": "default:chest",
    "minecraft:crafting_table": "workbench:workbench",
    "minecraft:furnace": "default:furnace",
    "minecraft:lit_furnace": "default:furnace",
}

def parse_block_state(block_name):
    """Parse block name and extract block states.
    Returns (base_name, states_dict)
    """
    if "[" not in block_name:
        return block_name, {}
    
    base_name = block_name.split("[")[0]
    states_str = block_name.split("[")[1].rstrip("]")
    
    states = {}
    for pair in states_str.split(","):
        if "=" in pair:
            key, value = pair.split("=", 1)
            states[key.strip()] = value.strip()
    
    return base_name, states

def get_param2_for_stairs(states):
    """Convert Minecraft stair block states to Minetest param2.
    Minecraft: facing (north/south/east/west), half (bottom/top)
    Minetest: param2 (0-3 normal, 20-23 upside-down)
    """
    # Minecraft facing to Minetest param2 mapping
    # Minecraft "facing" = direction the stairs ascend toward
    facing_map = {
        "north": 2,  # 北向き (back to south)
        "south": 0,  # 南向き (back to north)
        "east": 1,   # 東向き (back to west)
        "west": 3,   # 西向き (back to east)
    }
    
    facing = states.get("facing", "north")
    half = states.get("half", "bottom")
    
    param2 = facing_map.get(facing, 0)
    
    # If upside-down, add 20
    if half == "top":
        param2 += 20
    
    return param2

def get_param2_for_slab(states):
    """Convert Minecraft slab block states to Minetest param2.
    Minecraft: type (bottom/top/double)
    Minetest: param2 (0 = bottom, 20 = top)
    """
    slab_type = states.get("type", "bottom")
    
    if slab_type == "top":
        return 20
    elif slab_type == "double":
        return -1  # Will be handled specially (use full block)
    else:
        return 0

def is_stair_block(base_name):
    """Check if block is a stair type."""
    stair_keywords = ["stairs", "_stairs"]
    return any(kw in base_name.lower() for kw in stair_keywords)

def is_slab_block(base_name):
    """Check if block is a slab type."""
    slab_keywords = ["slab", "_slab"]
    return any(kw in base_name.lower() for kw in slab_keywords)

def get_multicraft_block(minecraft_name):
    """Convert Minecraft block name to Multicraft block name and param2.
    Returns (block_name, param2) tuple.
    """
    # Parse block state
    base_name, states = parse_block_state(minecraft_name.lower())
    
    # Normalize name
    if not base_name.startswith("minecraft:"):
        base_name = "minecraft:" + base_name
    
    # Calculate param2 for stairs and slabs
    param2 = 0
    if is_stair_block(base_name):
        param2 = get_param2_for_stairs(states)
    elif is_slab_block(base_name):
        param2 = get_param2_for_slab(states)
    
    # Check mapping
    if base_name in BLOCK_MAPPING:
        mapped = BLOCK_MAPPING[base_name]
        if mapped is None:
            return None, 0
        return mapped, param2
    
    # Fallback: simple replacement
    return base_name.replace("minecraft:", "default:"), param2

def generate_commands(blocks, scale=1):
    """Generate building commands from block list [(x,y,z,name), ...]."""
    commands = []
    current_pos = [0, 0, 0]
    skipped = 0
    
    # Sort by Y, then Z, then X
    sorted_blocks = sorted(blocks, key=lambda p: (p[1], p[2], p[0]))
    
    for block in sorted_blocks:
        x, y, z, name = block
        
        # Convert block name using mapping (returns tuple: block_name, param2)
        result = get_multicraft_block(name)
        cmd_name, param2 = result
        
        # Skip air blocks
        if cmd_name is None:
            skipped += 1
            continue
        
        target = [x, y, z]
        
        shifts = []
        for i, (curr, tgt) in enumerate(zip(current_pos, target)):
            scaled_tgt = tgt * scale
            scaled_curr = curr * scale
            diff = int(scaled_tgt - scaled_curr)
            
            if diff != 0:
                axis = ['x', 'y', 'z'][i]
                shifts.append(f"/shift {axis} {diff}")
                current_pos[i] = tgt
        
        commands.extend(shifts)
        
        # Add block placement command
        commands.append(f"/s {cmd_name}")
        
        # Add param2 command if non-zero (for stairs, slabs orientation)
        if param2 != 0:
            commands.append(f"/param2 {param2}")
    
    if skipped > 0:
        print(f"スキップしたブロック (air): {skipped}")
        
    return commands

def save_commands(commands, output_file):
    """Save commands to file(s)."""
    MAX_LINES = 30000
    
    if len(commands) > MAX_LINES:
        base_name, ext = os.path.splitext(output_file)
        num_files = (len(commands) + MAX_LINES - 1) // MAX_LINES
        
        for i in range(num_files):
            start_idx = i * MAX_LINES
            end_idx = min((i + 1) * MAX_LINES, len(commands))
            current_file = f"{base_name}_part{i+1}{ext}"
         
            with open(current_file, 'w') as f:
                for cmd in commands[start_idx:end_idx]:
                    f.write(cmd + '\n')
            print(f"パート {i+1} を保存しました: {current_file}")
    else:
        with open(output_file, 'w') as f:
            for cmd in commands:
                f.write(cmd + '\n')
        print(f"コマンドを保存しました: {output_file}")

def main():
    print("--- Minecraft Schematic to Command Converter ---")
    file_path = input("ファイルパスを入力してください (.schem, .nbt, .litematic): ").strip('"')
    
    if not os.path.exists(file_path):
        print("ファイルが見つかりません。")
        return

    ext = os.path.splitext(file_path)[1].lower()
    blocks = []
    
    if ext == '.schem':
        blocks = load_schem(file_path)
    elif ext == '.nbt':
        blocks = load_nbt(file_path)
    elif ext == '.litematic':
        blocks = load_litematic(file_path)
    else:
        print(f"未対応の拡張子です: {ext}")
        return
        
    if not blocks:
        print("ブロックが見つかりませんでした。")
        return
        
    print(f"読み込み完了: {len(blocks)} 個のブロック")
    
    # Find unknown blocks (not in mapping)
    unknown_blocks = {}
    for block in blocks:
        name = block[3].lower()
        base_name, _ = parse_block_state(name)
        if not base_name.startswith("minecraft:"):
            base_name = "minecraft:" + base_name
        
        if base_name not in BLOCK_MAPPING and base_name not in unknown_blocks:
            # Count occurrences
            count = sum(1 for b in blocks if parse_block_state(b[3].lower())[0] == base_name or 
                       "minecraft:" + parse_block_state(b[3].lower())[0] == base_name)
            unknown_blocks[base_name] = count
    
    # Ask user for replacements
    user_mappings = {}
    if unknown_blocks:
        print(f"\n未対応のブロックが {len(unknown_blocks)} 種類見つかりました:")
        for block_name, count in sorted(unknown_blocks.items(), key=lambda x: -x[1]):
            print(f"  - {block_name} ({count} 個)")
        
        print("\n各ブロックの置換先を入力してください。")
        print("(空欄でスキップ、'air'で削除、'default:stone'のような形式で入力)")
        print()
        
        for block_name in sorted(unknown_blocks.keys()):
            default_fallback = block_name.replace("minecraft:", "default:")
            replacement = input(f"{block_name} → (デフォルト: {default_fallback}): ").strip()
            
            if replacement == "":
                user_mappings[block_name] = default_fallback
            elif replacement.lower() == "air":
                user_mappings[block_name] = None  # Skip this block
            else:
                user_mappings[block_name] = replacement
        
        # Add user mappings to BLOCK_MAPPING temporarily
        BLOCK_MAPPING.update(user_mappings)
        print()
    
    filename = input("出力ファイル名を入力してください（未入力で自動生成）: ")
    if not filename:
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        filename = f"{base_name}.txt"
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, filename)
    print(f"ファイルは以下に保存されます: {output_file}")
    
    print("コマンド生成中...")
    commands = generate_commands(blocks)
    
    save_commands(commands, output_file)
    print(f"完了! 総コマンド数: {len(commands)}")

if __name__ == "__main__":
    main()
