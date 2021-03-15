# ИМЕННОВАННЫЕ АРГУМЕНТЫ состоят из имени параметров и 
# их значений, передаваемых функции. 
# В отличии от ПОЗИЦИОННЫХ аргументов порядок следования 
# ИМЕННОВАНЫХ АРГУМЕНТОВ не важен (1).
def describe_pet(animal_type, pet_name): 
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster') #1
