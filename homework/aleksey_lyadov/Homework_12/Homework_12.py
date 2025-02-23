# Создание классов цветы
from operator import attrgetter


class Flowers:

    def __init__(self, colour, stem_length, name, lifespan, cost):
        self.__colour = colour
        self.__stem_length = stem_length
        self.__name = name
        self.__lifespan = lifespan  # средняя продолжительность жизни в днях
        self.__cost = cost

    def __str__(self):
        return (f"{self.name} Цена: {self.cost} руб., Время жизни: "
                f"{self.lifespan} дней, Длина стебля: {self.stem_length}см")

    @property
    def colour(self):
        return self.__colour

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def name(self):
        return self.__name

    @property
    def lifespan(self):
        return self.__lifespan

    @property
    def cost(self):
        return self.__cost


class Rose(Flowers):
    def __init__(self):
        super().__init__('Красный', 50, 'Роза', 7, 150)


class Tulip(Flowers):
    def __init__(self):
        super().__init__('Желтый', 30, 'Тюльпан', 5, 80)


class Daisy(Flowers):
    def __init__(self):
        super().__init__('Белый', 20, 'Ромашка', 3, 100)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def __add_flower(self, flower):
        self.flowers.append(flower)

    def __average_lifespan(self):
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers) if self.flowers else 0

    def __sort(self):
        sorted_bouquet = sorted(self.flowers, key=attrgetter(
            'name', 'colour', 'cost', 'stem_length', 'lifespan'))
        return [str(flower) for flower in sorted_bouquet]

    def __find_flowers_by_lifespan(self, lifespan):
        found_flowers = [flower for flower in
                         self.flowers if flower.lifespan == lifespan]
        return [str(flower) for flower in found_flowers]

    @property
    def add_flower(self):
        return self.__add_flower

    @property
    def average_lifespan(self):
        return self.__average_lifespan

    @property
    def sort(self):
        return self.__sort

    @property
    def find_flowers_by_lifespan(self):
        return self.__find_flowers_by_lifespan

    def __str__(self):
        bouquet_details = ", ".join(str(flower) for flower in self.flowers)
        return (f'Среднее время увядания: '
                f'{int(self.average_lifespan())} дней\n{bouquet_details}')


# Создание экземпляров цветов
rose = Rose()
tulip = Tulip()
daisy = Daisy()

# Создание букета
bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(daisy)
print(bouquet)
print(bouquet.sort())
print(bouquet.find_flowers_by_lifespan(5))
