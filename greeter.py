#  Использование функции в цикле WHILE.
#  Здесь имя и фамилия в цикле запрашивается отдельно.
def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированныое полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True: # Бесконечный цикл, который...
    print("\nPlease tell me your name:") #1
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break #...прерывается если условие ЛОЖНО

    l_name = input("Last neme: ")
    if l_name == 'q':
        break #... здесь аналогично...
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    