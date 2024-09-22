def main():
    a, b, c, d = input(), int(input()), int(input()), int(input())
    chek = 'Чек'
    print(f'{chek:=^35}')
    print('Товар:' + f'{a:>29}')
    print('Цена:' + f'{f'{c}кг * {b}руб/кг':>30}')
    print('Итого:' + f'{f'{b * c}руб':>29}')
    print('Внесено:' + f'{f'{d}руб':>27}')
    print('Сдача:' + f'{f'{d - b * c}руб':>29}')
    print('=' * 35)


if __name__ == '__main__':
    main()