import pygame
from Interface import Input_Box, Button, TickBox
from Graphics import Color_Handler, Image_Handler
from Mechanics import Pizza_Options, Url_Getter, Url_Parser, Replacer, Restaurant_Struct, Meal, Check_Price, \
    List_Handler
import re
import time
import threading
import multiprocessing
import urllib
import os

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
        screen.blit(text, (1300, 250))
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
        options.size = int(input_box3.text)
        options.city = input_box1.text
        options.address = input_box2.text
        options.toppings_table = [tick_boxes[x].active for x in range(24)]
        options.only_opened = tick_box25.active
        if options.size_correct() and options.address_correct():
            return True
        else:
            return False

    pizza_options = Pizza_Options.PizzaOptions()

    input_box1 = Input_Box.InputBox(460, 200, 30, 620, 'Krakow', 'String')
    input_box2 = Input_Box.InputBox(460, 250, 30, 620, 'Dobrego Pasterza 48', 'String')
    input_box3 = Input_Box.InputBox(1240, 250, 2, 50, '45', 'Number')
    input_boxes = [input_box1, input_box2, input_box3]

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
    tick_box25 = TickBox.TickBox(1320, 750, True)

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
    pizza_toppings = [Pizza_Options.PizzaOptions.toppings[x] for x in range(len(pizza_options.toppings_table)) if
                      pizza_options.toppings_table[x]]
    pizza_size = pizza_options.size

    list_object = List_Handler.List_Handler()

    loading_pictures = [Image_Handler.get_image('loading_' + str(num)) for num in range(12)]

    def get_data(list_obj):
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

        pizzerias = []

        parsed_main_url = Url_Parser.Url_Parser(main_url)

        pizzerias_metadata = re.findall(
            r'<div class="restaurant grid"(.*?)</div>\\n\\t\\t</div>\\n\\t</div>\\n\\t</div>\\n\\n',
            str(parsed_main_url))
        selected = 0
        pizzerias_found = len(pizzerias_metadata)
        for metadata in pizzerias_metadata:
            chosen = Replacer.Uni_Replacer(re.search(r'<div class="open">(.*?)</div>', metadata).group(1))
            if pizza_options.only_opened and chosen != '':
                continue
            else:
                name = Replacer.Uni_Replacer(re.search(r'<a class="restaurantname(.*?)/a>', metadata).group(1))
                products = Replacer.Uni_Replacer(
                    re.search(r'<div class="kitchens">\\n\\t\\t\\t<span>(.*?)</span>', metadata).group(1))
                if 'izz' in name or 'izz' in products:
                    link = 'http://www.pyszne.pl' + Replacer.Uni_Replacer(re.search(r'href="(.*?)"', name).group(1))
                    min_order = Replacer.Uni_Replacer(
                        re.search(r'<div class="min-order">(.*?)</div>', metadata).group(1))
                    delivery = Replacer.Uni_Replacer(
                        re.search(r'<div class="open">(.*?)<div class="min-order', metadata).group(1))
                    delivery = Replacer.Uni_Replacer(re.search(r'<div class="delivery">(.*?)</div>', delivery).group(1))
                    name = Replacer.Uni_Replacer(re.search(r'itemprop="name">(.*?)<', name).group(1))[18:-12]
                    id = Replacer.Uni_Replacer(re.search(r'id="irestaurant(.*?)"', metadata).group(1))
                    pizzerias.append(Restaurant_Struct.RestaurantStruct(name, link, min_order, delivery, id))

        # BY THIS POINT WE HAVE THE LIST OF PIZZERIAS WE WANT TO CHECK

        for i in range(len(pizzerias)):
            parsed_url = Url_Parser.Url_Parser(pizzerias[i].link)
            pizzerias[i].parsed_url = str(parsed_url)
            categories = re.search(r'<ul class="menu-category-list">(.*?)</ul>', str(parsed_url)).group(1)
            categories = re.findall(r'<a href="#(.*?)"', categories)

            temp = []
            for category in categories:
                if 'izz' in category:
                    temp.append(category)
            if len(temp) > 0:
                pizzerias[i].categories = temp

        # BY NOW WE GOT PIZZERIAS CATEGORIES

        # GETTING LOGO URL
        for pizzeria in pizzerias:
            pizzeria.image_link = 'http://' + re.search(r'<div class="restaurant-logo">\\n {2}<img src="//(.*?) alt', str(pizzeria.parsed_url)).group(1)[:-1]

        temp = []
        for pizzeria in pizzerias:
            if pizzeria.categories:
                temp.append(pizzeria)
        pizzerias = temp

        # BY NOW PIZZERIAS WITH NO CORRESPONDING CATEGORIES ARE REMOVED

        for i in range(len(pizzerias)):
            sections = ''
            for j in range(len(pizzerias[i].categories)):
                meals_metadata = re.search(
                    r'anchor-id="' + re.escape(pizzerias[i].categories[j]) + r'(.*?)<div class="menu-meals-group"',
                    pizzerias[i].parsed_url)
                if meals_metadata:
                    meals_metadata = meals_metadata.group(1)
                    sections = sections + meals_metadata
            pizzerias[i].section = sections

        # BY NOW SECTIONS ARE ESTABLISHED

        temp = []
        for pizzeria in pizzerias:
            if pizzeria.section:
                temp.append(pizzeria)
        pizzerias = temp

        # BY NOW EMPTY SECTIONS ARE ELIMINATED

        for pizzeria in pizzerias:
            pizzeria.meals_raw = re.findall(
                r'<div class="meal" id="(.*?)</button>\\n\\t\\t\\t {4}</div>',
                pizzeria.section)

        # RAW MEALS DATA EXTRACTED

        for pizzeria in pizzerias:

            for raw_meal in pizzeria.meals_raw:

                id = re.search(r'(.*?)" itemscope itemtype="', raw_meal)
                if id:
                    id = Replacer.Uni_Replacer(id.group(1))

                name = re.search(r'<span class="meal-name" itemprop="name">\\n {8}(.*?) {6}</span>', raw_meal)
                if name:
                    name = Replacer.Uni_Replacer(name.group(1))

                toppings = re.search(
                    r'<div class="meal-description-additional-info" itemprop="description">(.*?)</div>',
                    raw_meal)
                if toppings:
                    toppings = Replacer.Uni_Replacer(toppings.group(1))

                sizes = re.search(r'<div class="meal-description-choose-from">(.*?)</div>', raw_meal)
                if sizes:
                    sizes = Replacer.Uni_Replacer(sizes.group(1))
                    sizes = re.findall('\d+', sizes)
                    sizes = [int(x) for x in sizes]

                # COMPARISON WITH USER INPUT SIZE AND TOPPINGS

                Toppings_flag = True

                for topping in pizza_toppings:
                    if toppings:
                        if topping not in toppings:
                            Toppings_flag = False

                if sizes:
                    Size_flags = [True for _ in range(len(sizes))]

                if sizes:
                    for x in range(len(sizes)):
                        if pizza_size != sizes[x]:
                            Size_flags[x] = False

                if sizes:
                    Size_flag = any(Size_flags)

                if sizes:
                    if Size_flag and Toppings_flag:
                        pizzeria.meals.append(Meal.Meal(name, toppings, pizza_size, id,
                                                        Restaurant_Struct.RestaurantInfo(pizzeria.name, pizzeria.link,
                                                                                         pizzeria.min_order,
                                                                                         pizzeria.delivery,
                                                                                         pizzeria.id,
                                                                                         pizzeria.image_link)))

        # BY THIS POINT ALL FITTING MEALS ARE FOUND

        for pizzeria in pizzerias:
            temp = []
            for meal in pizzeria.meals:
                if meal.name and meal.toppings and meal.size and meal.id:
                    temp.append(meal)
            pizzeria.meals = temp

        temp = []
        for pizzeria in pizzerias:
            if len(pizzeria.meals) > 0:
                temp.append(pizzeria)
        pizzerias = temp

        # BY THIS POINT ALL USELESS DATA IS FILTERED OUT

        # CHECKING THE PRICES

        cpus = multiprocessing.cpu_count() - 2

        if cpus == 0:
            for pizzeria in pizzerias:
                for meal in pizzeria.meals:
                    price_raw = Check_Price.Check_Price(pizzeria.link, meal.id, pizzeria.id, pizza_options.city,
                                                        pizza_options.address)
                    price_raw = price_raw.replace(',', '.')
                    numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', price_raw)]
                    prices = []
                    sizes = []
                    for i in range(0, len(numbers), 2):
                        sizes.append(numbers[i])
                        prices.append(numbers[i + 1])
                    for i in range(len(sizes)):
                        if pizza_size == sizes[i]:
                            final_price_pos = i
                    if len(prices) > 0:
                        meal.price = prices[final_price_pos]
        else:
            def look_for_price(meal, city, address):
                price_raw = Check_Price.Check_Price(meal.pizzeria_info.link, meal.id, meal.pizzeria_info.id, city,
                                                    address)
                price_raw = price_raw.replace(',', '.')
                numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', price_raw)]
                prices = []
                sizes = []
                for i in range(0, len(numbers), 2):
                    sizes.append(numbers[i])
                    prices.append(numbers[i + 1])
                for i in range(len(sizes)):
                    if pizza_size == sizes[i]:
                        final_price_pos = i
                if len(prices) > 0:
                    meal.price = prices[final_price_pos]

            threaded_meals = []
            for pizzeria in pizzerias:
                for meal in pizzeria.meals:
                    threaded_meals.append(meal)

            threaded_meals = [threaded_meals[i:i + cpus] for i in range(0, len(threaded_meals), cpus)]

            for x in range(len(threaded_meals)):
                thread_jobs = []
                for y in range(len(threaded_meals[x])):
                    thread_jobs.append(
                        threading.Thread(target=look_for_price, args=(threaded_meals[x][y], pizza_options.city,
                                                                      pizza_options.address)))
                for thread in thread_jobs:
                    thread.start()

                while True:
                    if not any([thread.is_alive() for thread in thread_jobs]):
                        break

        # SORTING BY PRICE

        sorted_list = []

        for pizzeria in pizzerias:
            for meal in pizzeria.meals:
                if meal.price is not None:
                    sorted_list.append(meal)

        sorted_list.sort(key=lambda x: x.price)
        if len(sorted_list) > 0:
            list_obj.list = sorted_list
            print("Searching Completed")
        else:
            list_obj.list = 'Empty'
            print("Empty")

        # BY THIS POINT, DATA IS READY TO SHOW :)

    # MAIN BODY

    thread1 = threading.Thread(target=get_data, args=(list_object,))
    thread1.start()
    loading_counter = 2
    loading_num = 0

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)

        # UPDATE STUFF

        # SHOW STUFF

        if thread1.is_alive():
            #  Animation here
            screen.blit(background_image, (0, 0))
            text = pygame.font.Font(font, 50).render("Searching for the cheapest pizza...", True,
                                                     Color_Handler.Color('BLACK'))
            screen.blit(text, (75, 300))
            text = pygame.font.Font(font, 30).render("(This might take a while)", True,
                                                     Color_Handler.Color('BLACK'))
            screen.blit(text, (510, 370))

            screen.blit(loading_pictures[loading_num], (700, 500))
            loading_counter -= 1
            if loading_counter == 0:
                loading_counter = 2
                loading_num += 1
                if loading_num == 12:
                    loading_num = 0

        else:
            if list_object.list == 'Empty':
                if no_pizzas_found():
                    return True, 'Menu'
            else:
                if show_results(list_object.list):
                    return True, 'Menu'

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def no_pizzas_found():

    button1 = Button.Button(500, 820, 400, 58, 'Try Again', 50, Button.Button.button_func_ret_Again())
    button2 = Button.Button(940, 820, 165, 58, 'Exit', 50, Button.Button.button_func_ret_Exit())
    buttons = [button1, button2]

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            for button in buttons:

                ret_val = button.handle_event(event)

                if ret_val == Button.ButtonFunctions.EXIT:
                    pygame.quit()
                    quit()

                elif ret_val == Button.ButtonFunctions.AGAIN:
                    return True

        # UPDATE STUFF

        for button in buttons:
            button.update()

        # SHOW STUFF

        screen.blit(background_image, (0, 0))

        text = pygame.font.Font(font, 50).render("No pizzas found :(", True,
                                                 Color_Handler.Color('BLACK'))
        screen.blit(text, (450, 400))

        for button in buttons:
            button.show(screen)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def show_results(pizzas_sorted):

    meal_to_show = 0

    button1 = Button.Button(500, 520, 170, 108, '', 20, Button.Button.button_func_ret_Left(), (Image_Handler.get_image('left_arrow_black'), Image_Handler.get_image('left_arrow_white')))
    button2 = Button.Button(800, 520, 170, 108, '', 20, Button.Button.button_func_ret_Right(), (Image_Handler.get_image('right_arrow_black'), Image_Handler.get_image('right_arrow_white')))
    button3 = Button.Button(420, 820, 490, 58, 'Check Again', 50, Button.Button.button_func_ret_Again())
    button4 = Button.Button(960, 820, 165, 58, 'Exit', 50, Button.Button.button_func_ret_Exit())
    buttons = [button1, button2, button3, button4]

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            for button in buttons:
                ret_val = button.handle_event(event)

                if ret_val == Button.ButtonFunctions.EXIT:
                    pygame.quit()
                    quit()

                elif ret_val == Button.ButtonFunctions.AGAIN:
                    return True

                elif ret_val == Button.ButtonFunctions.LEFT:
                    if meal_to_show != 0:
                        meal_to_show -= 1

                        with open('Graphics/Images/current_restaurant.png', 'wb') as f:
                            req = urllib.request.Request(
                                pizzas_sorted[meal_to_show].pizzeria_info.image_link,
                                headers={'User-Agent': 'Mozilla/5.0'})
                            img = urllib.request.urlopen(req).read()
                            f.write(img)

                elif ret_val == Button.ButtonFunctions.RIGHT:
                    if meal_to_show < len(pizzas_sorted) - 1:
                        meal_to_show += 1

                        with open('Graphics/Images/current_restaurant.png', 'wb') as f:
                            req = urllib.request.Request(
                                pizzas_sorted[meal_to_show].pizzeria_info.image_link,
                                headers={'User-Agent': 'Mozilla/5.0'})
                            img = urllib.request.urlopen(req).read()
                            f.write(img)

        # UPDATE STUFF

        for button in buttons:
            button.update()

        # SHOW STUFF

        screen.blit(background_image, (0, 0))

        # PIZZERIA NAME
        text = pygame.font.Font(font, 30).render(Replacer.Pl_Replacer(pizzas_sorted[meal_to_show].pizzeria_info.name), True,
                                                 Color_Handler.Color('BLACK'))
        text_width = text.get_width()
        screen.blit(text, ((1600 - text_width)/2, 50))

        # PIZZERIA LOGO
        screen.blit(Image_Handler.get_image('current_restaurant'), (567, 100))

        # PIZZA NAME
        text = pygame.font.Font(font, 30).render(Replacer.Pl_Replacer(pizzas_sorted[meal_to_show].name), True,
                                                 Color_Handler.Color('BLACK'))
        text_width = text.get_width()
        screen.blit(text, ((1600 - text_width) / 2, 500))

        for button in buttons:
            button.show(screen)

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
            main_end, wtd = program_main(pizza_options)
            if main_end:
                if wtd == 'Menu':
                    menu = True
                    main = False
                    end = False
                else:
                    menu = False
                    main = False
                    end = True
        elif end:
            end_end = program_end()
            if end_end:
                pass
