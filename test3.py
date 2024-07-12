def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Вывод: 1
#print(next(gen))  # Вывод: 2
#print(next(gen))  # Вывод: 3
