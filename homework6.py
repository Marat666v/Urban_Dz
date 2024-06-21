my_dict = {"Marat": 2008, 'Nurgiza': 2007, 'Luffy': 1999}
print(my_dict)
print(my_dict['Nurgiza'])
print(my_dict.get('Karina'))
del my_dict['Luffy']
print(my_dict)

my_set = {6, 'Luffy', 3.14, 6}
list_ = [2, 2, 2, 5, 6, 7, 5]
list_ = set(list_)
print(list_.discard(1))
print(my_set)