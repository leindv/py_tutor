# Работа с несколькими файлами.

# Переместим основной код проги из питоновского 
# файла предыдущего коммита в функцию с именем  
# count_words(). При этом комментарии в проге обновили (1).


def count_words(filename):
    """Подсчет приблизительного количества строк в файле.""" #1

    try:
        with open (filename, encoding = 'utf-8') as f:
           contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split() 
        num_words = len(words) 
        print(f"The file {filename} has about {num_words} words.") 
filename = 'alice1.txt'
count_words(filename)
