import json


def read_json(filename):  # функция для чтения JSON-файла; передаём имя файла для чтения
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_tags(data):  # функция для извлечения списка тегов; передаём список словарей с данными
    result = set()  # создание множества (без повторения одинаковых значений)
    for record in data:
        content = record['content']
        words = content.split()  # создание словаря из слов в описании поста для дальнейшей обработки
        for word in words:
            if word.startswith('#'):
                result.add(word[1:])  # добавление в множество совпадений по словам начинающимся с '#'
    tags = list(result)  # создание списка для дальнейшей сортировки по алфавиту
    tags.sort()  # сортировка списка
    return tags


def find_tag(tag, data):  # функция поиска совпадения тегов в постах; передаём ключевой тег и список словарей
    result = []
    for record in data:
        if f'#{tag}' in record['content']:
            result.append(record)  # добавление словаря в список совпадений
    return result


def add_post(filename, post):  # функция добавления постов в список словарей JSON
    data = read_json(filename)  # чтение JSON
    data.append(post)  # добавление новой записи
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)  # перезапись в файл обновлённых данных
