import pygame
from Graphics import Image_Handler, Color_Handler


class TickBox:

    def __init__(self, x, y, start_value=False):

        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 32, 32)
        self.active = start_value
        self.tick_image = Image_Handler.get_image('tick')
        self.color = Color_Handler.Color('BLACK')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the input_box rect
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable
                self.active = not self.active

    def show(self, screen):
        # Draw the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)

        if self.active:
            screen.blit(self.tick_image, (self.x - 5, self.y - 18))
