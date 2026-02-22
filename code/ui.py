import pygame
from settings import *
import settings
from loader import load_sound, resource_path

badgeChange = True
activeBadge = False

badgeSprite1 = True

class UI: 
    def __init__(self):

        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        ### Test temp surface
        #self.temp_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        #transGrey = (30, 30, 30, 128)
        self.overlay_image = pygame.image.load(resource_path('graphics/badges/badgeHolder/badgeHolder.png')).convert_alpha()
        self.allEnBadge = pygame.image.load(resource_path('graphics/badges/allEnBadge/0.png')).convert_alpha()
        self.bigScoreBadge = pygame.image.load(resource_path('graphics/badges/bigScoreBadge/0.png')).convert_alpha()
        self.bossBadge = pygame.image.load(resource_path('graphics/badges/bossBadge/0.png')).convert_alpha()
        self.electBadge = pygame.image.load(resource_path('graphics/badges/electBadge/0.png')).convert_alpha()
        self.greenBadge = pygame.image.load(resource_path('graphics/badges/greenBadge/0.png')).convert_alpha()

        self.allEnBadgeA = pygame.image.load(resource_path('graphics/badges/allEnBadge/1.png')).convert_alpha()
        self.bigScoreBadgeA = pygame.image.load(resource_path('graphics/badges/bigScoreBadge/1.png')).convert_alpha()
        self.bossBadgeA = pygame.image.load(resource_path('graphics/badges/bossBadge/1.png')).convert_alpha()
        self.electBadgeA = pygame.image.load(resource_path('graphics/badges/electBadge/1.png')).convert_alpha()
        self.greenBadgeA = pygame.image.load(resource_path('graphics/badges/greenBadge/1.png')).convert_alpha()

        self.spellGroups = pygame.image.load(resource_path('graphics/particles/spellGroups/spellGroupings.png')).convert_alpha()
        self.controlButtons = pygame.image.load(resource_path('graphics/particles/spellGroups/controls.png')).convert_alpha()

        # Bar Setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # Convert Weapon Dictionary to List
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = resource_path(weapon['graphic'])
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        self.magic_graphics = []
        for magic in magic_data.values():
            path = resource_path(magic['graphic'])  # Ensure correct path
            magic_image = pygame.image.load(path).convert_alpha()  # Load the image
            self.magic_graphics.append(magic_image)


    def show_bar(self, current,max_amount,bg_rect, colour):
        # draw the BG
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, bg_rect)

        # convert stat to pixels
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar itself
        pygame.draw.rect(self.display_surface, colour, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, bg_rect, 3)

    def show_exp(self,exp):
        text_surf = self.font.render("Score: " + str(int(exp)), False, TEXT_COLOUR)
        x = self.display_surface.get_size()[0] - 325
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright = (x,y))
        global bEXP 
        bEXP = int(exp)

        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, text_rect.inflate(20, 20))

        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, text_rect.inflate(20, 20), 3)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)

        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self, weapon_index,has_switched):
        bg_rect = self.selection_box(10, 830, has_switched) # weapon        Sent off screen. Can't see it.
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)


        self.display_surface.blit(weapon_surf, weapon_rect)

    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(95, 630, has_switched) # magic
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 
################################################
    def magic_overlay_U(self, has_switched):
        bg_rect = self.selection_box(1010, 450, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/boltSpell/boltSpell.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect)     

    def magic_overlay_I(self, has_switched):
        bg_rect = self.selection_box(1105-10, 460-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/elementSpell/elementSpell.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 
    
    def magic_overlay_O(self, has_switched):
        bg_rect = self.selection_box(1190-10, 460-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/gravity/gravity.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 

    def magic_overlay_J(self, has_switched):
        bg_rect = self.selection_box(1020-10, 545-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/loopSpell/loopSpell.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 
    
    def magic_overlay_K(self, has_switched):
        bg_rect = self.selection_box(1105-10, 545-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/heal/heal.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 

    def magic_overlay_L(self, has_switched):
        bg_rect = self.selection_box(1190-10, 545-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/forceSpell/forceSpell.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 
    
    def magic_overlay_M(self, has_switched):
        bg_rect = self.selection_box(1020-10, 630-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/wheelSpell/wheelSpell.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 

    def magic_overlay_COMMA(self, has_switched):
        bg_rect = self.selection_box(1105-10, 630-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/stoneSpell/stoneSpell.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 

    def magic_overlay_PERIOD(self, has_switched):
        bg_rect = self.selection_box(1190-10, 630-10, has_switched) # magic
        magic_surf = pygame.image.load(resource_path('graphics/particles/wave/wave.png')).convert_alpha()
        magic_rect = magic_surf.get_rect(center = bg_rect.center)    

        self.display_surface.blit(magic_surf, magic_rect) 
###############################################
    def spell_Group_Connections(self):
        self.display_surface.blit(self.spellGroups, (990, 410))

    def controls(self):
        self.display_surface.blit(self.controlButtons, (7, 520))



    def badge_holder_overlay(self):
        self.display_surface.blit(self.overlay_image, (10, 630))
        global badgeChange
        global activeBadge
        global badgeSprite1
        #print(settings.GREEN)
        if settings.GREEN == 24: #24
                # Check if the badge timer has been started
            if not hasattr(self, "green_badge_timer"):
                self.green_badge_timer = pygame.time.get_ticks()  # Store the current time
            # Calculate elapsed time
            elapsed_time = pygame.time.get_ticks() - self.green_badge_timer
            if elapsed_time < 500:  # Show self.greenBadgeA for 1 second
                self.display_surface.blit(self.greenBadgeA, (20, 640))
            else:  # Replace with self.greenBadge permanently
                self.display_surface.blit(self.greenBadge, (20, 640))



            #self.display_surface.blit(self.greenBadgeA, (20, 640))
            #self.display_surface.blit(self.greenBadge, (20, 640))

        if settings.ELECT == 7: #7
            if not hasattr(self, "elect_badge_timer"):
                self.elect_badge_timer = pygame.time.get_ticks()  # Store the current time
            # Calculate elapsed time
            elapsed_time2 = pygame.time.get_ticks() - self.elect_badge_timer
            if elapsed_time2 < 500:  # Show self.electBadgeA for 1 second
                self.display_surface.blit(self.electBadgeA, (84, 640))
            else:  # Replace with self.electBadge permanently
                self.display_surface.blit(self.electBadge, (84, 640))

            #self.display_surface.blit(self.electBadge, (84, 640))
        if settings.ALLEN == 74: #74
            if not hasattr(self, "allEn_badge_timer"):
                self.allEn_badge_timer = pygame.time.get_ticks()  # Store the current time
            # Calculate elapsed time
            elapsed_time3 = pygame.time.get_ticks() - self.allEn_badge_timer
            if elapsed_time3 < 500:  # Show self.greenBadgeA for 1 second
                self.display_surface.blit(self.allEnBadgeA, (212, 640))
            else:  # Replace with self.greenBadge permanently
                self.display_surface.blit(self.allEnBadge, (212, 640))
            #self.display_surface.blit(self.allEnBadge, (212, 640))
        if settings.BOSS == 1: 
            if not hasattr(self, "boss_badge_timer"):
                self.boss_badge_timer = pygame.time.get_ticks()  # Store the current time
            # Calculate elapsed time
            elapsed_time5 = pygame.time.get_ticks() - self.boss_badge_timer
            if elapsed_time5 < 500:  # Show self.greenBadgeA for 1 second
                self.display_surface.blit(self.bossBadgeA, (276, 640))
            else:  # Replace with self.greenBadge permanently
                self.display_surface.blit(self.bossBadge, (276, 640))

                text_message1 = self.font.render("Congratulations!", True, (255, 255, 255))
                text_rect = text_message1.get_rect(center=(WIDTH/2, HEIGHT/5))
                self.display_surface.blit(text_message1, text_rect)

                text_message2 = self.font.render("You defeated the boss!", True, (255, 255, 255))
                text_rect = text_message2.get_rect(center=(WIDTH/2, HEIGHT/5 + 50))
                self.display_surface.blit(text_message2, text_rect)

                text_message3 = self.font.render("But, did you collect all the badges?", True, (255, 255, 255))
                text_rect = text_message3.get_rect(center=(WIDTH/2, HEIGHT/5 + 100))
                self.display_surface.blit(text_message3, text_rect)

            #self.display_surface.blit(self.bossBadge, (276, 640))
        if bEXP > 6500 and badgeChange:
            badgeChange = False
            activeBadge = True
        if activeBadge:
            if not hasattr(self, "bigScore_badge_timer"):
                self.bigScore_badge_timer = pygame.time.get_ticks()  # Store the current time
            # Calculate elapsed time
            elapsed_time4 = pygame.time.get_ticks() - self.bigScore_badge_timer
            if elapsed_time4 < 500:  # Show self.greenBadgeA for 1 second
                self.display_surface.blit(self.bigScoreBadgeA, (148, 640))
            else:  # Replace with self.greenBadge permanently
                self.display_surface.blit(self.bigScoreBadge, (148, 640))
            #self.display_surface.blit(self.bigScoreBadge, (148, 640))

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOUR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOUR)
        
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        #self.selection_box(95, 630) # magic
        #self.magic_overlay(player.magic_index, not player.can_switch_magic)

        ###
        self.magic_overlay_U(not player.can_switch_bolt)
        self.magic_overlay_I(not player.can_switch_element)
        self.magic_overlay_O(not player.can_switch_gravity)
        self.magic_overlay_J(not player.can_switch_loop)
        self.magic_overlay_K(not player.can_switch_heal)
        self.magic_overlay_L(not player.can_switch_force)
        self.magic_overlay_M(not player.can_switch_wheel)
        self.magic_overlay_COMMA(not player.can_switch_stone)
        self.magic_overlay_PERIOD(not player.can_switch_wave)

        self.spell_Group_Connections()
        self.controls()
        
        self.badge_holder_overlay()

