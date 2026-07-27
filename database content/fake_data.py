from faker import Faker
import random

fake = Faker('ru_RU')

def generate_species():
    species_list = [
        "Собака", "Кошка", "Попугай", "Хомяк", "Черепаха",
        "Кролик", "Змея", "Ящерица", "Птица", "Рыбка",
        "Морская свинка", "Крыса", "Хорёк", "Шиншилла", "Улитка",
        "Игуана", "Паук", "Хамелеон", "Песчанка", "Пони"
    ]
    return [{"name": name} for name in species_list]

BREEDS_BY_SPECIES = {
    "Собака": ["Лабрадор", "Такса", "Овчарка", "Бульдог", "Пудель", 
               "Доберман", "Ротвейлер", "Чихуахуа", "Шпиц", "Хаски",
               "Далматинец", "Бигль", "Мопс", "Корги", "Сеттер"],
    "Кошка": ["Персидская", "Сиамская", "Британская", "Мейн-кун", "Сфинкс",
              "Бенгальская", "Русская голубая", "Шотландская", "Ориентал", "Рэгдолл",
              "Бурма", "Абиссинская", "Норвежская лесная", "Сибирская", "Балинезийская"],
    "Попугай": ["Волнистый", "Корелла", "Ара", "Какаду", "Жако",
                "Неразлучник", "Розелла", "Амазон", "Ожереловый", "Лори",
                "Аратинга", "Какарик", "Сенегальский", "Эклектус", "Квакер"],
    "Хомяк": ["Джунгарский", "Сирийский", "Кэмпбелла", "Роборовский",
              "Китайский", "Эдварда", "Радеау", "Брандта", "Соболиный",
              "Жемчужный", "Коричневый", "Оранжевый", "Белый", "Золотой", "Черный"],
    "Черепаха": [ "Красноухая", "Среднеазиатская", "Болотная", "Зеленая", "Греческая",
            "Египетская", "Индийская", "Каспийская", "Мексиканская", "Леопардовая",
            "Китайский трионикс", "Мускусная", "Иловая"],
    "Кролик": [
        "Вислоухий баран", "Голландский", "Ангорский", "Рекс", "Гермелин",
        "Бабочка", "Новозеландский", "Калифорнийский", "Серебристый", "Фландр",
        "Львиноголовый", "Карликовый", "Огневка", "Бельгийский великан"
    ],
   "Змея": [
        "Королевский питон", "Молочная змея", "Кукурузная змея", "Боа констриктор",
        "Маисовый полоз", "Тигровый питон", "Радужный удав", "Уж обыкновенный",
        "Черная мамба", "Зеленая мамба", "Гадюка", "Щитомордник", "Анаконда"
    ],
    "Ящерица": [
        "Геккон", "Игуана", "Агама", "Хамелеон", "Сцинк", "Варан",
        "Анолис", "Молох", "Поясохвост", "Живородящая", "Плащеносная",
        "Водяной дракон", "Бородатая агама"
    ],
    "Птица": ["Ворон", "Дрозд", "Канарейка", "Грач", "Петух", "Снегирь",
              "Утка", "Лебедь", "Щегол", "Сова", "Голубь", "Воробей", "Синица",
              "Сойка", "Дятел"],
    "Рыбка": [
        "Гуппи", "Скалярия", "Петушок", "Меченосец", "Моллинезия",
        "Данио", "Барбус", "Неон", "Золотая рыбка", "Карп кои",
        "Дискус", "Астронотус", "Пиранья", "Арована", "Сом"
    ],
    "Морская свинка": [
        "Американская", "Абиссинская", "Перуанская", "Тексель", "Шелти",
        "Коронет", "Рекс", "Тедди", "Альпака", "Мерино", "Лункария",
        "Белая", "Трехцветная", "Гималайская"
    ],
    "Крыса": [
        "Стандарт", "Дамбо", "Рекс", "Бесхвостая", "Сфинкс", "Сатин",
        "Пуховая", "Альбинос", "Капюшон", "Беркшир", "Английская",
        "Русская голубая", "Сиамская"
    ],
    "Хорёк": [
        "Альбинос", "Соболь", "Шампань", "Корица", "Черный",
        "Белый", "Пастель", "Серебристый", "Темноглазый белый",
        "Панда", "Блейз", "Далматинец", "Шоколадный"
    ],
    "Шиншилла": [
        "Стандарт серая", "Черный бархат", "Белая", "Сапфир", "Фиолет",
        "Бежевая", "Гомобежевая", "Эбони", "Коричневая", "Гетеробежевая",
        "Пастель", "Бело-розовая", "Антрацит"
    ],
    "Улитка": [
        "Ахатина", "Виноградная", "Катушка", "Физа", "Мелания",
        "Хелена", "Мариза", "Неретина", "Ампулярия", "Теодоксус",
        "Лужанка", "Цепея", "Битиния"
    ],
    "Игуана": [
        "Зеленая", "Синяя", "Красная", "Пустынная", "Морская",
        "Чаквелла", "Анолис", "Василиск", "Шлемоносная", "Кольцехвостая",
        "Шипохвостая", "Шишковатая", "Шлемоносый василиск"
    ],
    "Паук": [
        "Птицеед", "Крестовик", "Скакун", "Волк", "Бродяга",
        "Черная вдова", "Тарантул", "Сенокосец", "Домовый",
        "Серебрянка", "Каракурт", "Бразильский странствующий",
        "Мышиный"
    ],
    "Хамелеон": [
        "Йеменский", "Пантеровый", "Джексона", "Ковровый", "Четырехрогий",
        "Малый", "Гигантский", "Фишера", "Намаква", "Брукезия",
        "Рудис", "Хохлатый", "Карликовый"
    ],
    "Песчанка": [
        "Монгольская", "Когтистая", "Индийская", "Персидская", "Сундевалла",
        "Толстохвостая", "Карликовая", "Жирнохвостая", "Короткоухая",
        "Пушистохвостая", "Белуджистанская", "Египетская", "Королевская"
    ],
    "Пони": ["Карликовый", "Золотой", "Большой", "Волнистый", "Белый",
             "В яблоко", "Серый", "Черный", "Голубой", "Пятнистый",
             "Полосатый", "Пушистый", "Китайский", "Японский", "Коричневый"]
}

