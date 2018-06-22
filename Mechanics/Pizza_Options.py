class PizzaOptions:
    def __init__(self):
        self.size_min = None
        self.size_max = None
        self.cheese = True
        self.sauce = True
        self.mushroom = False
        self.ham = False

    def size_chosen(self):
        if self.size_min and self.size_max is not None:
            return True
