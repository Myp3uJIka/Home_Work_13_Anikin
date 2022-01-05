import json


def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_tags(data):
    result = set()
    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                result.add(word[1:])
    tags = list(result)
    tags.sort()
    return tags


def find_tag(tag, data):
    result = []
    for record in data:
        if tag in record['content']:
            result.append(record)
    return result
