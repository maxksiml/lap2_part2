class DetailRepair:
    VALID_DETAILS = {
        'Капот': 1, 'Передняя дверь': 1.2, 'Задняя дверь': 1.1, 'Передний бампер': 1,
        'Задний бампер': 1, 'Крыша': 1.1, 'Крыло': 1.15, 'Порог': 1.05
    }

    def __init__(self, detail):
        if detail not in self.VALID_DETAILS:
            raise ValueError(f"Недопустимое значение detail: {detail}")
        self.detail = detail

    @staticmethod
    def get_multiplier(detail):
        return DetailRepair.VALID_DETAILS.get(detail, 1)

    @staticmethod
    def get_available_details():
        return list(DetailRepair.VALID_DETAILS.keys())

