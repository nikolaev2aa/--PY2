class Reactor:
    def __init__(self, name: str, power: int, coolant: str):
        """
        Создание объекта класса реактор
        :param name: название реактора
        :param power: электрическая мощность (в МВт)
        :param coolant: теплоноситель

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        """
        self._name = name
        self._power = power
        self._coolant = coolant
        self._fuel = None  # тип топлива, по умолчанию отсутствует
        self._fuelassembly = None  # тип тепловыделяющей сборки, по умолчанию отсутствует

    @property
    def name(self):
        """
        Атрибут только для чтения (read-only)
        :return: возвращает название реактора
        """
        return self._name

    @property
    def power(self):
        """
        Атрибут только для чтения (read-only)
        :return: возвращает мощность реактора
        """
        return self._power

    @property
    def coolant(self):
        """
        Атрибут только для чтения (read-only)
        :return: возвращает тип теплоносителя
        """
        return self._coolant

    def add_fuelassembly(self, tvs: str):
        """
        Метод, позволяющий добавить тип тепловыделяющей сборки (ТВС)
        :param tvs: тип ТВС
        :return:

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuelassembly("ТВС-2006")
        """
        self._tvs = tvs

    def write_fuelassembly(self):
        """
        Метод, позволяющий вернуть ранее оставленный тип ТВС
        :return: Возвращает тип ТВС

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuelassembly("ТВС-2006")
        >>> test_reactor.write_fuelassembly()
        'ТВС-2006'
        """
        return self._tvs

    def add_fuel(self, typefuel: str):
        """
        Метод, позволяющий добавить тип топлива
        :param typefuel: тип топлива
        :return:

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuel("МОХ-топливо")
        """
        self._fuel = typefuel

    def write_fuel(self):
        """
        Метод, позволяющий вернуть ранее оставленный тип топлива
        :return: Возвращает тип топлива

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuel("МОХ-топливо")
        >>> test_reactor.write_fuel()
        'МОХ-топливо'
        """
        return self._fuel

    def __str__(self):
        """
        Магический метод __str__
        :return: Возвращает название, мощность реактора, тип теплоносителя

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")
        >>> print (test_reactor)
        Реактор: РБМК. Мощность: 1000 МВт. Теплоноситель: вода
        """
        return f"Реактор: {self.name}. Мощность: {self.power} МВт. Теплоноситель: {self.coolant}"

    def __repr__(self):
        """
        Магический метод __repr__
        :return: Возвращает название, мощность реактора, тип теплоносителя
        """
        return f"{self.__class__.__name__}(name={self.name!r}, power={self.power!r}, coolant={self.coolant!r})"

    def energy(self, power: int, time: int):
        """
        Метод вычисляющий энерговыработку за время time
        :param power: мощность в МВт
        :param time: время в часах
        :return: Возвращает энерговыработку за время time (в МВт*час)
        """
        ...
        return ...

