class ColorRepair:
    VALID_COLOURS = {
        'Белый': 1, 'Синий': 1, 'Желтый': 1.1, 'Красный': 1, 'Перламутровый': 1.2,
        'Серый металлик': 1.3, 'Чёрный': 1.15, 'Оранжевый': 1.1
    }

    def __init__(self, colour):
        if colour not in self.VALID_COLOURS:
            raise ValueError(f"Недопустимое значение colour: {colour}")
        self.colour = colour

    @staticmethod
    def get_multiplier(colour):
        return ColorRepair.VALID_COLOURS.get(colour, 1)

    @staticmethod
    def get_available_colours():
        return list(ColorRepair.VALID_COLOURS.keys())

