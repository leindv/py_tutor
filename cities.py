# Цикл, который начинается с 1, будет выполнятся БЕСКОНЕЧНО - если
# только в нем не будет выполнена команда break. Здесь эта команда 
# выполняется при вводе пользователем строки 'quit'.
#
prompt = "\nPlease enter the name of city you have visited:"
prompt +="\n(Enter 'quit' when you are finished.) "

while True: #1
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I`d love to go to {city.title()}!")