def generate_breeds(species_list):
    breeds = []
    for species in species_list:
        species_name = species["name"]
        species_id = species["species_id"]
        for breed_name in random.sample(BREEDS_BY_SPECIES.get(species_name, []), 
                                      min(15, len(BREEDS_BY_SPECIES.get(species_name, [])))):
            breeds.append({
                "name": breed_name,
                "species_id": species_id
            })
    return breeds

def generate_suppliers(count=50):
    suppliers = []
    for _ in range(count):
        suppliers.append({
            'name': fake.company()  
        })
    return suppliers

def generate_veterinarians(count=50):
    veterinarians = []
    specializations = [
        'Хирург', 'Терапевт', 'Офтальмолог', 'Дерматолог', 
        'Кардиолог', 'Невролог', 'Онколог', 'Стоматолог',
        'Уролог', 'Лаборант'
    ]
    qualifications = ['Высшая', 'Первая', 'Вторая']
    
    for _ in range(count):
        veterinarians.append({
            'first_name': fake.first_name_male() if random.choice([True, False]) else fake.first_name_female(),
            'second_name': fake.last_name_male() if random.choice([True, False]) else fake.last_name_female(),
            'middle_name': fake.middle_name_male() if random.choice([True, False]) else fake.middle_name_female(),
            'phone_number': fake.phone_number(),
            'email': fake.email(),
            'specialization': random.choice(specializations),
            'qualification': random.choice(qualifications)
        })
    return veterinarians

def generate_administrators(count=50):
    administrators = []
    for _ in range(count):
        gender = random.choice(['male', 'female'])
        administrators.append({
            'first_name': fake.first_name_male() if gender == 'male' else fake.first_name_female(),
            'second_name': fake.last_name_male() if gender == 'male' else fake.last_name_female(),
            'middle_name': fake.middle_name_male() if gender == 'male' else fake.middle_name_female(),
            'phone_number': f"+7({fake.random_int(900, 999)}){fake.random_int(100, 999)}-{fake.random_int(10, 99)}-{fake.random_int(10, 99)}",
            'email': f"{fake.user_name()}{fake.random_int(1, 99)}@{fake.domain_name()}"
        })
    return administrators


