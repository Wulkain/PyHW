class Animal:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def unique(self):
        pass


class Fish(Animal):
    MIN_PARAM = 50
    MAX_PARAM = 500

    def __init__(self, name: str, depth: int):
        super().__init__(name)
        self.__depth = depth

    def get_depth(self):
        return self.__depth

    def unique(self):
        if self.__depth < self.MIN_PARAM:
            return f'{self._name} - мелководная рыба'
        elif self.__depth > self.MAX_PARAM:
            return f'{self._name} - глубоководная рыба'
        else:
            return f'{self._name} - средневодная рыба'


class Bird(Animal):
    def __init__(self, name: str, wing: int):
        super().__init__(name)
        self.__wing = wing

    def get_wing(self):
        return self.__wing

    def unique(self):
        return f'Размах крыла птицы {self.get_name()} - {self.__wing * 2}'


class Mammal(Animal):
    MIN_PARAM = 10
    MAX_PARAM = 80

    def __init__(self, name: str, speed: int):
        super().__init__(name)
        self.__speed = speed

    def get_depth(self):
        return self.__depth

    def unique(self):
        if self.__speed < self.MIN_PARAM:
            return f'{self._name} - медленное животное'
        elif self.__speed > self.MAX_PARAM:
            return f'{self._name} - быстрейшее животное'
        else:
            return f'{self._name} - обычное животное'


if __name__ == '__main__':
    animals = []

    animals.append(Fish('Карась', 10))
    animals.append(Fish('Щука', 100))
    animals.append(Fish('Удильщик', 800))

    animals.append(Bird('Воробей', 3))
    animals.append(Bird('Сорока', 30))
    animals.append(Bird('Альбатрос', 60))

    animals.append(Mammal('Ленивец', 4))
    animals.append(Mammal('Волк', 40))
    animals.append(Mammal('Гепард', 120))

    for animal in animals:
        print(animal.unique())