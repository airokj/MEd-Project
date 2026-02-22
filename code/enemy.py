import pygame
from settings import *
from entity import Entity
from support import *
from loader import load_sound, resource_path

import settings
#specialMusicNumber2 = 1
#settings.specialMusicTrigger = True

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player, trigger_death_particles, add_exp):

        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index].copy()
        #self.imageCopy = self.image.copy()

        # Movement

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # Enemy Stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']
        self.music = monster_info['musicPlay']
        self.last_damage = 0
        self.just_got_hit_time = 0
        self.tint_duration = 200

        self.knockback = False
        self.knockback_timer = 0
        self.knockback_duration = 200

        # Player Interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.add_exp = add_exp

        # Invincibility Timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

        # Sounds
        self.death_sound = load_sound('audio/death.wav')
        self.hit_sound = load_sound('audio/hit.wav')
        self.attack_sound = load_sound(monster_info['attack_sound'])
        self.death_sound.set_volume(0.2)
        self.hit_sound.set_volume(0.2)
        self.attack_sound.set_volume(0.3)

        # Game Sound
#        grassMusic = '../audio/WhispersWoods.wav'
#        snowMusic = '../audio/SnowPixel.wav'
#        desertMusic = '../audio/DesertDream.wav'
#        darkMusic = '../audio/PixelGhosts.wav'
#        bossMusic = '../audio/EpicShowdown.wav'
        

    def import_graphics(self, name):
        self.animations ={'idle':[], 'move':[], 'attack':[], 'attack2':[]}
        main_path = resource_path(f'graphics/monsters/{name}/')
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude() #converts the vector into a distance
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack' and self.status != 'attack2':
                self.frame_index = 0
            if self.monster_name == 'finalboss':
                if settings.finalBoss == 1:
                    self.status = 'attack'
                    settings.finalBoss = 2

                elif settings.finalBoss == 2:
                    self.status = 'attack2'
                    settings.finalBoss = 1

            else:        
                self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

            '''
        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'
            '''


    def actions(self, player):
        
        current_time = pygame.time.get_ticks()
        if self.knockback:
            if current_time - self.knockback_timer >= self.knockback_duration:
                self.knockback = False
            return


        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage, self.attack_type)
            self.attack_sound.play()

        elif self.status == 'attack2':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage, self.attack_type)
            self.attack_sound.play()

        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()


    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            elif self.status == 'attack2':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
                                                                            ################
        if not self.vulnerable:
            # Flicker effect
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:

            if self.attack_time is not None and current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True


    def get_damage(self, player, attack_type):
        self.last_damage = 0 #reset damage frame

        forceList = ['BlobGreenGrav1', 'BlobGreenGrav2', 'CoonBrownGrav3', 'CoonWhiteGrav3', 'SquidForce3', 'StoneManForce']
        electList = ['SquidElect1', 'StoneManElect2', 'finalboss']
        velocityList = ['BlobGreenKin1', 'SpikeWhiteKin1', 'SpikeWhiteKin2', 'BlackBlobKin1']
        energyList = ['BlobGreenEnergy1', 'SpikeWhiteEnergy2', 'SquidEnergy3', 'BlackBlobEnergy1', 'BlackSpikeEnergy2']

        forceAttack = ['gravity', 'forceSpell']
        electAttack = ['boltSpell', 'elementSpell']
        velocityAttack = ['wheelSpell', 'loopSpell']
        energyAttack = ['wave', 'stoneSpell']

        if self.vulnerable:
            self.hit_sound.play()
            self.monster = list(monster_data.keys())
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
                self.last_damage = player.get_full_weapon_damage()
                damage = player.get_full_weapon_damage() *50
                
                #print(self.monster_name)


            elif attack_type == 'flame': # and self.monster_name == 'fg1':                         ################
                self.health -= player.get_full_magic_damage() *500
                self.last_damage = player.get_full_magic_damage() *500
                damage = player.get_full_magic_damage() *500

            elif attack_type in forceAttack and self.monster_name in forceList:
                self.health -= player.get_full_magic_damage() *50
                self.last_damage = player.get_full_magic_damage() *50
                damage = player.get_full_magic_damage() *50


            elif attack_type in electAttack and self.monster_name in electList:
                self.health -= player.get_full_magic_damage() *50
                self.last_damage = player.get_full_magic_damage() *50
                damage = player.get_full_magic_damage() *50

            elif attack_type in velocityAttack and self.monster_name in velocityList:
                self.health -= player.get_full_magic_damage() *50
                self.last_damage = player.get_full_magic_damage() *50
                damage = player.get_full_magic_damage() *50

            elif attack_type in energyAttack and self.monster_name in energyList:
                self.health -= player.get_full_magic_damage() *50
                self.last_damage = player.get_full_magic_damage() *50
                damage = player.get_full_magic_damage() *50

            else:
                # Magic Damage
                self.health -= player.get_full_magic_damage() *0+1
                self.last_damage = player.get_full_magic_damage() *0+1
                damage = player.get_full_magic_damage() *0+1
                #print(attack_type)



            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False
            if damage > 1:
                self.just_got_hit_time = pygame.time.get_ticks()
                self.knockback = True
                self.knockback_timer = pygame.time.get_ticks()
                self.direction *= -self.resistance
            
            ##
            


    def hit_reaction(self):

        #self.imageCopy = self.image.copy()
        current_time = pygame.time.get_ticks()
        self.image = self.animations[self.status][int(self.frame_index)].copy()

        if not self.vulnerable:
            if not self.knockback:
                self.direction *= -self.resistance
                self.knockback = True

            

            alpha = self.wave_value()
            self.image.set_alpha(alpha)

            if current_time - self.just_got_hit_time < self.tint_duration:
                red_tint = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
                red_tint.fill((255, 0, 0, 255))
                self.image.blit(red_tint, (0, 0), special_flags = pygame.BLEND_RGB_ADD)
            
        else:
            #self.image = self.animations[self.status][int(self.frame_index)].copy()
            self.image.set_alpha(255)
            self.knockback = False





    def check_death(self):
        global specialMusicNumber
        global specialMusicTrigger

        if self.health <=0:
            if self.monster_name == 'music1':
                specialMusicNumber = 1
                settings.specialMusicTrigger = True
                
            if self.monster_name == 'music2':
                settings.specialMusicNumber = 2
                settings.specialMusicTrigger = True

            if self.monster_name == 'music3':
                settings.specialMusicNumber = 3
                settings.specialMusicTrigger = True

            if self.monster_name == 'music4':
                settings.specialMusicNumber = 4
                settings.specialMusicTrigger = True
            
            greenList = ['BlobGreenGrav1', 'BlobGreenGrav2', 'BlobGreenEnergy1', 'BlobGreenKin1', 'CoonBrownGrav3']
            electList = ['SquidElect1', 'StoneManElect2']

            if self.monster_name in greenList:
                settings.GREEN += 1

            if self.monster_name in electList:
                settings.ELECT +=1
            
            if self.monster_name == 'finalboss':
                settings.BOSS += 1
                settings.specialMusicNumber = 5
                settings.specialMusicTrigger = True

            if self.monster_name != 'null':
                settings.ALLEN += 1

            self.kill()
            self.trigger_death_particles(self.rect.center, self.monster_name)
            self.add_exp(self.exp)
            self.death_sound.play()
           

        if self.status == 'attack' and self.monster_name == 'music1':
            self.health -= 1

        if self.status == 'attack' and self.monster_name == 'music2':
            self.health -= 1

        if self.status == 'attack' and self.monster_name == 'music3':
            self.health -= 1

        if self.status == 'attack' and self.monster_name == 'music4':
            self.health -= 1

    def update(self):
        
        
        self.move(self.speed)
        self.animate()
        self.hit_reaction()

        self.last_damage = 0

        self.cooldowns()
        self.check_death()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)


###