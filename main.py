import pygame
from Interface import String_Input_Box, Button, TickBox
from Graphics import Color_Handler, Image_Handler
from Mechanics import Pizza_Options

pygame.init()

screen = pygame.display.set_mode((1600, 900), 0, 32)


def get_center():
    return int(screen.get_size()[0] / 2), int(screen.get_size()[1] / 2)


font = 'Graphics/y.n.w.u.a.y.ttf'
background_image = Image_Handler.get_image('background')
program_name = "Cheapest pizza"
pygame.display.set_caption(program_name)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((0, 0, 0))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 100)
screen.blit(surface, (0, 0))


def program_menu():

    def data_process(options):
        pass

    pizza_options = Pizza_Options.PizzaOptions()

    string_input_box1 = String_Input_Box.StringInputBox(460, 250, 10, 180, '')
    string_input_box2 = String_Input_Box.StringInputBox(680, 250, 30, 470, '')
    string_input_boxes = [string_input_box1, string_input_box2]

    button1 = Button.Button(560, 820, 300, 58, 'Search', 50, Button.Button.button_func_ret_Search())
    button2 = Button.Button(880, 820, 165, 58, 'Exit', 50, Button.Button.button_func_ret_Exit())
    buttons = [button1, button2]

    tick_box1 = TickBox.TickBox(200, 200)
    tick_boxes = [tick_box1]

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            for string_input_box in string_input_boxes:
                string_input_box.handle_event(event)

            for button in buttons:

                ret_val = button.handle_event(event)

                if ret_val == Button.ButtonFunctions.EXIT:
                    pygame.quit()
                    quit()

                elif ret_val == Button.ButtonFunctions.SEARCH:
                    data_process(pizza_options)
                    return True, pizza_options

            for tick_box in tick_boxes:
                tick_box.handle_event(event)

        # Update stuff

        for string_input_box in string_input_boxes:
            string_input_box.update()

        for button in buttons:
            button.update()

        # Show stuff

        screen.blit(background_image, (0, 0))

        text = pygame.font.Font(font, 50).render("Find the cheapest pizza", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (300, 90))
        text = pygame.font.Font(font, 30).render("Address", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (800, 200))
        text = pygame.font.Font(font, 30).render("City", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (500, 200))
        text = pygame.font.Font(font, 30).render("Size", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (300, 300))
        text = pygame.font.Font(font, 30).render("Toppings", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (600, 300))

        for string_input_box in string_input_boxes:
            string_input_box.show(screen)

        for button in buttons:
            button.show(screen)

        for tick_box in tick_boxes:
            tick_box.show(screen)

        # Pygame mechanics stuff

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def program_main(pizza_options):
    pass

def program_end():
    pass


if __name__ == '__main__':

    menu = True
    main = False
    end = False

    while True:

        if menu:
            menu_end, pizza_options = program_menu()
            if menu_end:
                menu = False
                main = True
                end = False
        elif main:
            main_end = program_main(pizza_options)
            if main_end:
                menu = False
                main = False
                end = True
        elif end:
            end_end = program_end()
            if end_end:
                pass

'''
import urllib.request
import urllib.parse
import re


url = 'http://pythonprogramming.net'
values = {'s': 'basics',
          'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''
