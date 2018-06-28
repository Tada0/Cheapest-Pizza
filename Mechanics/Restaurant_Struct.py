class RestaurantStruct:
    def __init__(self, name, link, min_order, delivery, id):
        self.name = name
        self.link = link
        self.image_link = None
        self.min_order = min_order
        self.delivery = delivery
        self.id = id
        self.categories = None
        self.sizes = None
        self.parsed_url = None
        self.section = None
        self.meals_raw = None
        self.meals = []


class RestaurantInfo:
    def __init__(self, name, link, min_order, delivery, id, image_link):
        self.name = name
        self.link = link
        self.min_order = min_order
        self.delivery = delivery
        self.id = id
        self.image_link = image_link
