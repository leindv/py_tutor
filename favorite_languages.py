# В точке 1 значение, связанное с каждым именем, представляет 
# теперь список. При переборе словаря в точке 2 переменная с 
# именем languages применяется для хранения каждого значения из 
# словаря. В основном цикле (2) по элементам словаря другой цикл 
# (3) перебирает элементы списка любимых языков участников.
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    } #1
for name, languages in favorite_languages.items(): #2
    print(f"\n{name.title()}'s favorite langusges are:")
    for language in languages: #3
        print(f"\t{language.title()}")
