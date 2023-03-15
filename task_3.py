def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Число должно быть типа int")
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    if n == 0:
        return 1
    return factorial_recursive(n-1) * n
