from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, c):
        pass

    @abstractmethod
    def __rmul__(self, c):
        pass


class Color(ComputerColor):
    end = '\033[0'
    start = '\033[1;38;2'
    mod = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{self.start};{self.red};{self.green};{self.blue}{self.mod}●{self.end}{self.mod}'

    def __eq__(self, other):
        return (
            self.red == other.red
            and self.green == other.green
            and self.blue == other.blue
            )

    def __add__(self, other):
        new_red = self.red + other.red
        new_green = self.green + other.green
        new_blue = self.blue + other.blue
        return Color(new_red, new_green, new_blue)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __rmul__(self, c):
        cl = -256*(1-c)
        F = 259*(cl + 255) / 255 / (259 - cl)
        new_red = round(F*(self.red - 128) + 128)
        new_green = round(F*(self.green - 128) + 128)
        new_blue = round(F*(self.blue - 128) + 128)
        return Color(new_red, new_green, new_blue)

    def __mul__(self, c):
        cl = -256*(1-c)
        F = 259*(cl + 255) / 255 / (259 - cl)
        new_red = round(F*(self.red - 128) + 128)
        new_green = round(F*(self.green - 128) + 128)
        new_blue = round(F*(self.blue - 128) + 128)
        return Color(new_red, new_green, new_blue)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))
if __name__ == "__main__":
    red = Color(255, 0, 0)
    print_a(red)
