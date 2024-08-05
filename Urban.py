def print_params(a=1, b='Storka', c=True):
    print(a, b, c)


print_params(b=25)
#print_paramsc = (c = [1,2,3]) Так поменять не получиться

values_list = [58, 'ctr', False]
values_dict = {'a': 1, 'b': 'Stroka', 'c': True}
valuea_list_2 = [54.32, 'stroka']
print_params(*valuea_list_2, 42)

print_params(*values_list)
print_params(**values_dict)