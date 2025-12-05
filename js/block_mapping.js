// Minecraft to Multicraft Block Mapping Table
// Usage: BLOCK_MAPPING["minecraft:stone"] returns "default:stone"

const BLOCK_MAPPING = {
    // === 基本ブロック ===
    "minecraft:air": null, // Skip air blocks
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

    // === 木材 ===
    "minecraft:planks": "default:wood",
    "minecraft:oak_planks": "default:wood",
    "minecraft:spruce_planks": "default:pine_wood",
    "minecraft:birch_planks": "default:birch_wood",
    "minecraft:jungle_planks": "default:junglewood",
    "minecraft:acacia_planks": "default:acacia_wood",
    "minecraft:dark_oak_planks": "default:wood",

    // === 原木 ===
    "minecraft:log": "default:tree",
    "minecraft:oak_log": "default:tree",
    "minecraft:spruce_log": "default:pine_tree",
    "minecraft:birch_log": "default:birch_tree",
    "minecraft:jungle_log": "default:jungletree",
    "minecraft:acacia_log": "default:acacia_tree",
    "minecraft:dark_oak_log": "default:tree",

    // === 葉 ===
    "minecraft:leaves": "default:leaves",
    "minecraft:oak_leaves": "default:leaves",
    "minecraft:spruce_leaves": "default:pine_needles",
    "minecraft:birch_leaves": "default:birch_leaves",
    "minecraft:jungle_leaves": "default:jungleleaves",
    "minecraft:acacia_leaves": "default:acacia_leaves",
    "minecraft:dark_oak_leaves": "default:leaves",
    "minecraft:leaves2": "default:acacia_leaves",

    // === 砂・砂利 ===
    "minecraft:sand": "default:sand",
    "minecraft:red_sand": "default:redsand",
    "minecraft:gravel": "default:gravel",
    "minecraft:sandstone": "default:sandstone",
    "minecraft:chiseled_sandstone": "default:sandstonecarved",
    "minecraft:smooth_sandstone": "default:sandstonesmooth",
    "minecraft:red_sandstone": "default:redsandstone",

    // === 鉱石 ===
    "minecraft:gold_ore": "default:stone_with_gold",
    "minecraft:iron_ore": "default:stone_with_iron",
    "minecraft:coal_ore": "default:stone_with_coal",
    "minecraft:diamond_ore": "default:stone_with_diamond",
    "minecraft:emerald_ore": "default:stone_with_emerald",
    "minecraft:lapis_ore": "default:stone_with_bluestone",
    "minecraft:redstone_ore": "default:stone_with_bluestone",
    "minecraft:copper_ore": "default:stone_with_copper",
    "minecraft:quartz_ore": "default:quartz_ore",

    // === 鉱石ブロック ===
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

    // === レンガ・石材 ===
    "minecraft:brick_block": "default:brick",
    "minecraft:bricks": "default:brick",
    "minecraft:stonebrick": "default:stonebrick",
    "minecraft:stone_bricks": "default:stonebrick",
    "minecraft:mossy_stone_bricks": "default:stonebrickmossy",
    "minecraft:cracked_stone_bricks": "default:stonebrickcracked",
    "minecraft:chiseled_stone_bricks": "default:stonebrickcarved",
    "minecraft:mossy_cobblestone": "default:mossycobble",
    "minecraft:nether_brick": "default:brick",

    // === ガラス ===
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

    // === 羊毛 ===
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

    // === テラコッタ ===
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

    // === コンクリート ===
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

    // === その他ブロック ===
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

    // === 機能ブロック ===
    "minecraft:chest": "default:chest",
    "minecraft:crafting_table": "workbench:workbench",
    "minecraft:furnace": "default:furnace",
    "minecraft:lit_furnace": "default:furnace",

    // === 階段 (基本マッピング) ===
    "minecraft:oak_stairs": "stairs:stair_default_wood",
    "minecraft:spruce_stairs": "stairs:stair_default_pine_wood",
    "minecraft:birch_stairs": "stairs:stair_default_birch_wood",
    "minecraft:jungle_stairs": "stairs:stair_default_junglewood",
    "minecraft:acacia_stairs": "stairs:stair_default_acacia_wood",
    "minecraft:dark_oak_stairs": "stairs:stair_default_wood",
    "minecraft:stone_stairs": "stairs:stair_default_cobble",
    "minecraft:cobblestone_stairs": "stairs:stair_default_cobble",
    "minecraft:brick_stairs": "stairs:stair_default_brick",
    "minecraft:stone_brick_stairs": "stairs:stair_default_stonebrick",
    "minecraft:sandstone_stairs": "stairs:stair_default_sandstone",
    "minecraft:quartz_stairs": "stairs:stair_default_quartz_block",

    // === ハーフブロック (基本マッピング) ===
    "minecraft:stone_slab": "stairs:slab_default_stone",
    "minecraft:oak_slab": "stairs:slab_default_wood",
    "minecraft:spruce_slab": "stairs:slab_default_pine_wood",
    "minecraft:birch_slab": "stairs:slab_default_birch_wood",
    "minecraft:jungle_slab": "stairs:slab_default_junglewood",
    "minecraft:acacia_slab": "stairs:slab_default_acacia_wood",
    "minecraft:dark_oak_slab": "stairs:slab_default_wood",
    "minecraft:brick_slab": "stairs:slab_default_brick",
    "minecraft:stone_brick_slab": "stairs:slab_default_stonebrick",
    "minecraft:sandstone_slab": "stairs:slab_default_sandstone",
    "minecraft:quartz_slab": "stairs:slab_default_quartz_block",

    // === 松明・照明 ===
    "minecraft:torch": "default:torch",
    "minecraft:wall_torch": "default:torch",
    "minecraft:lantern": "lanterns:lantern_off",
    "minecraft:soul_lantern": "lanterns:lantern_off",
    "minecraft:redstone_lamp": "default:glowstone",
    "minecraft:lit_redstone_lamp": "default:glowstone",

    // === はしご ===
    "minecraft:ladder": "default:ladder_wood",

    // === フェンス ===
    "minecraft:fence": "default:fence_wood",
    "minecraft:oak_fence": "default:fence_wood",
    "minecraft:spruce_fence": "default:fence_pine_wood",
    "minecraft:birch_fence": "default:fence_birch_wood",
    "minecraft:jungle_fence": "default:fence_jungle_wood",
    "minecraft:acacia_fence": "default:fence_acacia_wood",
    "minecraft:dark_oak_fence": "default:fence_wood",
    "minecraft:nether_brick_fence": "default:fence_wood",

    // === フェンスゲート ===
    "minecraft:fence_gate": "doors:gate_wood",
    "minecraft:oak_fence_gate": "doors:gate_wood",
    "minecraft:spruce_fence_gate": "doors:gate_pine_wood",
    "minecraft:birch_fence_gate": "doors:gate_birch_wood",
    "minecraft:jungle_fence_gate": "doors:gate_jungle_wood",
    "minecraft:acacia_fence_gate": "doors:gate_acacia_wood",
    "minecraft:dark_oak_fence_gate": "doors:gate_wood",

    // === ドア ===
    "minecraft:wooden_door": "doors:door_wood",
    "minecraft:oak_door": "doors:door_wood",
    "minecraft:spruce_door": "doors:door_pine_wood",
    "minecraft:birch_door": "doors:door_birch_wood",
    "minecraft:jungle_door": "doors:door_jungle_wood",
    "minecraft:acacia_door": "doors:door_acacia_wood",
    "minecraft:dark_oak_door": "doors:door_wood",
    "minecraft:iron_door": "doors:door_steel",

    // === トラップドア ===
    "minecraft:trapdoor": "doors:trapdoor",
    "minecraft:oak_trapdoor": "doors:trapdoor",
    "minecraft:spruce_trapdoor": "doors:trapdoor_pine_wood",
    "minecraft:birch_trapdoor": "doors:trapdoor_birch_wood",
    "minecraft:jungle_trapdoor": "doors:trapdoor_jungle_wood",
    "minecraft:acacia_trapdoor": "doors:trapdoor_acacia_wood",
    "minecraft:dark_oak_trapdoor": "doors:trapdoor",
    "minecraft:iron_trapdoor": "doors:trapdoor_steel",

    // === ベッド ===
    "minecraft:bed": "beds:bed_red",
    "minecraft:white_bed": "beds:bed_white",
    "minecraft:orange_bed": "beds:bed_orange",
    "minecraft:magenta_bed": "beds:bed_magenta",
    "minecraft:light_blue_bed": "beds:bed_cyan",
    "minecraft:yellow_bed": "beds:bed_yellow",
    "minecraft:lime_bed": "beds:bed_green",
    "minecraft:pink_bed": "beds:bed_pink",
    "minecraft:gray_bed": "beds:bed_grey",
    "minecraft:light_gray_bed": "beds:bed_grey",
    "minecraft:cyan_bed": "beds:bed_cyan",
    "minecraft:purple_bed": "beds:bed_violet",
    "minecraft:blue_bed": "beds:bed_blue",
    "minecraft:brown_bed": "beds:bed_brown",
    "minecraft:green_bed": "beds:bed_dark_green",
    "minecraft:red_bed": "beds:bed_red",
    "minecraft:black_bed": "beds:bed_black",

    // === レール ===
    "minecraft:rail": "carts:rail",
    "minecraft:golden_rail": "carts:rail",
    "minecraft:powered_rail": "carts:rail",
    "minecraft:detector_rail": "carts:rail",
    "minecraft:activator_rail": "carts:rail",

    // === TNT ===
    "minecraft:tnt": "tnt:tnt",

    // === ガラス板・鉄格子 ===
    "minecraft:stained_glass_pane": "xpanes:pane_flat",
    "minecraft:iron_bars": "xpanes:bar_flat",

    // === クモの巣 ===
    "minecraft:web": "mobs_monsters:cobweb",
    "minecraft:cobweb": "mobs_monsters:cobweb",

    // === サンゴブロック ===
    "minecraft:tube_coral_block": "ocean:coral_blue_tubular_block",
    "minecraft:brain_coral_block": "ocean:coral_pink_acropora_block",
    "minecraft:bubble_coral_block": "ocean:coral_yellow_fiery_block",
    "minecraft:fire_coral_block": "ocean:coral_red_rubrum_block",
    "minecraft:horn_coral_block": "ocean:coral_yellow_fiery_block",

    // === 看板 ===
    "minecraft:standing_sign": "signs:sign",
    "minecraft:wall_sign": "signs:sign",
    "minecraft:oak_sign": "signs:sign",
    "minecraft:spruce_sign": "signs:sign_pine_wood",
    "minecraft:birch_sign": "signs:sign_birch_wood",
    "minecraft:jungle_sign": "signs:sign_junglewood",
    "minecraft:acacia_sign": "signs:sign_acacia_wood",
    "minecraft:dark_oak_sign": "signs:sign",

    // === その他の追加ブロック ===
    "minecraft:bamboo": "water_plants:bamboo",
    "minecraft:lily_pad": "swamp_biome:waterlily",
    "minecraft:waterlily": "swamp_biome:waterlily",
    "minecraft:jack_o_lantern": "farming_plants:pumpkin_fruit",
    "minecraft:lit_pumpkin": "farming_plants:pumpkin_fruit",
    "minecraft:carved_pumpkin": "farming_plants:pumpkin_fruit",
    "minecraft:jukebox": "default:chest",
    "minecraft:enchanting_table": "x_enchanting:table",
    "minecraft:brewing_stand": "brewing:stand",
    "minecraft:armor_stand": "3d_armor_stand:armor_stand",
    "minecraft:flower_pot": "flowers:pot",
    "minecraft:painting": "painting:painting",
    "minecraft:item_frame": "itemframes:frame",
};

// Function to get multicraft block name from minecraft block name
function getMulticraftBlock(minecraftBlock) {
    // Remove minecraft: prefix if present
    const key = minecraftBlock.startsWith("minecraft:") ? minecraftBlock : "minecraft:" + minecraftBlock;

    if (key in BLOCK_MAPPING) {
        return BLOCK_MAPPING[key];
    }

    // Fallback: try simple replacement
    return minecraftBlock.replace("minecraft:", "default:");
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { BLOCK_MAPPING, getMulticraftBlock };
}
