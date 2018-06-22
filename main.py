import pygame
from Interface import Input_Box, Button, TickBox
from Graphics import Color_Handler, Image_Handler
from Mechanics import Pizza_Options, Url_Getter, Url_Parser

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
        options.size_min = int(input_box3.text)
        options.size_max = int(input_box4.text)
        options.city = input_box1.text
        options.address = input_box2.text
        options.anchois = tick_box1.active
        options.artichokes = tick_box2.active
        options.arugula = tick_box3.active
        options.bacon = tick_box4.active
        options.bell_pepper = tick_box5.active
        options.camembert = tick_box6.active
        options.capers = tick_box7.active
        options.chicken = tick_box8.active
        options.corn = tick_box9.active
        options.feta = tick_box10.active
        options.garlic = tick_box11.active
        options.ham = tick_box12.active
        options.herbs = tick_box13.active
        options.jalapeno = tick_box14.active
        options.mozzarella = tick_box15.active
        options.olives = tick_box16.active
        options.onion = tick_box17.active
        options.pineapple = tick_box18.active
        options.portobello = tick_box19.active
        options.salami = tick_box20.active
        options.sausage = tick_box21.active
        options.seafood = tick_box22.active
        options.tomato = tick_box23.active
        options.tuna = tick_box24.active
        options.only_opened = tick_box25.active
        if options.size_correct() and options.address_correct():
            return True
        else:
            return False

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
                    if data_process(pizza_options):
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


def program_main(pizza_options):
    # SHOW WAITING INFO
    screen.blit(background_image, (0, 0))
    text = pygame.font.Font(font, 50).render("Searching for the cheapest pizza...", True, Color_Handler.Color('BLACK'))
    screen.blit(text, (75, 400))
    text = pygame.font.Font(font, 30).render("(This might take a while)", True, Color_Handler.Color('BLACK'))
    screen.blit(text, (510, 470))
    pygame.display.flip()
    pygame.display.update()

    # GETTING PROPER URL
    wait_time = 2

    while True:
        main_url = Url_Getter.Get_Url(pizza_options.city, pizza_options.address, wait_time)
        if main_url == 'Wrong address':
            print('Wrong address')
            pygame.quit()
            quit()
        elif main_url != 'https://www.pyszne.pl/':
            print('Address found - ' + main_url)
            break
        elif main_url == 'https://www.pyszne.pl/':
            wait_time += 1

    # PARSING DATA

    parsed_url = Url_Parser.Url_Parser(main_url)

    # BY THIS POINT, DATA IS GATHERED

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # UPDATE STUFF

        # SHOW STUFF

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


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
# PARSING
url = 'https://google.com'
values = {}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url)  # , data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData.decode('utf-8'))
'''
