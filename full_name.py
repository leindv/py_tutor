# Здесь f-строка (от слова "format"). Формирует строку, заменяя имена 
# переменных в фигурных скобках {} их значениями.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
