# Программа выполняет цикл , который считает 
# от 1 до 10, но выводит только нечетные числа в 
# этом диапазоне. сначала переменной current_number 
# присваевается 0. Так какзначение меньше 10 прога 
# входит в цикл while. При входе в цикл счетчик 
# увеличивается на1 в (1), поэтому current_number 
# принимает значение 1. Затем команда IF проверяет 
# остаток от деления на 2 и если он равен 0, то команда 
# continue приказывает ПРОИГНОРИРОВАТЬ оставшийся код цикла 
# и  вернуться к началу, если счетчик не делиться на 2, то 
# оставшаяся чачть цикла выполняется и прога выводит 
# текущее значение.
# То есть команда continue возвращает к началу цикла и проверке 
# условимий.
#  
current_number = 0 
while current_number < 10: 
    current_number += 1 #1
    if current_number % 2 == 0:
        continue

    print(current_number) 
   