# Функция describe_pet может вызываться в программе несколько 
# раз. Для вызова инфо о другом животном достаточно одного 
# вызова функции describe_pet().
# 
def describe_pet(animal_type, pet_name): 
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
