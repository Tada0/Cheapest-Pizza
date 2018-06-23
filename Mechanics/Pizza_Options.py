class PizzaOptions:

    toppings = {
        0: 'anchois',
        1: 'karczoch',
        2: 'rukol',
        3: 'bocz',
        4: 'papryk',
        5: 'camembert',
        6: 'kapar',
        7: 'kurczak',
        8: 'kukurydz',
        9: 'fet',
        10: 'czosn',
        11: 'szynk',
        12: 'zioł',
        13: 'jalapeno',
        14: 'mozzarell',
        15: 'oliwk',
        16: 'cebul',
        17: 'ananas',
        18: 'pieczark',
        19: 'salami',
        20: 'kiełbas',
        21: 'owoce morza',
        22: 'pomidor',
        23: 'tuńczyk',
    }

    def __init__(self):
        self.city = None
        self.address = None
        self.size = None
        self.toppings_table = [False for _ in range(24)]
        self.only_opened = False

    def size_correct(self):
        if self.size > 10:
            return True

    def address_correct(self):
        if len(self.city) > 3 and len(self.address) > 3:
            return True
