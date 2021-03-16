# ИЗМЕНЕНИЕ СПИСКА В ФУНКЦИИ.
# Меняем структуру кода от предыдущего коммита.  
# В точке (1) опеделяется функция с двумя папаметрами, она 
# имитирует печать каждой модели, последовательноизвлекая 
# модели из первого списка и перемещая их во второй список.
# В точке (2) определяется функция с одним параметром - 
# список напечатанных моделей Эта функция получает этот 
# список и выводит имена всех напечатанных моделей.
# Программа создает список моделей для печати и пустой список 
# для готовых моделей(3). Затем, так как обе функции определены,
# остается ВЫЗВАТЬ их и передать правильные АРГУМЕНТЫ (4).

def print_models(unprinted_designs, completed_models): #1
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models): #2
    """Выводи инфо о всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] #3
completed_models = []

print_models(unprinted_designs, completed_models) #4
show_completed_models(completed_models)
