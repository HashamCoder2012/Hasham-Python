my_dict = {}
my_dict = {1: 'apple', 2: 'ball'}
my_dict = {'name': 'John', 1: [2, 4, 3]}
my_dict = {'name': 'Roman', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 69
print(my_dict)
my_dict['address'] = 'Rawalpindi'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print("Address :", my_dict.get('address'))
my_dict.clear()
print(my_dict)