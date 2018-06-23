class PizzaOptions:

    toppings = {
        0: 'anchois',
        1: 'karczochy',
        2: 'rukola',
        3: 'boczek',
        4: 'papryka',
        5: 'camembert',
        6: 'kapary',
        7: 'kurczak',
        8: 'kukurydza',
        9: 'feta',
        10: 'czosnek',
        11: 'szynka',
        12: 'zioła',
        13: 'jalapeno',
        14: 'mozzarella',
        15: 'oliwki',
        16: 'cebula',
        17: 'ananas',
        18: 'pieczarki',
        19: 'salami',
        20: 'kiełbasa',
        21: 'owoce morza',
        22: 'pomidor',
        23: 'tuńczyk',
    }

    def __init__(self):
        self.city = None
        self.address = None
        self.size_min = None
        self.size_max = None
        self.toppings_table = [False for _ in range(24)]
        self.only_opened = False

    def size_correct(self):
        if self.size_min and self.size_max is not None and self.size_max > self.size_min:
            return True

    def address_correct(self):
        if len(self.city) > 3 and len(self.address) > 3:
            return True
