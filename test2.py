def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Использование генератора
for number in count_up_to(5):
    print(number)
