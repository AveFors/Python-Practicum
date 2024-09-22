def main():
    name, price, weight, money = input(), int(input()), int(input()), int(input())
    print('Чек')
    print(f'{name} - {weight}кг - {price}руб/кг')
    print(f'Итого: {(price * weight)}руб')
    print(f'Внесено: {money}руб')
    print(f'Сдача: {(money - price * weight)}руб')

if __name__ == '__main__':
    main()