class ColorRepair:
    VALID_COLOURS = {'Белый': 1, 'Синий': 1, 'Желтый': 1.1, 'Красный': 1, 'Перламутровый': 1.2, 'Серый металлик': 1.3}

    def __init__(self, colour):
        if colour not in self.VALID_COLOURS:
            raise ValueError(f"Недопустимое значение colour: {colour}")
        self.colour = colour

    def get_multiplier(self):
        return self.VALID_COLOURS[self.colour]
