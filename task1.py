class Country:
    def __init__(self, name: str, capital: str, population: int, language: str):
        """
        Конструктор класса Country.

        :param name: Название страны (строка)
        :param capital: Столица страны (строка)
        :param population: Население страны (целое число)
        :param language: Официальный язык страны (строка)
        """
        if not isinstance(name, str) or not isinstance(capital, str) or not isinstance(language, str):
            raise TypeError("Название, столица и язык должны быть строками.")
        if not isinstance(population, int) or population < 0:
            raise ValueError("Население должно быть неотрицательным целым числом.")
        
        self.name = name
        self.capital = capital
        self.population = population
        self.language = language

    def get_info(self) -> str:
        """
        Получить информацию о стране.

        :return: Строка с информацией о стране.
        """
        return f"{self.name} - Capital: {self.capital}, Population: {self.population}, Language: {self.language}"



    def update_population(self, new_population: int) -> None:
        """
        Обновить информацию о населении страны.

        :param new_population: Новое значение населения (целое число)
        """
        ...
        