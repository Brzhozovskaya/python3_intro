# extra_number.py
def total(init=5, *numbers, extra_number): 
    """
    Если некоторые ключевые параметры должны быть доступны только по ключу,
    а не как позиционные аргументы, их можно объявить после параметра со звёздочкой.

    Объявление параметров после параметра со звёздочкой даёт только ключевые аргументы.
    Если для таких аргументов не указано значение по умолчанию, и оно не передано при вызове,
    обращение к функции вызовет ошибку.

    """
    count = init 
    for number in numbers: 
        count += number 
    count += extra_number 
    return count

if __name__ == '__main__':
    print(total(10, 1, 2, 3, extra_number=50))
    # Вызовет ошибку, поскольку мы не указали значение 
    # аргумента по умолчанию для extra_number:
    # print(total(10, 1, 2, 3)) 

