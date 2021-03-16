# Изменение списка в функции.
# В начале проги создается список моделей и пустой список, в 
# который каждая модель перемещается после печати.
# Пока в unprinted_designs остаются модели цикл while имитирует
# печать каждой модели: модель удаляется из конца списка и 
# сохраняется в current_design, а пользователь получает сообщение
# о том, что текущая модель была напечатана.Затем модель перемещается 
# в список напечатанных. После завершения цикла выводится список 
# напечатанных моделей.  
#

# Список моделей, которые надо напечатать.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Цикл последовательно печатает каждую модель до конца списка.
# после печати каждая модель перемещается в список completed_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Вывод всех готовых моделей.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
