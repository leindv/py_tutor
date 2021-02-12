# Здесь f-строка (от слова "format"). Формирует строку, заменяя имена 
# переменных в фигурных скобках {} их значениями.
# Эти строки впервые появились в python 3.6
# Более ранних версиях вместо f используем метод format()
# Например, ful_mame = "{} {}".format(first_name, last_name)
# 
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
massage = f"Hello, {full_name.title()}!"
print(massage)
