class Person:
    def __init__(self, name: str, age: int, gender: str):
        """
        Конструктор класса Person.

        :param name: Имя человека (строка)
        :param age: Возраст человека (целое число)
        :param gender: Пол человека (строка, 'ж' или 'м')
        """
        if not isinstance(name, str) or not isinstance(gender, str):
            raise TypeError("Имя и пол должны быть строками.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом.")

        self.name = name
        self.age = age
        self.gender = gender

    def greet(self) -> str:
        """
        Приветствие от человека.

        :return: Строка с приветствием.
        """
        ...

    def have_birthday(self) -> None:
        """
        Празднование дня рождения.

        :return: None
        """
        ...