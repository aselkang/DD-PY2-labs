import doctest

class Rectangle:
    def __init__(self, side1: float, side2: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param side1: сторона прямоугльника
        :param side2: другая сторона прямоугольника

        Примеры:
        >>> rectangle = Rectangle(6, 4)  # инициализация экземпляра класса
        """

        if not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)):
            raise TypeError("Сторона прямоугольника должна быть типа int или float")
        if side1 <= 0 or side2 <= 0:
            raise ValueError("Сторона прямоугольника должна быть положительным числом")

        self.side1 = side1
        self.side2 = side2

    def is_square(self) -> bool:
        """
        Функция, которая проверяет является ли прямоугольник квадратом

        :return: Является ли прямоугольник квадратом

        Примеры:
        >>> rectangle = Rectangle(21.5, 21.5)
        >>> rectangle.is_square()
        True
        """

        if self.side1 == self.side2:
            return True
        else:
            return False

    def length(self) -> float:
        """
        Функция, которая определяет большую сторону прямоугольника - его длину

        :return: Длина прямоугольника
        >>> rectangle = Rectangle(2, 4)
        >>> rectangle.length()
        4
        """

        return max(self.side1, self.side2)

class Time:
    def __init__(self, hours: int, minutes: int):
        """
        Создание и подготовка к работе объекта "Время" в 24-часовом формате

        :param hours: Часы
        :param minutes: Минуты

        Примеры:
        >>> time = Time(1, 26)  # инициализация экземпляра класса
        """

        if not isinstance(hours, int) or not isinstance(minutes, int):
            raise TypeError("Количество часов и минут должно быть типа int")
        if hours > 23 or hours < 0:
            raise ValueError("Количество часов должно быть неотрицательноым числом меньше 24")
        if minutes > 59 or minutes < 0:
            raise ValueError("Количество минут должно быть неотрицательным числом меньше 60")

        self.hours = hours
        self.minutes = minutes

    def time_of_day(self) -> str:
        """
        Функция, которая определяет время суток: утро, день, вечер или ночь

        :return: Время суток

        Примеры:
        >>> time = Time(15, 23)
        >>> time.time_of_day()
        """
        ...

    def add(self, hours: int, minutes: int) -> None:
        """
        Прибавление прошедших часов и минут к исходному времени

        :param hours: Количество прибавляемых часов
        :param minutes: Количество прибавляемых минут

        :raise TypeError: Количество прибавлемых часов и минут должно быть типа int
        :raise ValueError: Количество прибавлемых часов должно быть неотрицательным

        Примеры:
        >>> time = Time(12, 58)
        >>> time.add(25, 10)
        """
        ...

class Film:
    def __init__(self, name: str, is_watched: bool, rating: int = None):
        """
        Создание и подготовка к работе объекта "Фильм"

        :param name: Название фильма
        :param is_watched: Отмечен ли фильм пользователем как просмотренный
        :param rating: Оценка пользователя

        Примеры:
        >>> film = Film('Saltburn', True, 8) # инициализация экземпляра класса
        """

        if rating is not None:
            if not isinstance(rating, int):
                raise TypeError("Оценка должна быть типа int")
            if rating < 1 or rating > 10:
                raise ValueError("Оценка должна быть в пределах от 1 до 10")
            if is_watched == False:
                raise ValueError("Если есть оценка, то фильм должен быть отмечен как просмотренный")

        self.name = name
        self.is_watched = is_watched
        self.rating = rating

    def rate(self, rating: int) -> None:
        """
        Функция, которая позволяет оценить фильм
        :param rating: Оценка, которую пользователь хочет поставить

        :raise ValueError: Оценка должна быть в пределах от 1 до 10

        Примеры:
        >>> film = Film('Mean Girls', False)
        >>> film.rate(10)
        """

        if rating < 0 or rating > 10:
            raise ValueError("Оценка должна быть в пределах от 1 до 10")
        self.rating = rating
        self.is_watched = True

    def delete_rating(self) -> None:
        """
        Удаление оценки

        Примеры:
        >>> film = Film('Melancholia', True, 10)
        >>> film.delete_rating()
        """

        self.rating = None

if __name__ == "__main__":
    doctest.testmod()