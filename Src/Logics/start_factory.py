
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.settings import settings
from Src.Storage.storage import storage
from Src.Models.reciepe_model import reciepe_model
from Src.Models.reciepe_row import reciepe_row_model
from Src.exceptions import exception_proxy

#
# Класс для обработки данных. Начало работы приложения
#
class start_factory:
    __oprions: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings,
                 _storage: storage = None) -> None:
        
        exception_proxy.validate(_options, settings)
        self.__oprions = _options
        self.__storage = _storage
        
      
    
    def __save(self, key:str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """
       
        exception_proxy.validate(key, str)
        
        if self.__storage == None:
            self.__storage = storage()
            
        self.__storage.data[ key ] = items

    def create(self):
        """
           В зависимости от настроек, сформировать начальную номенклатуру

        Returns:
            _type_: _description_
        """
        
        result = []
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            
            # Формируем и зпоминаем номеклатуру
            result = start_factory.create_nomenclature()
            self.__save( storage.nomenclature_key(), result )
        return result


    def __build(self):
        if self.__storage == None:
            self.__storage = storage()

        items = start_factory.create_nomenclature()

        self.__storage.data[storage.nomenclature_key()] = items
        self.__storage.data[storage.unit_key()] = set([v.unit for v in items])
        self.__storage.data[storage.group_key()] = set([v.group for v in items])    
                
    @property            
    def storage(self):
        """
             Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage

    
    @staticmethod
    def create_nomenclature():
        """
          Фабричный метод Создать список номенклатуры
        """
        
        result = []
        
        
        flour = nomenclature_model("Мука пшеничная")
        flour.group = group_model.create_group()
        flour.unit = unit_model.create_killogram()
        
        result.append(flour)

        butter = nomenclature_model("Масло сливочное")
        butter.group = group_model.create_group()
        butter.unit = unit_model.create_killogram()
        
        result.append(butter)

        sugar = nomenclature_model("Сахар")
        sugar.group = group_model.create_group()
        sugar.unit = unit_model.create_killogram()
        
        result.append(sugar)
    
        eggs = nomenclature_model("Яйца")
        eggs.group = group_model.create_group()
        eggs.unit = unit_model.create_30_pieces()
        
        result.append(eggs)

        vanillin = nomenclature_model("Ванилин")
        vanillin.group = group_model.create_group()
        vanillin.unit = unit_model.create_killogram()
        
        result.append(vanillin)

        cinnamon = nomenclature_model("Корица")
        cinnamon.group = group_model.create_group()
        cinnamon.unit = unit_model.create_killogram()
        
        result.append(cinnamon)

        egg_white = nomenclature_model("Яичный белок")
        egg_white.group = group_model.create_group()
        egg_white.unit = unit_model.create_killogram()
        
        result.append(egg_white)

        powdered_sugar = nomenclature_model("Сахарная пудра")
        powdered_sugar.group = group_model.create_group()
        powdered_sugar.unit = unit_model.create_killogram()
        
        result.append(powdered_sugar)

        cocoa = nomenclature_model("Какао")
        cocoa.group = group_model.create_group()
        cocoa.unit = unit_model.create_killogram()
        
        result.append(cocoa)

        chicken_fillet = nomenclature_model("Куриное филе")
        chicken_fillet.group = group_model.create_group()
        chicken_fillet.unit = unit_model.create_killogram()
        
        result.append(chicken_fillet)

        Romano_salad = nomenclature_model("Салат Романо")
        Romano_salad.group = group_model.create_group()
        Romano_salad.unit = unit_model.create_killogram()
        
        result.append(Romano_salad)

        Parmesan_cheese = nomenclature_model("Сыр Пармезан")
        Parmesan_cheese.group = group_model.create_group()
        Parmesan_cheese.unit = unit_model.create_killogram()
        
        result.append(Parmesan_cheese)

        garlic = nomenclature_model("Чеснок")
        garlic.group = group_model.create_group()
        garlic.unit = unit_model.create_killogram()
        
        result.append(garlic)

        white_bread = nomenclature_model("Белый хлеб")
        white_bread.group = group_model.create_group()
        white_bread.unit = unit_model.create_killogram()
        
        result.append(white_bread)

        salt = nomenclature_model("Соль")
        salt.group = group_model.create_group()
        salt.unit = unit_model.create_killogram()
        
        result.append(salt)

        black_pepper = nomenclature_model("Черный перец")
        black_pepper.group = group_model.create_group()
        black_pepper.unit = unit_model.create_killogram()
        
        result.append(black_pepper)

        olive_oil = nomenclature_model("Оливковое масло")
        olive_oil.group = group_model.create_group()
        olive_oil.unit = unit_model.create_liter()
        
        result.append(olive_oil)

        lemon_juice = nomenclature_model("Лимонный сок")
        lemon_juice.group = group_model.create_group()
        lemon_juice.unit = unit_model.create_liter()
        
        result.append(lemon_juice)

        mustard_of_Dijon = nomenclature_model("Горчица Дижонская")
        mustard_of_Dijon.group = group_model.create_group()
        mustard_of_Dijon.unit = unit_model.create_killogram()
        
        result.append(mustard_of_Dijon)
        
        return result

    
    @staticmethod
    def create_reciepes():
        return [
            reciepe_model(
                'ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ',
            reciepe_row_model(
                nomenculature = nomenclature_model('Пшеничная мука', unit_model.create_kilogramm(), group_model.create_group()),
                unit=unit_model.create_gramm(),
                size=100),
            reciepe_row_model(
                nomenculature = nomenclature_model('Сахар', unit_model.create_kilogramm(), group_model.create_group()),
                unit=unit_model.create_gramm(),
                size=80),
            reciepe_row_model(
                nomenculature = nomenclature_model('Сливочное масло', unit_model.create_gramm(), group_model.create_group()),
                unit=unit_model.create_gramm(),
                size=70),
            reciepe_row_model(
                nomenculature = nomenclature_model('Яйца', unit_model.create_count(), group_model.create_group()),
                unit=unit_model.create_count(),
                size=1),
            reciepe_row_model(
                nomenculature = nomenclature_model('Ванилин', unit_model.create_gramm(), group_model.create_group()),
                unit=unit_model.create_gramm(),
                size=5),
            description='''
Время приготовления: 20 мин
Как испечь вафли хрустящие в вафельнице? Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см.
Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.
Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.
Добавьте в масло яйцо. Предварительно все-таки проверьте масло, не горячее ли оно, иначе яйцо может свариться. Перемешайте яйцо с маслом до однородности.
Всыпьте муку, добавьте ванилин.
Перемешайте массу венчиком до состояния гладкого однородного теста.
Разогрейте вафельницу по инструкции к ней. У меня очень старая, еще советских времен электровафельница. Она может и не очень красивая, но печет замечательно! Я не смазываю вафельницу маслом, в тесте достаточно жира, да и к ней уже давно ничего не прилипает. Но вы смотрите по своей модели. Выкладывайте тесто по столовой ложке. Можно класть немного меньше теста, тогда вафли будут меньше и их получится больше.
Пеките вафли несколько минут до золотистого цвета. Осторожно откройте вафельницу, она очень горячая! Снимите вафлю лопаткой. Горячая она очень мягкая, как блинчик. Но по мере остывания становится твердой и хрустящей. Такие вафли можно свернуть трубочкой. Но делать это надо сразу же после выпекания, пока она мягкая и горячая, потом у вас ничего не получится, вафля поломается. Приятного аппетита!
            ''')
        ]
    
    