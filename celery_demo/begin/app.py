from begin.tasks import add

if __name__ == '__main__':
    print('begin')
    # add.delay()
    result = add.delay(1, 2)
    # result = add.apply_async(1, 2)

    print('end')
    print(result)
