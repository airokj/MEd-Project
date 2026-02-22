import pygame
from settings import *
from random import randint
from loader import load_sound


class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal':load_sound('audio/heal.wav'),
            'flame':load_sound('audio/Fire.wav')
        }


    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            self.sounds['heal'].play()
            player.health += strength

            
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0, -60), groups)



    def flame(self, player, cost, groups):
        if player.energy >= cost:
            self.sounds['flame'].play()
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 5):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_flame_particles('flame', (x, y), groups)                     

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_flame_particles('flame', (x, y), groups)     #Flame from Magic Data in Settings
                    


    def gravity(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_gravity_particles('gravity', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_gravity_particles('gravity', (x, y), groups)     #Flame from Magic Data in Settings
                    

    def wave(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_wave_particles('wave', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_wave_particles('wave', (x, y), groups)     #Flame from Magic Data in Settings


    def stoneSpell(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_stone_particles('stoneSpell', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_stone_particles('stoneSpell', (x, y), groups)     #Flame from Magic Data in Settings

    def boltSpell(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_bolt_particles('boltSpell', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_bolt_particles('boltSpell', (x, y), groups)     #Flame from Magic Data in Settings    

    def elementSpell(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x# + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery# + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_element_particles('elementSpell', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx# + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + offset_y# + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_element_particles('elementSpell', (x, y), groups)     #Flame from Magic Data in Settings  

    def forceSpell(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x# + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery# + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_force_particles('forceSpell', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx# + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + offset_y# + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_force_particles('forceSpell', (x, y), groups)     #Flame from Magic Data in Settings  

    def wheelSpell(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            for i in range(1, 3):
                if direction.x: # horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x# + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery# + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_wheel_particles('wheelSpell', (x, y), groups)

                else: # vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx# + randint(-TILESIZE//5, TILESIZE//5)
                    y = player.rect.centery + offset_y# + randint(-TILESIZE//5, TILESIZE//5)
                    self.animation_player.create_wheel_particles('wheelSpell', (x, y), groups)     #Flame from Magic Data in Settings  

    def loopSpell(self, player, cost, groups):
            if player.energy >= cost:
                player.energy -= cost

                if player.status.split('_')[0] == 'right':
                    direction = pygame.math.Vector2(1, 0)
                elif player.status.split('_')[0] == 'left':
                    direction = pygame.math.Vector2(-1, 0)
                elif player.status.split('_')[0] == 'up':
                    direction = pygame.math.Vector2(0, -1)
                elif player.status.split('_')[0] == 'down':
                    direction = pygame.math.Vector2(0, 1)

                for i in range(1, 3):
                    if direction.x: # horizontal
                        offset_x = (direction.x * i) * TILESIZE
                        x = player.rect.centerx + offset_x# + randint(-TILESIZE//5, TILESIZE//5)
                        y = player.rect.centery# + randint(-TILESIZE//5, TILESIZE//5)
                        self.animation_player.create_loop_particles('loopSpell', (x, y), groups)

                    else: # vertical
                        offset_y = (direction.y * i) * TILESIZE
                        x = player.rect.centerx# + randint(-TILESIZE//5, TILESIZE//5)
                        y = player.rect.centery + offset_y# + randint(-TILESIZE//5, TILESIZE//5)
                        self.animation_player.create_loop_particles('loopSpell', (x, y), groups)     #Flame from Magic Data in Settings  