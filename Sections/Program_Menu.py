import pygame
from Interface import Input_Box, Button, TickBox
from Graphics import Color_Handler, Image_Handler
from Mechanics import Pizza_Options

font = 'Graphics/y.n.w.u.a.y.ttf'


def program_menu(screen):
    def show_text():
        # UI
        text = pygame.font.Font(font, 50).render("Find the cheapest pizza", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (300, 90))
        text = pygame.font.Font(font, 30).render("Address", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 250))
        text = pygame.font.Font(font, 30).render("City", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 200))
        text = pygame.font.Font(font, 30).render("Size", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1250, 200))
        text = pygame.font.Font(font, 30).render("Toppings", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (695, 350))
        text = pygame.font.Font(font, 30).render("cm", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1385, 250))
        text = pygame.font.Font(font, 30).render("-", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1280, 250))
        text = pygame.font.Font(font, 30).render("Search only in currently opened pizzerias", True,
                                                 Color_Handler.Color('BLACK'))
        screen.blit(text, (220, 750))

        # TOPPINGS

        # FIRST COLUMN
        text = pygame.font.Font(font, 30).render("Anchois", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 400))
        text = pygame.font.Font(font, 30).render("Artichokes", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 450))
        text = pygame.font.Font(font, 30).render("Arugula", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 500))
        text = pygame.font.Font(font, 30).render("Bacon", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 550))
        text = pygame.font.Font(font, 30).render("Bell Pepper", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 600))
        text = pygame.font.Font(font, 30).render("Camembert", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (100, 650))

        # SECOND COLUMN
        text = pygame.font.Font(font, 30).render("Capers", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (480, 400))
        text = pygame.font.Font(font, 30).render("Chicken", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (480, 450))
        text = pygame.font.Font(font, 30).render("Corn", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (480, 500))
        text = pygame.font.Font(font, 30).render("Feta", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (480, 550))
        text = pygame.font.Font(font, 30).render("Garlic", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (480, 600))
        text = pygame.font.Font(font, 30).render("Ham", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (480, 650))

        # THIRD COLUMN
        text = pygame.font.Font(font, 30).render("Herbs", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (770, 400))
        text = pygame.font.Font(font, 30).render("Jalapeno", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (770, 450))
        text = pygame.font.Font(font, 30).render("Mozzarella", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (770, 500))
        text = pygame.font.Font(font, 30).render("Olives", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (770, 550))
        text = pygame.font.Font(font, 30).render("Onion", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (770, 600))
        text = pygame.font.Font(font, 30).render("Pineapple", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (770, 650))

        # FOURTH COLUMN

        text = pygame.font.Font(font, 30).render("Portobello", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1150, 400))
        text = pygame.font.Font(font, 30).render("Salami", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1150, 450))
        text = pygame.font.Font(font, 30).render("Sausage", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1150, 500))
        text = pygame.font.Font(font, 30).render("Sea Food", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1150, 550))
        text = pygame.font.Font(font, 30).render("Tomato", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1150, 600))
        text = pygame.font.Font(font, 30).render("Tuna", True, Color_Handler.Color('BLACK'))
        screen.blit(text, (1150, 650))

    def data_process(options):
        pass

    pizza_options = Pizza_Options.PizzaOptions()

    input_box1 = Input_Box.InputBox(460, 200, 30, 620, '', 'String')
    input_box2 = Input_Box.InputBox(460, 250, 30, 620, '', 'String')
    input_box3 = Input_Box.InputBox(1220, 250, 2, 50, '', 'Number')
    input_box4 = Input_Box.InputBox(1320, 250, 2, 50, '', 'Number')
    input_boxes = [input_box1, input_box2, input_box3, input_box4]

    button1 = Button.Button(560, 820, 300, 58, 'Search', 50, Button.Button.button_func_ret_Search())
    button2 = Button.Button(880, 820, 165, 58, 'Exit', 50, Button.Button.button_func_ret_Exit())
    buttons = [button1, button2]

    # FIRST COLUMN
    tick_box1 = TickBox.TickBox(400, 400)
    tick_box2 = TickBox.TickBox(400, 450)
    tick_box3 = TickBox.TickBox(400, 500)
    tick_box4 = TickBox.TickBox(400, 550)
    tick_box5 = TickBox.TickBox(400, 600)
    tick_box6 = TickBox.TickBox(400, 650)

    # SECOND COLUMN
    tick_box7 = TickBox.TickBox(680, 400)
    tick_box8 = TickBox.TickBox(680, 450)
    tick_box9 = TickBox.TickBox(680, 500)
    tick_box10 = TickBox.TickBox(680, 550)
    tick_box11 = TickBox.TickBox(680, 600)
    tick_box12 = TickBox.TickBox(680, 650)

    # THIRD COLUMN
    tick_box13 = TickBox.TickBox(1080, 400)
    tick_box14 = TickBox.TickBox(1080, 450)
    tick_box15 = TickBox.TickBox(1080, 500)
    tick_box16 = TickBox.TickBox(1080, 550)
    tick_box17 = TickBox.TickBox(1080, 600)
    tick_box18 = TickBox.TickBox(1080, 650)

    # FOURTH COLUMN
    tick_box19 = TickBox.TickBox(1440, 400)
    tick_box20 = TickBox.TickBox(1440, 450)
    tick_box21 = TickBox.TickBox(1440, 500)
    tick_box22 = TickBox.TickBox(1440, 550)
    tick_box23 = TickBox.TickBox(1440, 600)
    tick_box24 = TickBox.TickBox(1440, 650)

    # UI
    tick_box25 = TickBox.TickBox(1320, 750)

    tick_boxes = [tick_box1, tick_box2, tick_box3, tick_box4, tick_box5, tick_box6,
                  tick_box7, tick_box8, tick_box9, tick_box10, tick_box11, tick_box12,
                  tick_box13, tick_box14, tick_box15, tick_box16, tick_box17, tick_box18,
                  tick_box19, tick_box20, tick_box21, tick_box22, tick_box23, tick_box24, tick_box25]

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            for input_box in input_boxes:
                input_box.handle_event(event)

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

        for input_box in input_boxes:
            input_box.update()

        for button in buttons:
            button.update()

        # Show stuff

        screen.blit(background_image, (0, 0))

        show_text()

        for input_box in input_boxes:
            input_box.show(screen)

        for button in buttons:
            button.show(screen)

        for tick_box in tick_boxes:
            tick_box.show(screen)

        # Pygame mechanics stuff

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
