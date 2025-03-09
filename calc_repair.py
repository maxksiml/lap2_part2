from detail_repair import DetailRepair
from color_repair import ColorRepair

class CalcRepair:
    BASIC_COST = 12000

    def __init__(self, detail, colour):
        self.detail = DetailRepair(detail)
        self.colour = ColorRepair(colour)

    def calc_cost(self):
        return round(self.BASIC_COST * DetailRepair.get_multiplier(self.detail.detail) * self.colour.get_multiplier())

# Пример использования
calc = CalcRepair('Крыша', 'Желтый')
print(calc.calc_cost())
