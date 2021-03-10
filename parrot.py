# В точке 1 определяется сообщение, которое объясняет, 
# что у пользователя есть два варианта: ввести сообщение 
# или ввести признак завершения (строка 'quit'). Затем в 
# переменной (2) присваивается введенное пользователем значение. 
# В проге эта переменная инициализируется пустой строкой " ". 
# Цикл будет выполнятся пока значение massage НЕ РАВНО 'quit'.
#
prompt = "\nTell me something, and I will repeat it back to you:" #1
prompt += "\nEnter 'quit' to end the program."

massage = "" #2
while massage != 'quit': #3
    massage = input(prompt)
    print(massage)
