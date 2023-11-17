WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

#ui

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "../graphics/font/joystix.ttf"
UI_FONT_SIZE = 18

WATER_COLOR = "#71ddee"
UI_BGCOLOR = "#222222"
UI_BORDERCOLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

TEXT_COLOR_SELECTED = "#111111"
BAR_COLOR = "#EEEEEE"
BAR_COLOR_ACTIVE = "#111111"

HEALTH_COLOR = "red"
ENERGY_COLOR = "blue"
UI_BORDERCOLOR_ACTIVE = "gold"

weapon_data = {
    "sword" : {"cooldown": 100, "damage": 15, "graphic": "../graphics/weapons/sword/full.png"},
    "lance" : {"cooldown": 400, "damage": 30, "graphic": "../graphics/weapons/lance/full.png"},
    "axe" : {"cooldown": 300, "damage": 20, "graphic": "../graphics/weapons/axe/full.png"},
    "rapier" : {"cooldown": 50, "damage": 8, "graphic": "../graphics/weapons/rapier/full.png"},
    "sai" : {"cooldown": 80, "damage": 10, "graphic": "../graphics/weapons/sai/full.png"},
}

spell_data = {
    "flame" : {"strength": 7, "cost": 15, "graphic": "../graphics/particles/flame/fire.png"},
    "heal" : {"strength": 20, "damage": 15, "graphic": "../graphics/particles/heal/heal.png"}
}

#Monstres
monster_data = {
    "squid" : {"health": 100, "exp": 20, "attack_type":"slash", "attack_sound": "../audio/attack/slash.wav", "speed": 3, "resistance": 3, "attack_radius" : 80, "notice_radius": 360},
    "racoon" : {"health": 300, "exp": 40, "attack_type":"claw", "attack_sound": "../audio/attack/claw.wav", "speed": 2, "resistance": 3, "attack_radius" : 120, "notice_radius": 400},
    "spirit" : {"health": 100, "exp": 8, "attack_type":"thunder", "attack_sound": "../audio/attack/thunder.wav", "speed": 4, "resistance": 3, "attack_radius" : 60, "notice_radius": 350},
    "bamboo" : {"health": 70, "exp": 6, "attack_type":"razor_leaf", "attack_sound": "../audio/attack/razor_leaf.wav", "speed": 3, "resistance": 3, "attack_radius" : 50, "notice_radius": 300},
}
