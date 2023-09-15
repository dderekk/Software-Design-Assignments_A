import pygame
import sys

pygame.init()

# Screen size
screen_width = 800
screen_height = 750
pygame.display.set_caption("Congratulation")

clock = pygame.time.Clock()


class enterData:
    def __init__(self):
        self.surface = pygame.Surface((300, 250))
        self.rect = self.surface.get_rect(center=(screen_width // 2, screen_height // 2))
        self.active = False
        self.text = ""
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        self.surface.fill((255, 255, 255))
        pygame.draw.rect(self.surface, (0, 0, 0), self.surface.get_rect(), 3)

        # Text input box
        txt_surface = self.font.render(self.text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)
        input_rect = pygame.Rect(50, 100, width, 50)
        pygame.draw.rect(self.surface, (0, 0, 0), input_rect, 2)

        self.surface.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = width

        # Blit the surface
        screen.blit(self.surface, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"User entered: {self.text}")
                    self.text = ""
                    return "DONE"
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        return None

    def whileloop(self):
        screen = pygame.display.set_mode((screen_width, screen_height))
        result = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                result = self.handle_event(event)
            if result == "DONE":
                self.active = False
                break

            screen.fill((30, 30, 30))
            if self.active:
                self.draw(screen)
            pygame.display.update()
            clock.tick(30)