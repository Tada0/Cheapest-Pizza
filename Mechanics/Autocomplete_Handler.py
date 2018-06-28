import pickle


class AutoCompleter:
    def __init__(self):
        self.city = ''
        self.address = ''
        self.size = ''
        self.ingredients = [False for _ in range(24)]

    def insert(self, city, address, size, ingredients):
        self.city = city
        self.address = address
        self.size = size
        self.ingredients = ingredients

    def save(self):
        global pickle_out

        file_name = 'ud.acf'

        try:
            pickle_out = open(file_name, "wb")
            pickle.dump(self, pickle_out)
        except IOError as e:
            print(e)
        finally:
            pickle_out.close()

    @staticmethod
    def load():
        global pickle_in
        global object_from_pickle

        try:
            pickle_in = open('ud.acf', "rb")
            object_from_pickle = pickle.load(pickle_in)
        except Exception as e:
            return AutoCompleter()
        finally:
            pickle_in.close()

        if object_from_pickle is not None:
            return object_from_pickle