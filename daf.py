calls = 0

def count_calls():
    global calls
    calls =+ 1

def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains (string, list_to_search):
        count_calls()
        for word in list_to_search:
            if string.lower() in word.lower() or word.lower() in string.lower():
                return True
        else:
             return False


print(string_info('Capybara'))
print(string_info("Armageddon"))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls * 4)