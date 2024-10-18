def main():
    x, y = 0, 0
    while (n := input()) != 'СТОП':
        v = int(input())
        if n == 'СЕВЕР':
            y += v
        if n == 'ЮГ':
            y -= v
        if n == 'ВОСТОК':
            x += v
        if n == 'ЗАПАД':
            x -= v
    print(y, x, sep='\n')


if __name__ == '__main__':
    main()