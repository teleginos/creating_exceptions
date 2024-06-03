from my_exception.exceptions import ProcessingException, InvalidDataException


def mathematical_operations(number_1, number_2, operation):
    if operation == '+':
        return int(number_1) + int(number_2)
    elif operation == '-':
        return int(number_1) - int(number_2)
    elif operation == '*':
        return int(number_1) * int(number_2)
    elif operation == '/':
        return int(number_1) / int(number_2)
    elif operation == '//':
        return int(number_1) // int(number_2)
    else:
        raise ProcessingException('Такой математической операции наша программа не знает',
                                  operator)


if __name__ == '__main__':
    try:
        num_1 = input('Введите первое число: ')
        operator = input('Введите математическую операцию: ')
        num_2 = input('Введите второе число: ')

        if num_1.isalpha() or num_2.isalpha():
            raise InvalidDataException('То что вы ввели не является числом',
                                       (num_1, num_2) if num_1.isalpha() and num_2.isalpha()
                                       else num_1 if num_1.isalpha() else num_2)

        result = mathematical_operations(num_1, num_2, operator)

    except (ProcessingException, InvalidDataException) as exc:
        print(f"\nПроизошла ошибка!\n{exc.message}: {exc.extra_info[0]}")
        result = None

    finally:
        if result:
            print(f'Результат операции {num_1} {operator} {num_2} = {result}')
        else:
            print('К сожалению из-за возникшей ошибки результат не был вычислен')
