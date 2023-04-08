""" Фукції"""
def describe_pet (pet_name, animal_type='dog'):
    print(f'{pet_name.title()} is a {animal_type}')
describe_pet()

def get_formated_name(first_name, last_name, midle_name=''):
    """Повернемо відформатоване значення"""
    if midle_name:
        full_name = f"{first_name} {last_name} {midle_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('viktor', 'khruschc')
print(musician)