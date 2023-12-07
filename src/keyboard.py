from src.item import Item


class MixinChange:
    """
    Класс-миксин по хранению и изменению раскладки клавиатуры
    """
    __en_layer = 'EN'
    __ru_layer = 'RU'

    def __init__(self):
        self.__language = self.__en_layer

    def change_lang(self):
        """
        Меняется раскладка при запуске метода
        """
        if self.__language == self.__en_layer:
            self.__language = self.__ru_layer
        elif self.__language == self.__ru_layer:
            self.__language = self.__en_layer

    @property
    def language(self):
        return self.__language

    @property
    def en_layer(self):
        return self.__en_layer

    @property
    def ru_layer(self):
        return self.__ru_layer


class Keyboard(Item, MixinChange):
    """
    Класс наследуется от 'Item' а также от 'MixinChange', где есть атрибут `language`
    и метод для изменения языка (раскладки клавиатуры)
    """
    pass

