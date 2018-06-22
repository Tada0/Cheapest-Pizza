class PizzaOptions:
    def __init__(self):
        self.city = None
        self.address = None
        self.size_min = None
        self.size_max = None
        self.anchois = False
        self.artichokes = False
        self.arugula = False
        self.bacon = False
        self.bell_pepper = False
        self.camembert = False
        self.capers = False
        self.chicken = False
        self.corn = False
        self.feta = False
        self.garlic = False
        self.ham = False
        self.herbs = False
        self.jalapeno = False
        self.mozzarella = False
        self.olives = False
        self.onion = False
        self.pineapple = False
        self.portobello = False
        self.salami = False
        self.sausage = False
        self.seafood = False
        self.tomato = False
        self.tuna = False
        self.only_opened = False

    def size_correct(self):
        if self.size_min and self.size_max is not None and self.size_max > self.size_min:
            return True

    def address_correct(self):
        if len(self.city) > 3 and len(self.address) > 3:
            return True
