# Оператор % сообщает остаток от деленияю Данная прога 
# проверяет четность или нечетность введенного числа.
#
number = input("Enter a number? and I will rell you if it is even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe nomber {number} is odd.")
