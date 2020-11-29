# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль


def my_fun(**args):
    try:
        user_answer1 = int(input('Введите число 1 '))
        user_answer2 = int(input('Введите число 2 '))
        result = user_answer1 / user_answer2
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    return result

print(f'result  {my_fun()}')

