from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if len(container) <= 1:
        return container

    max_elem = max(container) + 1
    temp = dict.fromkeys(range(max_elem), 0)  # создаем словарь для подсчета элементов
    for elem in container:
        temp[elem] += 1  # заполняем его
    container = []
    for key in temp.keys():  # заполняем отсортированный список
        if temp[key] != 0:
            for i in range(temp[key]):
                container.append(key)

    return container
