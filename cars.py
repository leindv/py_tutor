# Метод sorted() применяется для 
# сохранения исходного порядка элементов списка,
# но временного предсавления его в отсортированном 
# виде.
# Сначала список отобразиться в исходном (1) порядке,
# затем он отсортируется в алфавитном (2) и вернется в 
# исходное (3) состояние
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") #1
print(cars)
print("\nHere is the sorted list:") #2
print(sorted(cars))
print("\nHere is the original list againe:") #3
print(cars)
