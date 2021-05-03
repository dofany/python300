# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
#
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75


def print_arithmetic_operation(x, y):
    print("{0} + {1} = {2}".format(x, y, x + y))
    print("{0} - {1} = {2}".format(x, y, x - y))
    print("{0} * {1} = {2}".format(x, y, x * y))
    print("{0} / {1} = {2}".format(x, y, x / y))


print_arithmetic_operation(3, 4)
