def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Число должно быть типа int")
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    if n == 0:
        return 1
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
