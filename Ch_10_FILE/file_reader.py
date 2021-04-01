# Проверка дня рождения.

# В (1) прога запрашивает день рождения пользователя, 
# а затем в (2) проверяет вхождение этой строки в 
# pi_string.


filename = 'pi_million_digits.txt' 

with open(filename) as file_object:
    lines = file_object.readlines() 

pi_string = '' 
for line in lines: 
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ") #1
if birthday in pi_string: #2
    print("Your birthdey appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

    