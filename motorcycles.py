# Удаление элементов по значению методом remove()
# с выводом причин удаления (Здесь применяется f-строка)
# После определения списка в точке 1, значение элемента списка сох-
# раняется в точке 2. Затем эта переменная сообщает Python,какое 
# значение должно быть удалено из списка (3). 
# В точке 4 значение элемента было удалено из списка,
# но продолжает храниться в переменной  too_expensive.
motorcycles = ['honda', 'yamaha', 'suzuki', 'dukati'] #1
print(motorcycles)
too_expensive = 'dukati' #2
motorcycles.remove(too_expensive) #3
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.") #4
