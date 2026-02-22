import pygame
from support import import_folder
from random import choice
from loader import load_sound, load_image, resource_path


class AnimationPlayer:
    def __init__(self):
        self.frames = {
			# magic
			'flame': import_folder(resource_path('graphics/particles/flame/frames')),
			'aura': import_folder(resource_path('graphics/particles/aura')),
			'heal': import_folder(resource_path('graphics/particles/heal/frames')),
            'gravity': import_folder(resource_path('graphics/particles/gravity/frames')),
            'wave': import_folder(resource_path('graphics/particles/wave/frames')),
            'stoneSpell':import_folder(resource_path('graphics/particles/stoneSpell/frames')),
            'boltSpell':import_folder(resource_path('graphics/particles/boltSpell/frames')),
            'elementSpell':import_folder(resource_path('graphics/particles/elementSpell/frames')),
            'forceSpell':import_folder(resource_path('graphics/particles/forceSpell/frames')),
            'wheelSpell':import_folder(resource_path('graphics/particles/wheelSpell/frames')),
            'loopSpell':import_folder(resource_path('graphics/particles/loopSpell/frames')),

            'test':import_folder(resource_path('graphics/particles/flame/frames')),

			
			# attacks 
			'claw': import_folder(resource_path('graphics/particles/claw')),
			'slash': import_folder(resource_path('graphics/particles/slash')),
			'sparkle': import_folder(resource_path('graphics/particles/sparkle')),
			'leaf_attack': import_folder(resource_path('graphics/particles/leaf_attack')),
			'thunder': import_folder(resource_path('graphics/particles/thunder')),

			# monster deaths
			'squid': import_folder(resource_path('graphics/particles/smoke_orange')),
			'fg3white': import_folder(resource_path('graphics/particles/fg3white')),
			'spirit': import_folder(resource_path('graphics/particles/nova')),
			'fg1': import_folder(resource_path('graphics/particles/fg1')),
            'chargedspirit': import_folder(resource_path('graphics/particles/nova')),

            ### Need to add new monsters here
            'BlobGreenEnergy1': import_folder(resource_path('graphics/particles/nova')),
            'BlobGreenGrav1': import_folder(resource_path('graphics/particles/nova')),
            'BlobGreenGrav2': import_folder(resource_path('graphics/particles/nova')),
            'BlobGreenKin1': import_folder(resource_path('graphics/particles/nova')),
            'CoonBrownGrav3': import_folder(resource_path('graphics/particles/nova')),
            'CoonWhiteGrav3': import_folder(resource_path('graphics/particles/nova')),
            'SpikeWhiteEnergy2': import_folder(resource_path('graphics/particles/nova')),
            'SpikeWhiteKin1': import_folder(resource_path('graphics/particles/nova')),
            'SpikeWhiteKin2': import_folder(resource_path('graphics/particles/nova')),
            'SquidElect1': import_folder(resource_path('graphics/particles/nova')),
            'SquidEnergy3': import_folder(resource_path('graphics/particles/nova')),
            'SquidForce3': import_folder(resource_path('graphics/particles/nova')),
            'StoneManElect2': import_folder(resource_path('graphics/particles/nova')),
            'StoneManForce': import_folder(resource_path('graphics/particles/nova')),
            'BlackBlobEnergy1': import_folder(resource_path('graphics/particles/nova')),
            'BlackBlobKin1': import_folder(resource_path('graphics/particles/nova')),
            'BlackSpikeEnergy2': import_folder(resource_path('graphics/particles/nova')),
            'finalboss': import_folder(resource_path('graphics/particles/nova')),


            'music1': import_folder(resource_path('graphics/particles/nova')),
            'music2': import_folder(resource_path('graphics/particles/nova')),			
            'music3': import_folder(resource_path('graphics/particles/nova')),	
            'music4': import_folder(resource_path('graphics/particles/nova')),	

			# leafs 
			'leaf': (
				import_folder(resource_path('graphics/particles/leaf1')),
				import_folder(resource_path('graphics/particles/leaf2')),
				import_folder(resource_path('graphics/particles/leaf3')),
				import_folder(resource_path('graphics/particles/leaf4')),
				import_folder(resource_path('graphics/particles/leaf5')),
				import_folder(resource_path('graphics/particles/leaf6')),
				self.reflect_images(import_folder(resource_path('graphics/particles/leaf1'))),
				self.reflect_images(import_folder(resource_path('graphics/particles/leaf2'))),
				self.reflect_images(import_folder(resource_path('graphics/particles/leaf3'))),
				self.reflect_images(import_folder(resource_path('graphics/particles/leaf4'))),
				self.reflect_images(import_folder(resource_path('graphics/particles/leaf5'))),
				self.reflect_images(import_folder(resource_path('graphics/particles/leaf6')))
				)
			}


    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
            return new_frames
        
    def create_grass_particles(self, pos, groups):
          animation_frames = choice(self.frames['leaf'])
          ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)

    def create_flame_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        FlameEffect(pos, animation_frames, groups)

    def create_gravity_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        GravityEffect(pos, animation_frames, groups)

    def create_wave_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        WaveEffect(pos, animation_frames, groups)

    def create_stone_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        StoneSpellEffect(pos, animation_frames, groups)

    def create_bolt_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        BoltSpellEffect(pos, animation_frames, groups)

    def create_element_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ElementSpellEffect(pos, animation_frames, groups)

    def create_force_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ForceSpellEffect(pos, animation_frames, groups)

    def create_wheel_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        WheelSpellEffect(pos, animation_frames, groups)

    def create_loop_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        LoopSpellEffect(pos, animation_frames, groups)

class LoopSpellEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'loopSpell'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()

class WheelSpellEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'wheelSpell'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()

class ForceSpellEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'forceSpell'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()

class ElementSpellEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'elementSpell'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()


class BoltSpellEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'boltSpell'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()

class StoneSpellEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'stoneSpell'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()

class WaveEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'wave'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()

class GravityEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'gravity'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()


class FlameEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'flame'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    def update(self):
        self.animate()



class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'      # 6:23 for information of multiple types of spells
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)


    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)] 

    

    def update(self):
        self.animate()