def generate_services():
    services = [
        {"name": "Первичный осмотр", "price": 1500.00},
        {"name": "Повторный осмотр", "price": 1000.00},
        {"name": "Вакцинация", "price": 2000.00},
        {"name": "Чипирование", "price": 2500.00},
        {"name": "Кастрация кота", "price": 5000.00},
        {"name": "Стерилизация кошки", "price": 8000.00},
        {"name": "УЗИ брюшной полости", "price": 3500.00},
        {"name": "Рентген", "price": 3000.00},
        {"name": "Анализ крови", "price": 2500.00},
        {"name": "Чистка зубов", "price": 4000.00},
        {"name": "Удаление зубов", "price": 6000.00},
        {"name": "Обработка от паразитов", "price": 1800.00},
        {"name": "Подстригание когтей", "price": 800.00},
        {"name": "Перевязка", "price": 1200.00},
        {"name": "Наложение швов", "price": 3500.00},
        {"name": "Капельница", "price": 2000.00},
        {"name": "Госпитализация (сутки)", "price": 4500.00},
        {"name": "ЭКГ", "price": 2800.00},
        {"name": "Анализ мочи", "price": 1500.00},
        {"name": "Анализ кала", "price": 1700.00},
        {"name": "Тримминг", "price": 2500.00},
        {"name": "Груминг мелких пород", "price": 3500.00},
        {"name": "Груминг средних пород", "price": 4500.00},
        {"name": "Груминг крупных пород", "price": 6000.00},
        {"name": "Вызов на дом", "price": 3000.00},
        {"name": "Эвтаназия", "price": 4000.00},
        {"name": "Кремация", "price": 7000.00},
        {"name": "Скорая помощь", "price": 5000.00},
        {"name": "Консультация диетолога", "price": 2500.00},
        {"name": "Консультация хирурга", "price": 3000.00},
        {"name": "Консультация онколога", "price": 3500.00},
        {"name": "Физиотерапия", "price": 2800.00},
        {"name": "Лазерная терапия", "price": 3200.00},
        {"name": "Химиотерапия", "price": 8500.00},
        {"name": "Онкологическая операция", "price": 15000.00},
        {"name": "Офтальмологический осмотр", "price": 2200.00},
        {"name": "Стоматологический осмотр", "price": 1800.00},
        {"name": "Дерматологический осмотр", "price": 2000.00},
        {"name": "Кардиологический осмотр", "price": 3500.00},
        {"name": "Неврологический осмотр", "price": 3800.00},
        {"name": "Ортопедический осмотр", "price": 3000.00},
        {"name": "Родыспоможение", "price": 10000.00},
        {"name": "Кесарево сечение", "price": 12000.00},
        {"name": "Микроскопия кожи", "price": 1800.00},
        {"name": "Цитологическое исследование", "price": 2500.00},
        {"name": "Гистологическое исследование", "price": 5000.00},
        {"name": "Анестезия", "price": 3000.00},
        {"name": "Реанимационные мероприятия", "price": 6000.00},
        {"name": "Интенсивная терапия", "price": 4500.00},
        {"name": "Переливание крови", "price": 8000.00}
    ]
    return services

def generate_products(supplier_ids, count=700):
    products = []
    categories = {
        'Корм': ['сухой', 'влажный', 'консервы', 'премиум', 'холистик'],
        'Лекарства': ['антибиотики', 'витамины', 'противопаразитарные', 'анальгетики', 'противовоспалительные'],
        'Аксессуары': ['ошейники', 'поводки', 'миски', 'лежанки', 'переноски'],
        'Гигиена': ['шампуни', 'расчески', 'зубные щетки', 'пеленки', 'салфетки'],
        'Игрушки': ['мячи', 'пищалки', 'интерактивные', 'канаты', 'грызунки']
    }
    
    countries = ['Россия', 'Германия', 'Франция', 'США', 'Великобритания', 'Китай', 'Италия', 'Испания']

    supplier_cycle = supplier_ids * (count // len(supplier_ids))
    remaining = count % len(supplier_ids)
    supplier_cycle += supplier_ids[:remaining]
    
    for _ in range(count):
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category])
        products.append({
            'name': f"{category} {subcategory} {fake.word()}",
            'country': random.choice(countries),
            'price': round(random.uniform(50, 5000), 2),
            'supplier_id': random.choice(supplier_ids)
        })
    return products

