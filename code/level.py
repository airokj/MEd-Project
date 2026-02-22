import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import *
from particles import AnimationPlayer
from magic import MagicPlayer
import settings
from math import *
from loader import load_sound, resource_path, load_image

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()



        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()


        # Sprite setup
        self.create_map()

        # User interface (UI)
        self.ui = UI()

        # Particle Sprites
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

#        self.main_sound = pygame.mixer.Sound('../audio/WhispersWoods.wav')
#        self.main_sound.set_volume(0.5)
#        self.main_sound.play(loops =1, fade_ms= 2000)


    def create_map(self):
        layouts = {
            'boundary': import_csv_layout(resource_path('map/thesis_FloorBlocks.csv')),
            'grass': import_csv_layout(resource_path('map/thesis_Grass.csv')),
            'objects': import_csv_layout(resource_path('map/thesis_Objects.csv')),
            'entities':import_csv_layout(resource_path('map/thesis_Entities.csv'))
        }
        graphics = {
            'grass': import_folder(resource_path('graphics/grass')),
            'objects': import_folder(resource_path('graphics/objects'))
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y= row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible') #self.visible_sprites, 
                        if style == 'grass':
                            #create grass
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'grass', random_grass_image)
                        if style == 'objects':
                            #create object
                            surf = graphics['objects'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'objects', surf)

                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                (x,y),                    #places character in the center of map
                                [self.visible_sprites], 
                                self.obstacle_sprites, 
                                self.create_attack, 
                                self.despawn_weapon,
                                self.create_magic
                                )        
                            
                            else:
                                if col =='390': 
                                    monster_name = 'fg1'
                                elif col =='391': 
                                    monster_name = 'spirit'
                                elif col =='392': 
                                    monster_name = 'fg3white'
                                elif col =='393': 
                                    monster_name = 'squid'
                                elif col =='369': 
                                    monster_name = 'chargedspirit'

                                elif col =='748': 
                                    monster_name = 'BlobGreenEnergy1'
                                elif col =='749': 
                                    monster_name = 'BlobGreenGrav1'
                                elif col =='750': 
                                    monster_name = 'BlobGreenGrav2'
                                elif col =='751': 
                                    monster_name = 'BlobGreenKin1'
                                elif col =='752': 
                                    monster_name = 'CoonBrownGrav3'

                                elif col =='770': 
                                    monster_name = 'SpikeWhiteKin1'
                                elif col =='771': 
                                    monster_name = 'SpikeWhiteKin2'
                                elif col =='772': 
                                    monster_name = 'SpikeWhiteEnergy2'
                                elif col =='773': 
                                    monster_name = 'CoonWhiteGrav3'

                                elif col =='792': 
                                    monster_name = 'SquidElect1'
                                elif col =='793': 
                                    monster_name = 'SquidForce3'
                                elif col =='794': 
                                    monster_name = 'SquidEnergy3'
                                elif col =='795': 
                                    monster_name = 'StoneManForce'
                                elif col =='796': 
                                    monster_name = 'StoneManElect2'

                                elif col =='800': 
                                    monster_name = 'BlackBlobEnergy1'
                                elif col =='799': 
                                    monster_name = 'BlackBlobKin1'
                                elif col =='798': 
                                    monster_name = 'BlackSpikeEnergy2'

                                elif col == '797':
                                    monster_name = 'finalboss'


                                elif col == '726':
                                    monster_name = 'music1'
                                elif col == '727':
                                    monster_name = 'music2'
                                elif col == '728':
                                    monster_name = 'music3'
                                elif col == '729':
                                    monster_name = 'music4'
                                Enemy(
                                    monster_name, 
                                    (x,y), 
                                    [self.visible_sprites, self.attackable_sprites], 
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles,
                                    self.add_exp)
                            

        #         if col == 'x':
        #             Tile((x,y), [self.visible_sprites, self.obstacle_sprites])
        #         if col == 'p':
        #             self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)


    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites, self.attack_sprites])


    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

        if style == 'flame':
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'gravity':
            self.magic_player.gravity(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'wave':
            self.magic_player.wave(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'stoneSpell':
            self.magic_player.stoneSpell(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'boltSpell':
            self.magic_player.boltSpell(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'elementSpell':
            self.magic_player.elementSpell(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'forceSpell':
            self.magic_player.forceSpell(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'wheelSpell':
            self.magic_player.wheelSpell(self.player, cost, [self.visible_sprites, self.attack_sprites])

        if style == 'loopSpell':
            self.magic_player.loopSpell(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def despawn_weapon(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 75)
                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)          # Can do IF for each enemy type is necessary
                            

    def damage_player (self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= floor(sqrt(amount) + 5.5) #Formula for increasing damage (8 to 13 per hit)
            
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            # swapn particles
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])
            if self.player.exp >= 6:
                self.player.exp -= amount

    def damage_penalty(self):
        if self.player.health > 0:
            self.player.speed = 5
        elif self.player.health <= 0:
            self.player.health = 0
            self.player.speed = 1

    def check_music(self):
        global specialMusicNumber
        global specialMusicTrigger
        #print("This is being checked")
        if settings.specialMusicNumber == 6:
            settings.specialMusicNumber = 1
            self.main_sound = load_sound('audio/WhispersWoods.wav')
            self.main_sound.set_volume(0.5)
            self.main_sound.play(loops =1, fade_ms= 5000)
            #print(settings.specialMusicNumber)
        
        #print(settings.specialMusicTrigger)
        if settings.specialMusicNumber == 1 and settings.specialMusicTrigger:
            settings.specialMusicTrigger = False
            settings.specialMusicNumber = 2
            self.main_sound.fadeout(2000)
            self.main_sound = load_sound('audio/SnowPixel.wav')
            self.main_sound.set_volume(0.5)
            self.main_sound.play(loops =1, fade_ms= 3000)
            #print(specialMusicNumber)
            #specialMusicNumber = 0
            #print("this is working")
            
        if settings.specialMusicNumber == 2 and settings.specialMusicTrigger:
            settings.specialMusicTrigger = False
            settings.specialMusicNumber = 3
            self.main_sound.fadeout(2000)
            self.main_sound = load_sound('audio/DesertDream.wav')
            self.main_sound.set_volume(0.5)
            self.main_sound.play(loops =1, fade_ms= 3000)
            #print(specialMusicNumber)
            
        if settings.specialMusicNumber == 3 and settings.specialMusicTrigger:
            settings.specialMusicTrigger = False
            settings.specialMusicNumber = 4
            self.main_sound.fadeout(2000)
            self.main_sound = load_sound('audio/PixelGhosts.wav')
            self.main_sound.set_volume(0.5)
            self.main_sound.play(loops =1, fade_ms= 3000)

        if settings.specialMusicNumber == 4 and settings.specialMusicTrigger:
            settings.specialMusicTrigger = False
            settings.specialMusicNumber = 5
            self.main_sound.fadeout(2000)
            self.main_sound = load_sound('audio/EpicShowdown.wav')
            self.main_sound.set_volume(0.5)
            self.main_sound.play(loops =1, fade_ms= 3000)

        if settings.specialMusicNumber == 5 and settings.specialMusicTrigger:
            settings.specialMusicTrigger = False
            settings.specialMusicNumber = 0
            self.main_sound.fadeout(2000)
            self.main_sound = load_sound('audio/Winning.wav')
            self.main_sound.set_volume(0.5)
            self.main_sound.play(loops =1, fade_ms= 3000)

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def run(self):
        # update and draw the game
        self.check_music()
        #print(settings.specialMusicTrigger)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.damage_penalty()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # General Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        # Creating the floor image
        self.floor_surf = load_image('graphics/tilemap/groundThesis.png').convert()  ###
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        # Getting the offset of camera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)


