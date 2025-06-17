# Сериализация и Десериализация данных
# Виды сериализаций:
# 1. Бинарная сериализация данных - данные собираются в некую последовательную
# структуру состящую из чисто байтовой последовательности
# 2. Текстовая сериализация данных - XML -> JSON

import json

file = open("example.json", "r", encoding="utf-8")
json_obj = json.load(file)
file.close()

print(json_obj["total"]["key_array"][3]["key_1"])

json_obj["total"]["key_array"][3]["key_1"] = "value"
print(json_obj["total"]["key_array"][3]["key_1"])

file = open("example.json", "w", encoding="utf-8")
json.dump(json_obj, file, ensure_ascii=False, indent=4)
file.close()
JSON = (json.dumps(json_obj, ensure_ascii=False)).replace(" ","")
print(JSON)
print(type(JSON))
json_object = json.loads(JSON)
print(json_object)
print(type(json_object))

import pickle
file = open("example_binary","wb")
pickle.dump(json_object, file,4)
file.close()
file = open("example_binary","rb")
binary_file = pickle.load(file)
print(binary_file)
file.close()


