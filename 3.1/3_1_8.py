def main():
    n = int(input())
    for i in range(n):
        if 'зайка' in (n := input()):
            print(n.find('зайка') + 1)
        else:
            print('Заек нет =(')


if __name__ == '__main__':
    main()
