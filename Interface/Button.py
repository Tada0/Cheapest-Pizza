import pygame
from enum import Enum
from Graphics.Color_Handler import Color


class ButtonFunctions(Enum):
    QUIT = 1
    SEARCH = 2
    MENU = 3
    EXIT = 4


class Button:

    @staticmethod
    def button_func_ret_Quit():
        return ButtonFunctions.QUIT

    @staticmethod
    def button_func_ret_Search():
        return ButtonFunctions.SEARCH

    @staticmethod
    def button_func_ret_Menu():
        return ButtonFunctions.MENU

    @staticmethod
    def button_func_ret_Exit():
        return ButtonFunctions.EXIT

    def __init__(self, x, y, w, h, text, text_size, functionality):

        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.font = 'Graphics/y.n.w.u.a.y.ttf'
        self.functionality = functionality
        self.color_2 = Color("BLACK")
        self.color_1 = Color("WHITE")
        self.text_size = text_size

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and self.rect.collidepoint(mouse):
                return self.functionality

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.color_1
        else:
            self.color = self.color_2

    def show(self, screen):
        # pygame.draw.rect(screen, Color("RED"), self.rect) # For debugging
        # Draw button text
        text = pygame.font.Font(self.font, self.text_size).render(self.text, True, self.color)
        screen.blit(text, (self.x, self.y))
