import doctest


class Engine:
    def __init__(self, power_nominal: float, power: float, periodicity: float):
        """
                Создание и подготовка к работе объекта "Двигатель"
                :param power_nominal: Номинальная мощность
                :param power: Текущая мощность
                :param periodicity: Частота
                Примеры:
        >>> engine = Engine(500, 200, 50)  # инициализация экземпляра класса
                """

        if not isinstance(power_nominal, (int, float)):
            raise TypeError("Номинальная мощность должна быть типа int или float")
        if power_nominal <= 0:
            raise ValueError("Номинальная мощность должна быть положительным числом")
        self.power_nominal = power_nominal

        if not isinstance(power, (int, float)):
            raise TypeError("Текущая мощность должна быть типа int или float")
        if power <= 0:
            raise ValueError("Текущая мощность должна быть положительным числом")
        self.power = power

        if not isinstance(periodicity, (int, float)):
            raise TypeError("Частота должна быть int или float")
        if periodicity < 0:
            raise ValueError("Частота не может быть отрицательным числом")
        self.periodicity = periodicity


    def is_on_engine(self) -> bool:
        """
        Функция которая проверяет включён ли двигатель
        :return: Двигатель включен
        Примеры:
        >>> engine = Engine(500, 200, 50)
        >>> engine.is_on_engine()
        """
        ...

    def add_power_to_engine(self, pow: float) -> None:
        """
        Увеличение мощности двигателя.
        :param pow: Повышение мощности
        :raise ValueError: Если итоговая мощность превысит номинальную, то вызываем ошибку
         Примеры:
        >>> engine = Engine(500, 200, 50)
        >>> engine.add_power_to_engine(150)
        """
        if not isinstance(pow, (int, float)):
            raise TypeError("Добавляемая мощность должна быть типа int или float")
        if pow < 0:
            raise ValueError("Добавляемая мощность должна положительным числом")
        ...


class Tree:
    def __init__(self, height: float, age: float):
        """
                Создание и подготовка к работе объекта "Дерево"
                :param height: Высота дерева
                :param age: Возраст дерева
                Примеры:
        >>> tree = Tree(10, 200)  # инициализация экземпляра класса
                """

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int или float")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age


    def add_height_to_tree(self, h: float) -> None:
        """
        Увеличение высоты дерева
        :param h: Увеличение высоты
         Примеры:
        >>> tree = Tree(10,200)
        >>> tree.add_height_to_tree(1)
        """
        if not isinstance(h, (int, float)):
            raise TypeError("Добавляемая высота должна быть типа int или float")
        if h < 0:
            raise ValueError("Добавляемая высота должна быть положительным числом")
        ...

    def height_to_tree(self, time: float) -> None:
        """
        Расчёт высоты дерева через заданный промежуток времени
        :param time: заданный промежуток времени
         Примеры:
        >>> tree = Tree(10,200)
        >>> tree.height_to_tree(5)
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть типа int или float")
        if time < 0:
            raise ValueError("Время должно быть положительным числом")
        ...


class Cupboard:
    def __init__(self, length: float, width: float, height: float, M: float):
        """
                Создание и подготовка к работе объекта "Шкаф"
                :param length: Длина шкафа
                :param width: Ширина шкафа
                :param height: Высота шкафа
                :param M: Масса шкафа
                Примеры:
        >>> cupboard = Cupboard(80, 40, 180, 20)  # инициализация экземпляра класса
                """

        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(M, (int, float)):
            raise TypeError("Масса должна быть типа int или float")
        if M <= 0:
            raise ValueError("Масса должна быть положительным числом")
        self.M = M


    def volume_of_cupboard(self) -> None:
        """
        Вычисление объёма шкафа
        Примеры:
        >>> cupboard = Cupboard(80, 40, 180, 20)
        >>> cupboard.volume_of_cupboard()
        """
        ...

    def massa_of_cupboard(self, m: float) -> None:
        """
        Расчёт массы шкафа при заполении его вещами
        :param m: масса вещей
         Примеры:
        >>> cupboard = Cupboard(80, 40, 180, 20)
        >>> cupboard.massa_of_cupboard(5)
        """
        if not isinstance(m, (int, float)):
            raise TypeError("Масса должна быть типа int или float")
        if m < 0:
            raise ValueError("Масса должна быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации