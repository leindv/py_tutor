# В отличии от предыдущего коммита здесь первое значение 
# является истинным, поэтому остальные значения 
# не проверяются.
requested_toppings = ['mashrooms', 'extra cheese'] 
if 'mashrooms' in requested_toppings: 
    print("Adding mashrooms.")
elif 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")       
