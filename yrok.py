def build_person (first_name, last_name, age=None):
    """Slovnuk z info pro ludiny"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musicial = build_person('jimi', 'helpix', age=27)
print(musicial)

def get_formated_name(first_name, last_name):
    """Po vernem vidformatovane imja"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()
while True:
    print('\nPlease tell you name:')
    print('q - to quit')

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    fomated_name = get_formated_name(f_name, l_name)
    print(f'\nHello {fomated_name}')