def generate_owners(count=200):
    owners = []
    for _ in range(count):
        gender = random.choice(['male', 'female'])
        owners.append({
            'first_name': fake.first_name_male() if gender == 'male' else fake.first_name_female(),
            'second_name': fake.last_name_male() if gender == 'male' else fake.last_name_female(),
            'middle_name': fake.middle_name_male() if gender == 'male' else fake.middle_name_female(),
            'phone_number': f"+7({fake.random_int(900, 999)}){fake.random_int(100, 999)}-{fake.random_int(10, 99)}-{fake.random_int(10, 99)}",
            'email': f"{fake.user_name()}{random.randint(1, 99)}@{fake.domain_name()}",
            'address': f"{fake.city()}, ул. {fake.street_name()}, д. {fake.building_number()}"
        })
    return owners

def generate_pets(owner_ids, species_list, breed_list, pets_per_owner=(1, 30)):
    pets = []
    pet_names = {
        'Собака': ['Шарик', 'Рекс', 'Джек', 'Белка', 'Тузик', 'Лорд', 'Цезарь', 
                  'Бобик', 'Ральф', 'Арчи', 'Граф', 'Дейзи', 'Лайма', 'Зевс', 'Оскар', 'Чарли', 'Тедди'],
        'Кошка': ['Мурзик', 'Васька', 'Пушистик', 'Снежок', 'Рыжик', 'Персик', 'Барсик', 'Мурка',
                 'Симба', 'Луна', 'Оливер', 'Лео', 'Мия', 'Тигра', 'Сэм', 'Люси', 'Гарфилд', 'Нюша'],
        'Попугай': ['Кеша', 'Гоша', 'Рио', 'Арчи', 'Яша', 'Кира', 'Лора', 'Чижик',
                   'Коко', 'Жак', 'Пип', 'Рики', 'Чико', 'Бонни', 'Клео', 'Лори'],
        'Хомяк': ['Пушок', 'Нюша', 'Боня', 'Фунтик', 'Пиксель', 'Кнопа', 'Сеня', 'Зефирка',
                 'Хома', 'Буся', 'Мотя', 'Кругляш', 'Цуки', 'Филя', 'Шуша', 'Плюша'],
        'Черепаха': ['Тоша', 'Шелл', 'Донни', 'Лео', 'Рафа', 'Мики', 'Сплинтер', 'Вальт',
                    'Спиди', 'Касси', 'Тортилла', 'Бабблз', 'Шелдон', 'Квази', 'Танк'],
        'Кролик': ['Роджер', 'Багз', 'Лола', 'Снежок', 'Пухля', 'Флаффи', 'Банни', 'Джаспер',
                  'Орео', 'Коко', 'Питер', 'Дейзи', 'Макс', 'Лулу', 'Симба'],
        'Змея': ['Нага', 'Каа', 'Зигги', 'Сайрен', 'Пайтон', 'Медяна', 'Слизи', 'Вайпер',
                'Барон', 'Гиза', 'Спаркл', 'Эсмеральда', 'Оникс', 'Салазар'],
        'Ящерица': ['Годзилла', 'Иго', 'Рекс', 'Спайк', 'Дарт', 'Скала', 'Зилла', 'Гекко',
                   'Риптор', 'Драко', 'Твигги', 'Йоши', 'Комодо', 'Сцинк'],
        'Птица': ['Квизи', 'Твити', 'Блю', 'Скай', 'Санни', 'Пип', 'Чип', 'Дейзи',
                 'Рио', 'Альба', 'Перси', 'Спарки', 'Феникс', 'Валькирия'],
        'Рыбка': ['Немо', 'Дори', 'Баббл', 'Голди', 'Флиппер', 'Спот', 'Близзард', 'Неон',
                 'Азур', 'Коралл', 'Плавник', 'Жабр', 'Скаляр', 'Гуппи'],
        'Морская свинка': ['Пигги', 'Гвинни', 'Флафф', 'Сквик', 'Бекон', 'Панкейк', 'Мох', 'Пух',
                          'Шоколад', 'Карамель', 'Пончик', 'Бисквит', 'Пельмень', 'Вафля'],
        'Крыса': ['Рэтчет', 'Рэтту', 'Сквиджи', 'Твич', 'Сникерс', 'Пипсквик', 'Гном', 'Шашлык',
                 'Рокки', 'Скраффи', 'Чиззи', 'Рэттиган', 'Сплinter', 'Тайл'],
        'Хорёк': ['Фредди', 'Ферби', 'Ласка', 'Джинкс', 'Зип', 'Слим', 'Виззи', 'Фуззи',
                'Нудл', 'Сквирт', 'Фигаро', 'Локи', 'Пикси', 'Твинкл'],
        'Шиншилла': ['Чилла', 'Душка', 'Плюш', 'Шани', 'Чоко', 'Латте', 'Марш', 'Зефир',
                    'Бамбино', 'Чиби', 'Пуфик', 'Сноу', 'Мисти', 'Эльф'],
        'Улитка': ['Турбо', 'Шелл', 'Спиди', 'Слизз', 'Баббл', 'Гэри', 'Эскарго', 'Сникер',
                  'Крулл', 'Спираль', 'Койл', 'Слимп', 'Густо', 'Баблз'],
        'Игуана': ['Изи', 'Годзи', 'Спайк', 'Зилла', 'Рекс', 'Драгон', 'Торч', 'Смауг',
                  'Риптор', 'Скала', 'Огненный', 'Альберт', 'Кома', 'Зорро'],
        'Паук': ['Питер', 'Шелоб', 'Арахна', 'Веном', 'Тара', 'Фанг', 'Чарли', 'Скай',
                'Октобер', 'Инки', 'Спайдер', 'Уиджи', 'Локи', 'Зорг'],
        'Хамелеон': ['Камео', 'Рэйнбоу', 'Зигги', 'Лео', 'Джаспер', 'Рипли', 'Пантер', 'Мистик',
                    'Сэм', 'Блендер', 'Краска', 'Халк', 'Ирис', 'Клевер'],
        'Песчанка': ['Джерри', 'Санд', 'Джинжер', 'Ниббл', 'Скутер', 'Пип', 'Твич', 'Джампер',
                    'Бисквит', 'Флик', 'Зип', 'Спарки', 'Флип', 'Бамбл'],
        'Пони': ['Пинки', 'Твай', 'Рарити', 'Эпл', 'Флаттер', 'Спайк', 'Скут', 'Каденс',
               'Санни', 'Луна', 'Стар', 'Шугар', 'Баттер', 'Блу']
    }
    
    used_chip_numbers = set()
    owner_pet_counts = {owner_id: random.randint(*pets_per_owner) for owner_id in owner_ids}
    
    for owner_id, pet_count in owner_pet_counts.items():
        for _ in range(pet_count):
            species = random.choice(species_list)
            species_id = species['species_id']
            species_name = species['name']
            
            available_breeds = [b for b in breed_list if b['species_id'] == species_id]
            breed = random.choice(available_breeds) if available_breeds else None

            chip = None
            if random.random() > 0.7:
                while True:
                    new_chip = random.randint(100000000, 2147483647)
                    if new_chip not in used_chip_numbers:
                        used_chip_numbers.add(new_chip)
                        chip = new_chip
                        break
            
            name_options = pet_names.get(species_name, ['Дружок', 'Счастливчик', 'Лапуля'])
            
            pets.append({
                'nickname': random.choice(name_options),
                'birth_date': fake.date_between(start_date='-15y', end_date='-1y').strftime('%Y-%m-%d'),
                'sex': random.choice(['Male', 'Female']),
                'allergy': random.choice([None, 'Пыльца', 'Курица', 'Злаки', 'Блошиный укус']),
                'chip_number': chip,
                'owner_id': owner_id,
                'species_id': species_id,
                'breed_id': breed['breed_id'] if breed else None })
    
    return pets

