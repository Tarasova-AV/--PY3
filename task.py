from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    count_paths = [[0] * m for _ in range(n)]

    count_paths[0][0] = 1

    for i in range(1, n):
        count_paths[i][0] += count_paths[i - 1][0]
    for j in range(1, m):
        count_paths[0][j] += count_paths[0][j - 1]

    for i in range(1, n):
        for j in range(1, m):
            count_paths[i][j] += (count_paths[i - 1][j] + count_paths[i][j - 1] + count_paths[i - 1][j - 1])

    return count_paths


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
