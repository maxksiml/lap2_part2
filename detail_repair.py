class DetailRepair:
    VALID_DETAILS = {'Капот': 1, 'Передняя дверь': 1.2, 'Задняя дверь': 1.1, 'Передний бампер': 1, 'Задний бампер': 1, 'Крыша': 1.1}

    def __init__(self, detail):
        if detail not in self.VALID_DETAILS:
            raise ValueError(f"Недопустимое значение detail: {detail}")
        self.detail = detail

    def get_multiplier(self):
        return self.VALID_DETAILS[self.detail]
