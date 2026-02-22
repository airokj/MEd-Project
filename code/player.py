import pygame
from settings import *
import settings
from support import import_folder
from entity import Entity
from loader import load_sound, load_image, resource_path

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, despawn_weapon, create_magic):
        super().__init__(groups)
        self.image= load_image('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET['player'])

        # graphics setup
        self.import_player_assets()
        self.status = 'down'


        # Movement

        #self.speed = 5 # Moved to stats
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack

        self.obstacle_sprites = obstacle_sprites

        # weapon config
        self.create_attack = create_attack
        self.despawn_weapon = despawn_weapon
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # magic config
        self.create_magic = create_magic
        
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        #### Testing Config ####                                    ########################
        self.can_switch_bolt = True
        self.bolt_switch_time = None

        self.can_switch_heal = True
        self.heal_switch_time = None

        self.can_switch_gravity = True
        self.gravity_switch_time = None
        
        self.can_switch_wave = True
        self.wave_switch_time = None

        self.can_switch_stone = True
        self.stone_switch_time = None

        self.can_switch_element = True
        self.element_switch_time = None

        self.can_switch_force = True
        self.force_switch_time = None

        self.can_switch_wheel = True
        self.wheel_switch_time = None

        self.can_switch_loop = True
        self.loop_switch_time = None
        ########################
        

        # Player stats
        self.stats = {
            'health': 100,
            'energy': 60,
            'attack': 1000,
            'magic': 4,
            'speed': 5,
            'music': 1
        }
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 0
        self.speed = self.stats['speed']
        self.music = self.stats['music']


        # Damage Timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnarability_duration = 500


        # Import Sounds
        self.weapon_attack_sound = load_sound('audio/sword.wav')
        self.weapon_attack_sound.set_volume(0.4)

    def import_player_assets(self):
        character_path = resource_path('graphics/player/')
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
            'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        global specialMusicNumber
        magic_cost = 10
        if not self.attacking:
            keys = pygame.key.get_pressed()

 #           if keys[pygame.K_e]:
 #               print(specialMusicNumber)         

            # Movement Inputs
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # Attack inputs
            if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.weapon_attack_sound.play()

            if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_magic('flame', 500, magic_cost*0+1)    #(spell style, strength, cost)

            if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    

            # Magic inputs
            ### Moved to end
            
            ##### Testing
            if keys[pygame.K_u] and self.can_switch_bolt:
                self.attacking = True
                self.can_switch_bolt = False
                self.attack_time = pygame.time.get_ticks()
                self.bolt_switch_time = pygame.time.get_ticks()

                self.create_magic('boltSpell', 1, magic_cost)    #(spell style, strength, cost)

            if keys[pygame.K_i] and self.can_switch_element:
                self.attacking = True
                self.can_switch_element = False
                self.attack_time = pygame.time.get_ticks()
                self.element_switch_time = pygame.time.get_ticks()

                self.create_magic('elementSpell', 1, magic_cost)

            if keys[pygame.K_o] and self.can_switch_gravity:
                self.attacking = True
                self.can_switch_gravity = False
                self.attack_time = pygame.time.get_ticks()
                self.gravity_switch_time = pygame.time.get_ticks()

                self.create_magic('gravity', 1, magic_cost)

            if keys[pygame.K_l] and self.can_switch_force:
                self.attacking = True
                self.can_switch_force = False
                self.attack_time = pygame.time.get_ticks()
                self.force_switch_time = pygame.time.get_ticks()

                self.create_magic('forceSpell', 1, magic_cost)

            if keys[pygame.K_PERIOD] and self.can_switch_wave:
                self.attacking = True
                self.can_switch_wave = False
                self.attack_time = pygame.time.get_ticks()
                self.wave_switch_time = pygame.time.get_ticks()

                self.create_magic('wave', 1, magic_cost)

            if keys[pygame.K_COMMA] and self.can_switch_stone:
                self.attacking = True
                self.can_switch_stone = False
                self.attack_time = pygame.time.get_ticks()
                self.stone_switch_time = pygame.time.get_ticks()

                self.create_magic('stoneSpell', 1, magic_cost)

            if keys[pygame.K_m] and self.can_switch_wheel:
                self.attacking = True
                self.can_switch_wheel = False
                self.attack_time = pygame.time.get_ticks()
                self.wheel_switch_time = pygame.time.get_ticks()

                self.create_magic('wheelSpell', 1, magic_cost)

            if keys[pygame.K_j] and self.can_switch_loop:
                self.attacking = True
                self.can_switch_loop = False
                self.attack_time = pygame.time.get_ticks()
                self.loop_switch_time = pygame.time.get_ticks()

                self.create_magic('loopSpell', 1, magic_cost)

            if keys[pygame.K_k] and self.can_switch_heal:
                self.attacking = True
                self.can_switch_heal = False
                self.attack_time = pygame.time.get_ticks()
                self.heal_switch_time = pygame.time.get_ticks()

                self.create_magic('heal', 20, magic_cost)

            ####

            # Switch Weapon/Spells

            if keys[pygame.K_k] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index +=1
                else:
                    self.weapon_index = 0

                self.weapon = list(weapon_data.keys())[self.weapon_index]


### Remove this

### Moved to end
                
###


    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    # overwrite idle
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')



    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.despawn_weapon()


        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

#####
        if not self.can_switch_bolt:
            if current_time - self.bolt_switch_time >= self.switch_duration_cooldown:
                self.can_switch_bolt = True
        
        if not self.can_switch_gravity:
            if current_time - self.gravity_switch_time >= self.switch_duration_cooldown:
                self.can_switch_gravity = True
        
        if not self.can_switch_wave:
            if current_time - self.wave_switch_time >= self.switch_duration_cooldown:
                self.can_switch_wave = True

        if not self.can_switch_stone:
            if current_time - self.stone_switch_time >= self.switch_duration_cooldown:
                self.can_switch_stone = True

        if not self.can_switch_element:
            if current_time - self.element_switch_time >= self.switch_duration_cooldown:
                self.can_switch_element = True

        if not self.can_switch_force:
            if current_time - self.force_switch_time >= self.switch_duration_cooldown:
                self.can_switch_force = True

        if not self.can_switch_wheel:
            if current_time - self.wheel_switch_time >= self.switch_duration_cooldown:
                self.can_switch_wheel = True

        if not self.can_switch_loop:
            if current_time - self.loop_switch_time >= self.switch_duration_cooldown:
                self.can_switch_loop = True

        if not self.can_switch_heal:
            if current_time - self.heal_switch_time >= self.switch_duration_cooldown:
                self.can_switch_heal = True
#####

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnarability_duration:
                self.vulnerable = True
            
        

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        # Flicker


    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def get_full_magic_damage(self):
        base_damage = self.stats['magic']
        spell_damage = magic_data[self.magic]['strength']
        return spell_damage


    def energy_recovery(self):
        #print(self.exp)
        if self.exp >= 5000:
            eRate = 0.035
        elif self.exp >= 2500:
            eRate = 0.03
        else:
            eRate = 0.02

        if self.energy < self.stats['energy']:
            self.energy += eRate * self.stats['magic']
        else:
            self.energy = self.stats['energy']

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.energy_recovery()



####
'''
            if keys[pygame.K_m]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic'] # Adds magic stat to spell power
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style, strength, cost)
                print(style)
                print(strength)
                print(cost)

            if keys[pygame.K_COMMA] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()

                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index +=1
                else:
                    self.magic_index = 0

                self.magic = list(magic_data.keys())[self.magic_index]
'''