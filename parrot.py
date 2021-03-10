# Дополнили прогу из предыдущего коммита с целью не выводить 
# сообщение 'quit', если оно вводится пользователем. Решается 
# проверкой IF (1).
#
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "

massage = " " 
while massage != 'quit':
    massage = input(prompt)
    if massage != 'quit': #1
        print(massage)
