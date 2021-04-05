# Обработка исключения FileNotFoundError.

# С применением блока try-except.



filename = 'alice.txt'
try:
    with open (filename, encoding = 'uef-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
