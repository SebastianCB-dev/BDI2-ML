import json

data_file = open('./items.json', 'r', encoding='utf8')


beck_data = json.loads(data_file.read())

print(beck_data)