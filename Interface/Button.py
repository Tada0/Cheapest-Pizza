import pygame
from enum import Enum
from Graphics.Color_Handler import Color


class ButtonFunctions(Enum):
    QUIT = 1
    SEARCH = 2
    MENU = 3
    AGAIN = 4
    LEFT = 5
    RIGHT = 6
    EXIT = 7


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

    @staticmethod
    def button_func_ret_Again():
        return ButtonFunctions.AGAIN

    @staticmethod
    def button_func_ret_Left():
        return ButtonFunctions.LEFT

    @staticmethod
    def button_func_ret_Right():
        return ButtonFunctions.RIGHT

    def __init__(self, x, y, w, h, text, text_size, functionality, imgs=None):

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
        self.imgs = imgs

        if self.imgs:
            self.show_img = self.imgs[0]
        else:
            self.show_img = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and self.rect.collidepoint(mouse):
                return self.functionality

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.show_img:
                self.show_img = self.imgs[1]
            self.color = self.color_1
        else:
            if self.show_img:
                self.show_img = self.imgs[0]
            self.color = self.color_2

    def show(self, screen):
        # pygame.draw.rect(screen, Color("RED"), self.rect)  # For debugging
        # Draw button
        if self.show_img:
            screen.blit(self.show_img, (self.x, self.y))
        else:
            text = pygame.font.Font(self.font, self.text_size).render(self.text, True, self.color)
            screen.blit(text, (self.x, self.y))
