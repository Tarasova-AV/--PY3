"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError('В последовательности отсутствуют элементы')
    min_elem = arr[0]
    min_index = 0
    for i, elem in enumerate(arr):
        if elem > min_elem:
            continue
        else:
            min_elem = elem
            min_index = i
    return min_index
