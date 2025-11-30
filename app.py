from flask import Flask, render_template

app = Flask(__name__)

# Данные меню с описаниями
menu_data = {
    'classic': [
        {'name': 'Тот самый PARADISE', 'price': 3200, 'description': 'Наша фирменная смесь - идеальный баланс вкуса и крепости'},
        {'name': 'Грейпфрутовый', 'price': 3800, 'description': 'Свежий цитрусовый вкус с легкой горчинкой'},
        {'name': 'Гранат', 'price': 4600, 'description': 'Сладкий и насыщенный вкус спелого граната'},
        {'name': 'Абонент недоступен', 'price': 5200, 'description': 'Загадочная смесь с необычным послевкусием'},
        {'name': 'Двойной ананас', 'price': 6400, 'description': 'Тропический вкус спелого ананаса в двойной концентрации'},
        {'name': 'Помело', 'price': 6700, 'description': 'Нежный цитрусовый вкус с освежающим эффектом'},
        {'name': 'Дыня', 'price': 9200, 'description': 'Сладкий аромат спелой дыни - лето круглый год'},
        {'name': 'Арбуз', 'price': 10500, 'description': 'Освежающий вкус арбуза с ярким послевкусием'},
    ],
    'fast_furious': [
        {'name': 'WTO TOBACCO', 'price': 1000, 'description': 'Мощная добавка для увеличения крепости'},
        {'name': 'Bonche', 'price': 800, 'description': 'Премиальная добавка с мягким воздействием'},
        {'name': "Trofimoff's", 'price': 600, 'description': 'Классическая добавка для ценителей крепости'},
        {'name': 'Brume', 'price': 400, 'description': 'Легкая добавка для мягкого усиления'},
        {'name': 'Dokha', 'price': 300, 'description': 'Традиционная добавка восточного происхождения'},
    ],
    'paradise_special': [
        {'name': 'NIGHT PARADISE', 'price': 12500, 'description': 'Эксклюзивная смесь для ночных сессий - темный и насыщенный вкус'},
        {'name': 'LOVE PARADISE', 'price': 8600, 'description': 'Романтическая смесь с нежными фруктовыми нотами'},
        {'name': 'DOUBLE TROPICAL', 'price': 13800, 'description': 'Тропическая феерия из экзотических фруктов'},
        {'name': 'FRUIT PARADISE', 'price': 15500, 'description': 'Фруктовый микс из лучших вкусов в одной чаше'},
        {'name': 'LIFE PARADISE', 'price': 35000, 'description': 'Легендарная смесь премиум-класса - уникальный опыт на всю жизнь'},
    ]
}

# Отзывы
testimonials = [
    {
        'name': 'Александр',
        'rating': 5,
        'text': 'Лучшая кальянная в городе! Обслуживание на высшем уровне, кальян-мастер настоящий профессионал. Обязательно вернусь!',
        'date': '15 декабря 2024'
    },
    {
        'name': 'Мария',
        'rating': 5,
        'text': 'Невероятная атмосфера! Кальян FRUIT PARADISE просто потрясающий. Уютное место для отдыха с друзьями.',
        'date': '10 декабря 2024'
    },
    {
        'name': 'Дмитрий',
        'rating': 5,
        'text': 'Регулярно хожу в PARADISE. Качество всегда на высоте, большой выбор вкусов, приятная обстановка. Рекомендую!',
        'date': '8 декабря 2024'
    },
    {
        'name': 'Елена',
        'rating': 5,
        'text': 'Первый раз была в кальянной такого уровня. Мастер подобрал идеальный вкус, все было на высшем уровне!',
        'date': '5 декабря 2024'
    },
    {
        'name': 'Иван',
        'rating': 5,
        'text': 'Отличное место для вечернего отдыха. Кальян NIGHT PARADISE - это нечто особенное! Обслуживание безупречное.',
        'date': '2 декабря 2024'
    },
    {
        'name': 'Анна',
        'rating': 5,
        'text': 'Приятная атмосфера, профессиональные мастера, превосходный выбор кальянов. PARADISE действительно оправдывает свое название!',
        'date': '28 ноября 2024'
    }
]

# Статистика
stats = [
    {'number': '50+', 'label': 'Вкусов кальяна'},
    {'number': '1000+', 'label': 'Довольных клиентов'},
    {'number': '5', 'label': 'Лет опыта'},
    {'number': '24/7', 'label': 'Поддержка'},
]

@app.route('/')
def index():
    return render_template('index.html', testimonials=testimonials[:3], stats=stats)

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_data=menu_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/testimonials')
def all_testimonials():
    return render_template('testimonials.html', testimonials=testimonials)

if __name__ == '__main__':
    app.run()

