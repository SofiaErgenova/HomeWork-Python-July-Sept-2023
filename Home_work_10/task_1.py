""" Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного 
(название одного из созданных классов) 
и параметры для этого типа.
○ Внутри класса создайте экземпляр 
на основе переданного типа и верните его из класса-фабрики. """

class Animals():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Insect(Animals):
    def __init__(self, color, *args, **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)

    def spec(self):
        return f'{self.color = }'
    
class Birds(Animals):
    def __init__(self, feather_color, *args, **kwargs):
        self.feather_color = feather_color
        super().__init__(*args, **kwargs)

    def spec(self):
        return f'{self.feather_color = }'
    
class Fishes(Animals):
    def __init__(self, scale_color, *args, **kwargs):
        self.scale_color = scale_color
        super().__init__(*args, **kwargs)

    def spec(self):
        return f'{self.scale_color = }'


class Factory:

   def create_animal(self, animal_type, *args, **kwargs):
        if animal_type == 'Insect':
            return Insect(*args, **kwargs)
        elif animal_type == 'Birds':
            return Birds(*args, **kwargs)
        elif animal_type == 'Fishes':
            return Fishes(*args, **kwargs)
        else:
            return None

factory = Factory()

insect = factory.create_animal('Insect', color='red', name='Gee', age=1)

bird = factory.create_animal('Birds', feather_color='blue', name='Kоко', age=5)

fishe = factory.create_animal('Fishes', scale_color='silver', name='Поньо', age=3)


# второе решение через словарь

class Fabric:
    def __init__(self, animal_type, **kwargs):
        self.animal_type = animal_type
        self.kwargs = kwargs
    
    def get_animal(self):
        animal_dict = {"насекомые": Insect, 'рыбы': Fishes, 'птицы': Birds}
        animal_class = animal_dict.get(self.animal_type)
        if animal_class:
            return animal_class(**self.kwargs)
        return None




fabric = Fabric('насекомые', color='red', name='Kоко', age=5)
insect = fabric.get_animal()

fabric = Fabric('рыбы', scale_color='silver', name='Kоко', age=5)
fish = fabric.get_animal()

fabric = Fabric('птицы', feather_color='blue', name='Kоко', age=5)
bird = fabric.get_animal()

