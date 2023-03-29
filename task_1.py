from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    flag = True
    counter = 0
    len_ = len(container) - 1
    for _ in container:
        if flag:
            counter = 0  # обнуляем счетчик
            for i in range(len_):
                if container[i] > container[i + 1]:
                    container[i], container[i + 1] = container[i + 1], container[i]
                    counter += 1  # считаем изменения
            if counter == 0:
                flag = False  # если не было перестановок - меняем значение "флага"
            len_ -= 1  # уменьшаем количество сортируемых элементов
        else:
            break

    return container
