import json

json_file = "services.json"

with open(json_file, 'r', encoding='utf-8') as f:
    json_data = json.loads(f.read())

print(json_data)
print("====================")
print(json_data['services']['debug'])
