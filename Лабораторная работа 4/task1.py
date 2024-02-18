if __name__ == "__main__":
    class Pen:
        def __init__(self, color: str, ink: int):
            """
            :param color: Цвет ручки
            :param ink: Оставшиеся чернила (в процентах)

            :raise TypeError: Количество оставшихся чернил в процентах должно быть типа int
            :raise ValueError: Количество оставшихся чернил в процентах должно быть от 0 до 100
            """

            self.color = color

            if not isinstance(ink, int):
                raise TypeError("Количество оставшихся чернил в процентах должно быть типа int")
            if ink < 0 or ink > 100:
                raise ValueError("Количество оставшихся чернил в процентах должно быть от 0 до 100")

            self.ink = ink

        def __repr__(self):
            return f"{self.__class__.__name__}(color={self.color!r}, ink={self.ink!r})"

        def __str__(self):
            return f"Ручка цвета {self.color}. Оставшиеся чернила {self.ink}%"

        def write(self, used_ink: int) -> None:
            """
            Функция, которая позволяет писать ручкой
            :param used_ink: Использованные на написание чернила

            :raise TypeError: Количество использованных чернил в процентах должно быть типа int
            :raise ValueError: Количество использованных чернил в процентах должно быть
            меньше количества оставшихся чернил и больше 0
            """

            if not isinstance(used_ink, int):
                raise TypeError("Количество использованных чернил в процентах должно быть типа int")

            if used_ink > self.ink or used_ink < 0:
                raise ValueError("Количество использованных чернил в процентах должно быть "
                                 "меньше количества оставшихся чернил и больше 0")

            self.ink -= used_ink

        def change_ink(self, new_color: str, new_ink: int) -> None:
            """
            Функция, которя позволяет поменять стержень ручки

            :param new_color: Новый цвет чернил
            :param new_ink: Новое количество чернил

            :raise TypeError: Новое количество чернил в процентах должно быть типа int
            :raise ValueError: Новое количество чернил в процентах должно быть от 0 до 100
            """

            if not isinstance(new_ink, int):
                raise TypeError("Новое количество чернил в процентах должно быть типа int")

            if new_ink < 0 or new_ink > 100:
                raise ValueError("Новое количество чернил в процентах должно быть от 0 до 100")

            self.ink = new_ink
            self.color = new_color


    class AutomaticPen(Pen):
        def __init__(self, color: str, ink: int, if_pinned: bool = False):
            """
            :param color: Цвет ручки
            :param ink: Оставшиеся чернила (в процентах)
            :param if_pinned: Вытащен ли стержень
            """
            super().__init__(color=color, ink=ink)
            self.if_pinned = if_pinned

        def __repr__(self):
            return f"{self.__class__.__name__}(color={self.color!r}, ink={self.ink!r}, if_pressed={self.if_pinned!r})"

        def write(self, used_ink: int) -> None:
            """
            Функция, которая позволяет писать ручкой

            Перезагружаем метод, потому что автоматической ручкой можно писать,
            только если стержень вытащен

            :param used_ink: Использованные на написание чернила

            :raise ValueError: Атрибут if_pinned должен быть значения True (стержень должен быть вытащен)
            :raise TypeError: Количество использованных чернил в процентах должно быть типа int
            :raise ValueError: Количество использованных чернил в процентах должно быть
            меньше количества оставшихся чернил и больше 0
            """

            if not self.if_pinned:
                raise ValueError("Атрибут if_pinned должен быть значения True (стержень должен быть вытащен)")

            if not isinstance(used_ink, int):
                raise TypeError("Количество использованных чернил в процентах должно быть типа int")

            if used_ink > self.ink or used_ink < 0:
                raise ValueError("Количество использованных чернил в процентах должно быть "
                                 "меньше количества оставшихся чернил и больше 0")

            self.ink -= used_ink

    pass
