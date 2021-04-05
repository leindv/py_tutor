# Ошибки без уведомления пользователя.

# Если в предыдущем коммите мы сообщили пользователю, 
# что три файла недоступны, то обычно  обязанность сообщать 
# пользователю об ошибках не обязательно. 
# Прога при возниконовении исключения должна просто 
# проигнорировать сбой и продолжать работу.
# Для этого блок try пишется так же как обычно, но в блоке 
# except включаем команду pass, с которой блок ничего не 
# делает (1).
# В этом случае прога не выдает данных трассировки и 
# вообще никаких результатов, указывающих на возникновение 
# ошибки.

def count_words(filename):
    """Подсчет приблизительного количества строк в файле.""" 

    try:
        with open (filename, encoding = 'utf-8') as f:
           contents = f.read()
    except FileNotFoundError:
        pass #1
    else:
        words = contents.split() 
        num_words = len(words) 
        print(f"The file {filename} has about {num_words} words.") 
filenames = ['alice1.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

