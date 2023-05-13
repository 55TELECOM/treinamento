

def method_z(value):
    print("Method Z")

    try:
        method_y(value)
    except TypeError as data:
        print('TypeError', data)


def method_y(value):
    print('Method Y')

    method_x(value)


def method_x(value):
    print("Method X")
    result = value / 29
    print('result: ', result)


if __name__ == '__main__':
    method_z('asd')

    print("Finalizou o processo")