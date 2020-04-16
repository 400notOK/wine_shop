from datetime import datetime


def get_foundation_date():
    return datetime.now().year - 1920


def parse_drinks(drinks):
    drinks_chunk = {}
    for chunk in drinks.split('\n'):
        if 'Название' in chunk:
            drinks_chunk['title'] = chunk.split(': ')[-1]
        if 'Сорт' in chunk and len(chunk.split(': ')) > 1:
            drinks_chunk['type'] = chunk.split(': ')[-1]
        if 'Цена' in chunk:
            drinks_chunk['price'] = chunk.split(': ')[-1]
        if 'Картинка' in chunk:
            drinks_chunk['picture'] = chunk.split(': ')[-1]
        if 'Выгодное предложение' in chunk:
            drinks_chunk['good_offer'] = True
    return drinks_chunk


def collect_drinks(drinks):
    drinks_collection = []
    for chunk in drinks.split('\n\n\n'):
        if '#' in chunk:
            category = {
                'name': chunk.split('# ')[-1],
                'drinks': [],
            }
        else:
            parsed_data = [parse_drinks(drink) for drink in chunk.split('\n\n')]
            category['drinks'].extend(parsed_data)
            drinks_collection.append(category)
            category = {}
    return drinks_collection
