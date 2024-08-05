def get_multiplied_digits(number):
    number = int(number)
    str_number = (str(number))
    first = int(str_number[0])
    if len(str_number) > 1:
        return first*get_multiplied_digits(int(str_number[1:]))
    return first

resuit = get_multiplied_digits('000040203')
print(resuit)