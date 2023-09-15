import pygame

class ConfigurePage:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 30)
        self.is_active = False
        self.AI_enable = False
        self.mode_rect = None
        self.close_rect = None
        self.player_control = True

    def draw(self,screen):
        # set screen size
        screen_width = 800
        screen_height = 750
        # colour defined
        black = (0, 0, 0)

        # Configure buttons
        font = pygame.font.Font(None, 48)
        configure_text = font.render("Configure", True, black)
        configure_rect = configure_text.get_rect(center=(screen_width // 2, screen_height // 7))

        font = pygame.font.Font(None, 36)
        fsize_button = font.render("Field Size: [375*750]", True, black)
        fsize_rect = fsize_button.get_rect(center=(screen_width // 2, screen_height // 5 + 60))

        gameLevel_button = font.render("Game Level: [2]", True, black)
        gameLevel_rect = gameLevel_button.get_rect(center=(screen_width // 2, screen_height // 5 + 120))

        extend_button = font.render("Extend: [CLOSE]", True, black)
        extend_rect = extend_button.get_rect(center=(screen_width // 2, screen_height // 5 + 180))

        mode_button = font.render(f"AI Mode: [{self.AI_enable}]", True, black)
        mode_rect = mode_button.get_rect(center=(screen_width // 2, screen_height // 5 + 240))

        close_button = font.render("Close", True, black)
        close_rect = close_button.get_rect(center=(screen_width // 2 + 260, screen_height // 1.5 + 160))

        screen.blit(configure_text, configure_rect)
        screen.blit(fsize_button, fsize_rect)
        screen.blit(gameLevel_button, gameLevel_rect)
        screen.blit(extend_button, extend_rect)
        screen.blit(mode_button, mode_rect)
        screen.blit(close_button, close_rect)

        self.mode_rect = mode_rect
        self.close_rect = close_rect
    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