class PWR(Reactor):
    def __init__(self, name: str, power: int, coolant: str, moderator: str):
        """
        Создание дочернего класса PWR
        :param name: название реактора
        :param power: электрическая мощность
        :param coolant: теплоноситель
        :param moderator: замедлитель

        Примеры:
        >>> test_reactor = PWR("ВВЭР", 1000, "вода", "вода")  # Инициализация объекта класса
        """

        super().__init__(name, power, coolant)  # вызывает метод родительского класса
        if isinstance(moderator, str):  # Проверка на корректность входных данных
            self.moderator = moderator  # расширение метода
        else:
            raise AttributeError(f'Некорректно указан замедлитель:{moderator!r}')

    def __str__(self):
        """
        Перегрузка магического метода __str__
        :return: Возвращает название, мощность реактора, тип теплоносителя, замедлителя

        Примеры:
        >>> test_reactor = Reactor("ВВЭР", 1000, "вода", "вода")
        >>> print (test_reactor)
        Реактор: ВВЭР. Мощность: 1000 МВт. Теплоноситель: вода. Замедлитель: вода
        """
        return f"Реактор: {self.name}. Мощность: {self.power} МВт. Теплоноситель: {self.coolant}. " \
               f"Замедлитель: {self.moderator}"

    def __repr__(self):
        """
        Перегрузка магического метода __repr__
        :return: Возвращает название, мощность реактора, тип теплоносителя, замедлителя
        """
        return f"{self.__class__.__name__}(name={self.name!r}, power={self.power!r}, coolant={self.coolant!r}, " \
               f"moderator={self.moderator!r})"

    def add_fuel(self, typefuel: str):
        """
        Наследование метода add_fuel, позволяющего добавить тип топлива
        :param typefuel: тип топлива
        :return:

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuel("МОХ-топливо")
        """
        self._fuel = typefuel

    def write_fuel(self):
        """
        Наследование метода, позволяющего вернуть ранее оставленный тип топлива
        :return: Возвращает тип топлива

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuel("МОХ-топливо")
        >>> test_reactor.write_fuel()
        'МОХ-топливо'
        """
        return self._fuel


class SFR(Reactor):
    def __init__(self, name: str, power: int, coolant: str, circuit: int):
        """
         Создание дочернего класса SFR
         :param name: название реактора
         :param power: электрическая мощность
         :param coolant: теплоноситель
         :param circuit: число контуров циркуляции

         Примеры:
         >>> test_reactor = PWR("БН", 1200, "вода", 3)  # Инициализация объекта класса
         """

        super().__init__(name, power, coolant)  # вызывает метод родительского класса
        if isinstance(circuit, int) and circuit > 0:  # Проверка на корректность входных данных
            self.circuit = circuit  # расширение метода
        else:
            raise AttributeError(f'Некорректно указано количество контуров:{circuit!r}')

    def __str__(self):
        """
        Перегрузка магического метода __str__
        :return: Возвращает название, мощность реактора, тип теплоносителя, число контуров циркуляции

        Примеры:
        >>> test_reactor = Reactor("БН", 1200, "вода", 3)
        >>> print (test_reactor)
        Реактор: БН. Мощность: 1200 МВт. Теплоноситель: вода. Количество контуров: 3
        """
        return f"Реактор: {self.name}. Мощность: {self.power} МВт. Теплоноситель: {self.coolant}. " \
               f"Количество контуров: {self.circuit}"

    def __repr__(self):
        """
        Перегрузка магического метода __repr__
        :return: Возвращает название, мощность реактора, тип теплоносителя, число контуров циркуляции
        """
        return f"{self.__class__.__name__}(name={self.name!r}, power={self.power!r}, coolant={self.coolant!r}, " \
               f"circuit={self.circuit!r})"

    def add_fuelassembly(self, tvs: str):
        """
        Наследование метода add_fuelassembly
        Метод, позволяющий добавить тип тепловыделяющей сборки (ТВС)
        :param tvs: тип ТВС
        :return:

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuelassembly("ТВС-2006")
        """
        self._fuelassembly = tvs

    def write_fuelassembly(self):
        """
        Метод, позволяющий вернуть ранее оставленный тип ТВС
        :return: Возвращает тип ТВС

        Примеры:
        >>> test_reactor = Reactor("РБМК", 1000, "вода")  # Инициализация объекта класса
        >>> test_reactor.add_fuelassembly("ТВС-2006")
        >>> test_reactor.write_fuelassembly()
        'ТВС-2006'
        """
        return self._tvs

    def energy(self, power: int, time: int):
        """
        Перегрузка метода, вычисляющего энерговыработку за время time, чтобы рассчитывалась энерговыработка за год
        :param power: мощность в МВт
        :param time: число часов в год
        :return: Возвращает энерговыработку за год (в МВт*час)
        """
        ...
        return ...

if __name__ == "__main__":
    # Write your solution here
    pass
