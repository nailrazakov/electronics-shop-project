from src.item import Item


class Phone(Item):
    """
    Phone содержит все атрибуты класса Item и дополнительно атрибут,
    содержащий количество поддерживаемых сим-карт
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, data):
        if isinstance(data, int) and data > 0:
            self.__number_of_sim = data
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
