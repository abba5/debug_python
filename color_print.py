"""

made by love of debugging
created by abbas rangwala ( abba5 )

want to use ?
just use cprint

1) default background and default color
cprint( string / data / object)

2) for change default color
cprint( string / data / object, text_color=color.RED)

3) for change default background
cprint( string / data / object, background_color=color.RED)

4) for change both
cprint( string / data / object, background_color=color.RED, text_color=color.RED)

"""

class color:
    RED = (245, 90, 66)
    ORANGE = (245, 170, 66)
    YELLOW = (245, 252, 71)
    GREEN = (92, 252, 71)
    BLUE = (71, 177, 252)
    PURPLE = (189, 71, 252)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


def text(text, rgb):
    return "\033[38;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m" + str(text) + "\033[0m"


def background(text, rgb):
    return "\033[48;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m" + text + "\033[0m"


def cprint(*data, text_color=color.RED, background_color=color.BLACK):
    for data_arg in data:
        print(background(text(data_arg, text_color), background_color))


def log_cprint(data, text_color=color.RED, background_color=color.BLACK):
    return background(text(data, text_color), background_color)