""" Фукції"""
def get_formated_name(first_name, last_name, midle_name=''):
    """Повернемо відформатоване значення"""
    if midle_name:
        full_name = f"{first_name} {last_name} {midle_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formated_name('viktor', 'khruschc')
print(musician)

def build_person(first_name, last_name, age=None):
    """Повернути словник з інфо за людину"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('viktor', 'khruschc', age='31')
print(musician)

def get_formatted_name(first_name, last_name):
    """Повернемо відформатоване імя"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()
#tse neskin4ennuj cukl
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")
