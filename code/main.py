import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Adventure')
        self.clock = pygame.time.Clock()

        self.level = Level()

        ### Pausing attributes ###
        self.paused = False

        self.WHITE = (255, 255, 255)
        self.DARK_GREY = (50, 50, 50)
        self.font = pygame.font.Font(None, 50)

        # Sound
#        main_sound = pygame.mixer.Sound('../audio/WhispersWoods.wav')
#        main_sound.set_volume(0.5)
#        main_sound.play(loops =1)

    def draw_pause_screen(self):

        # Step 1: Capture the current game screen **after** the game is drawn
        dark_overlay = self.screen.copy()

        # Step 2: Darken the screen using color blending
        dark_surface = pygame.Surface((WIDTH, HEIGHT))
        dark_surface.fill((50, 50, 50))  # Dark gray
        dark_overlay.blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

        # Step 3: Draw the darkened overlay **after** everything else
        self.screen.blit(dark_overlay, (0, 0))

        text = self.font.render("Game Paused", True, self.WHITE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.screen.blit(text, text_rect)

        text2 = self.font.render("Press Space to Unpause, or ESC to exit game.", True, self.WHITE)
        text2_rect = text.get_rect(center=(WIDTH//2 - 240, (HEIGHT - HEIGHT//4) - 100))
        self.screen.blit(text2, text2_rect)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    #### Add keygrab here?
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
            
            self.screen.fill('black')

            if not self.paused:
                self.level.run()

            if self.paused:
                self.draw_pause_screen()
            


            
            
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