def generate_purchases(owner_ids, product_ids, admin_ids, purchases_per_owner=(40, 80)):
    purchases = []
    owner_purchase_counts = {owner_id: random.randint(*purchases_per_owner) for owner_id in owner_ids}
    total_purchases = sum(owner_purchase_counts.values())

    admin_pool = []

    base_per_admin = max(1, total_purchases // len(admin_ids) - 10)
    for admin_id in admin_ids:
        admin_pool.extend([admin_id] * base_per_admin)

    remaining = total_purchases - len(admin_pool)
    if remaining > 0:
        extra_admins = random.choices(admin_ids, k=remaining)
        admin_pool.extend(extra_admins)
    random.shuffle(admin_pool)  

    product_weights = [random.uniform(0.3, 1.7) for _ in product_ids]  # Разная популярность
    product_pool = random.choices(
        product_ids, 
        weights=product_weights,
        k=total_purchases
    )
    purchase_index = 0
    for owner_id, purchase_count in owner_purchase_counts.items():
        for _ in range(purchase_count):
            purchases.append({
                'purchase_date': fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),
                'product_id': product_pool[purchase_index],
                'owner_id': owner_id,
                'admin_id': admin_pool[purchase_index]
            })
            purchase_index += 1
    
    return purchases

def generate_appointments(pet_list, service_ids, admin_ids, appointments_per_pet=(20, 50)):
    appointments = []
    reasons = [
        "Плановый осмотр", "Вакцинация", "Травма", 
        "Кожные проблемы", "Проблемы с ЖКТ", "Стоматология",
        "Аллергия", "Кастрация/стерилизация", "Чипирование"
    ]
    treatments = [
        "Назначены лекарства", "Рекомендован отдых", 
        "Проведена операция", "Назначена диета",
        "Рекомендованы дополнительные анализы", "Проведена обработка"
    ]
    conclusions = [
        "Здоров", "Требуется наблюдение", "Хроническое заболевание",
        "Острое состояние", "Послеоперационный уход", "Ремиссия"
    ]
    pet_appointment_counts = {pet['pet_id']: random.randint(*appointments_per_pet) for pet in pet_list}
    total_appointments = sum(pet_appointment_counts.values())
    
    admin_appointment_counts = {}
    remaining = total_appointments
    num_admins = len(admin_ids)
    
    for i, admin_id in enumerate(admin_ids[:-1]):
        min_a = max(20, remaining - 50 * (num_admins - i - 1))
        max_a = min(50, remaining - 20 * (num_admins - i - 1))
        if min_a > max_a:
            count = (min_a + max_a) // 2
        else:
            count = random.randint(min_a, max_a)
            
        admin_appointment_counts[admin_id] = count
        remaining -= count

    admin_appointment_counts[admin_ids[-1]] = remaining

    admin_pool = []
    for admin_id, count in admin_appointment_counts.items():
        admin_pool.extend([admin_id] * count)
    random.shuffle(admin_pool)
    
    appointment_index = 0
    for pet in pet_list:
        pet_id = pet['pet_id']
        owner_id = pet['owner_id']
        pet_services = [random.choice(service_ids) for _ in range(pet_appointment_counts[pet_id])]
        for service_id in pet_services:
            appointment_date = fake.date_between(start_date='-2y', end_date='today')
            appointments.append({
                'status': random.choice(['Completed', 'Cancelled', 'No-show']),
                'appointment_date': appointment_date.strftime('%Y-%m-%d'),
                'appointment_time': fake.time(pattern='%H:%M'),
                'reason': random.choice(reasons),
                'conclusion': random.choice(conclusions) if random.random() > 0.2 else None,
                'treatment': random.choice(treatments) if random.random() > 0.3 else None,
                'service_id': service_id,
                'pet_id': pet_id,
                'owner_id': owner_id,
                'admin_id': admin_pool[appointment_index]
            })
            appointment_index += 1
    return appointments

def generate_vet_appointments(appointment_ids, vet_ids):
    vet_appointments = []
    vet_cycle = (vet_ids * ((len(appointment_ids) // len(vet_ids)) + 1))[:len(appointment_ids)]
    for i, appointment_id in enumerate(appointment_ids):
        vet_appointments.append({
            'appointment_id': appointment_id,
            'vet_id': vet_cycle[i]
        })
        if random.random() < 0.3:
            additional_vets = random.sample(vet_ids, random.randint(1, 2))
            for vet_id in additional_vets:
                if vet_id != vet_cycle[i]:  
                    vet_appointments.append({
                        'appointment_id': appointment_id,
                        'vet_id': vet_id
                    })
    return vet_appointments
