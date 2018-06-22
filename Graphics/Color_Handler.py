# Function returns requested color


def Color(color_name):
    return {
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0, 0),
        'BLUE': (0, 0, 255),
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'OVER_GREEN': (0, 203, 0),
        'OVER_RED': (203, 0, 0),
        'LIGHT_BLUE_3': (154, 192, 255),
        'DODGER_BLUE_3': (24, 116, 205),
        'GRAY': (128, 128, 128),
        'DARK_GRAY': (26, 26, 26)
    }[color_name]


