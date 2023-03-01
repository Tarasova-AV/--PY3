def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if not brackets_row:
        return True
    if brackets_row.count('(') != brackets_row.count(')'):
        return False
    a, b = 0, 0
    for _ in range(brackets_row.count(')')):
        a = brackets_row.find('(', a)
        b = brackets_row.find(')', b)
        if a > b:
            return False
        a += 1
        b += 1

    return True



if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
