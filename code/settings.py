from loader import load_sound, load_font, load_image, resource_path

# Game Setup

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player':-26,
    'objects':-40,
    'grass':-10,
    'invisible':0
}
 
# Player EXP
EXP = 0

# Badge Conditions
GREEN = 0
ELECT = 0
BOSS = 0
ALLEN = 0
BSCORE = 0

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = resource_path('graphics/font/joystix.ttf')
UI_FONT_SIZE = 18

# general colours

WATER_COLOUR = '#71ddee'
UI_BG_COLOUR = '#222222'
UI_BORDER_COLOUR = '#111111'
TEXT_COLOUR = '#EEEEEE'

# ui colours

HEALTH_COLOUR = 'red'
ENERGY_COLOUR = 'blue'
UI_BORDER_COLOUR_ACTIVE = 'gold'

# Pause Screen UI
# Colors
WHITE = (255, 255, 255)
DARK_GREY = (50, 50, 50, 200)  # Semi-transparent dark overlay



WORLD_MAP = [

]

specialMusicNumber = 6
specialMusicTrigger = None

finalBoss = 1

weapon_data = {
    #'sword':{'cooldown':100, 'damage':15, 'graphic': resource_path('graphics/weapons/sword/full.png')},
    'lance':{'cooldown':400, 'damage':30, 'graphic': resource_path('graphics/weapons/lance/full.png')},
    #'axe':{'cooldown':300, 'damage':20, 'graphic': resource_path('graphics/weapons/axe/full.png')},
    #'rapier':{'cooldown':50, 'damage':8, 'graphic': resource_path('graphics/weapons/rapier/full.png')},
    #'sai':{'cooldown':80, 'damage':10, 'graphic': resource_path('graphics/weapons/sai/full.png')}
}

magic_data = {
    'flame':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/flame/fire.png')},
    'heal':{'strength':20, 'cost':10, 'graphic': resource_path('graphics/particles/heal/heal.png')},
    'gravity':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/gravity/gravity.png')},
    'wave':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/wave/wave.png')},
    'stoneSpell':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/stoneSpell/stoneSpell.png')},
    'boltSpell':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/boltSpell/boltSpell.png')},
    'elementSpell':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/elementSpell/elementSpell.png')},
    'forceSpell':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/forceSpell/forceSpell.png')},
    'wheelSpell':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/wheelSpell/wheelSpell.png')},
    'loopSpell':{'strength':1, 'cost':10, 'graphic': resource_path('graphics/particles/loopSpell/loopSpell.png')}
}

monster_data = {
    'squid':{'health':100, 'exp':100, 'damage':20, 'attack_type':'slash','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':80, 'notice_radius':360, 'musicPlay':0},
    'fg3white':{'health':300, 'exp':250, 'damage':40, 'attack_type':'claw','attack_sound':resource_path('audio/attack/claw.wav'), 'speed':2, 'resistance':3, 'attack_radius':120, 'notice_radius':400, 'musicPlay':1},
    'spirit':{'health':100, 'exp':110, 'damage':8, 'attack_type':'thunder','attack_sound':resource_path('audio/attack/fireball.wav'), 'speed':4, 'resistance':3, 'attack_radius':60, 'notice_radius':350, 'musicPlay':0},
    'chargedspirit':{'health':100, 'exp':110, 'damage':16, 'attack_type':'thunder','attack_sound':resource_path('audio/attack/fireball.wav'), 'speed':5, 'resistance':3, 'attack_radius':60, 'notice_radius':350, 'musicPlay':0},

    'fg1':{'health':100, 'exp':120, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':50, 'notice_radius':300, 'musicPlay':0},


    'BlobGreenEnergy1':{'health':100, 'exp':100, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':100, 'notice_radius':300, 'musicPlay':0},
    'BlobGreenGrav1':{'health':100, 'exp':100, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':100, 'notice_radius':300, 'musicPlay':0},
    'BlobGreenGrav2':{'health':100, 'exp':100, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':100, 'notice_radius':300, 'musicPlay':0},
    'BlobGreenKin1':{'health':100, 'exp':100, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':100, 'notice_radius':300, 'musicPlay':0},
    'CoonBrownGrav3':{'health':500, 'exp':150, 'damage':18, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':175, 'notice_radius':300, 'musicPlay':0},
    'CoonWhiteGrav3':{'health':500, 'exp':150, 'damage':24, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':200, 'notice_radius':350, 'musicPlay':0},
    'SpikeWhiteEnergy2':{'health':200, 'exp':125, 'damage':7, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':125, 'notice_radius':300, 'musicPlay':0},
    'SpikeWhiteKin1':{'health':200, 'exp':125, 'damage':7, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':125, 'notice_radius':300, 'musicPlay':0},
    'SpikeWhiteKin2':{'health':200, 'exp':125, 'damage':7, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':125, 'notice_radius':300, 'musicPlay':0},
    'SquidElect1':{'health':300, 'exp':145, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':175, 'notice_radius':325, 'musicPlay':0},
    'SquidEnergy3':{'health':300, 'exp':145, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':175, 'notice_radius':325, 'musicPlay':0},
    'SquidForce3':{'health':300, 'exp':145, 'damage':6, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':175, 'notice_radius':325, 'musicPlay':0},
    'StoneManElect2':{'health':500, 'exp':175, 'damage':21, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':225, 'notice_radius':350, 'musicPlay':0},
    'StoneManForce':{'health':500, 'exp':175, 'damage':21, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':225, 'notice_radius':350, 'musicPlay':0},
    'BlackBlobEnergy1':{'health':300, 'exp':150, 'damage':11, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':150, 'notice_radius':300, 'musicPlay':0},
    'BlackBlobKin1':{'health':300, 'exp':150, 'damage':11, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':175, 'notice_radius':300, 'musicPlay':0},
    'BlackSpikeEnergy2':{'health':300, 'exp':150, 'damage':11, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':3, 'resistance':3, 'attack_radius':175, 'notice_radius':300, 'musicPlay':0},    


    'finalboss':{'health':1000, 'exp':275, 'damage':64, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':5, 'resistance':3, 'attack_radius':250, 'notice_radius':450, 'musicPlay':0},



    'music1':{'health':1, 'exp':0, 'damage':0, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':0, 'resistance':0, 'attack_radius':250, 'notice_radius':300, 'musicPlay':1},
    'music2':{'health':1, 'exp':0, 'damage':0, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':0, 'resistance':0, 'attack_radius':250, 'notice_radius':300, 'musicPlay':2},
    'music3':{'health':1, 'exp':0, 'damage':0, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':0, 'resistance':0, 'attack_radius':250, 'notice_radius':300, 'musicPlay':3},
    'music4':{'health':1, 'exp':0, 'damage':0, 'attack_type':'leaf_attack','attack_sound':resource_path('audio/attack/slash.wav'), 'speed':0, 'resistance':0, 'attack_radius':250, 'notice_radius':300, 'musicPlay':4}
}
