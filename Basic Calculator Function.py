try:
    n1 = float(input('First Value: '))
    op = input('(+, -, *, /, //, %, **)\nOperator:  ')
    n2 = float(input('n2: '))

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '//':
        print(n1 // n2)
    elif op == '%':
        print(n1 % n2)
    elif op == '**':
        print(n1 ** n2)
    else:
        print('Invalid Operator')

except TypeError:
    print('Unsupported Type!')
except ValueError:
    print('Invalid Value!')
except OverflowError:
    print('Result is too large!')
except ZeroDivisionError:
    print('Math Error!')
