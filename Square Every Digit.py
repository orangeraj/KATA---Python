def square_digits(num):
    op = ''
    num = str(num)
    for i in num:
        op += str(int(i)*int(i))
    return op


print(square_digits(765))