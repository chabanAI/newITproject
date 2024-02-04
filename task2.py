class Animal:
    def __init__(self, species: str, sound: str):
        """
        Конструктор класса Animal.

        :param species: Вид животного (строка)
        :param sound: Звук, издаваемый животным (строка)
        
        """
        if not isinstance(species, str) or not isinstance(sound, str):
            raise TypeError("Вид и звук должны быть строками.")
        

        self.species = species
        self.sound = sound
     

    def make_sound(self) -> str:
        """
        Издавание звука животным.

        :return: Строка с издаваемым звуком.
        """
        ...

    def move(self, distance: float) -> None:
        """
        Перемещение животного на указанное расстояние.

        :param distance: Расстояние для перемещения (вещественное число)
        :return: None
        """
        ...