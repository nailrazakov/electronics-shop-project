import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # при инициализации добавляет экземпляр класса в список all
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        """
        Магический метод сложения с проверкой условий, что слагаемые именно класса Item
        """
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Возможно сложить только с экземплярами `Phone` или `Item` классов")

    @property
    # геттер для name
    def name(self):
        return self.__name

    @name.setter
    # сеттер для name с проверкой, что длина наименования товара не больше 10 символов
    def name(self, data):
        if len(data) < 10:
            self.__name = data
        else:
            self.__name = data[:10]
            print('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls, file):
        Item.all.clear()
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла items.csv"""
        with open(file, 'r') as csvfile:
            items = list(csv.DictReader(csvfile))
            for item in items:
                Item(item['name'], float(item['price']), int(item['quantity']))

    @staticmethod
    def string_to_number(number):
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
