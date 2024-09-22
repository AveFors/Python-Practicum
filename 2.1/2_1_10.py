def main():
    a, b = input(), int(input())
    print(f'Группа №{b // 100}.')
    print(f'{b % 10}. {a}.')
    print(f'Шкафчик: {b}.')
    print(f'Кроватка: {b // 10 % 10}.')


if __name__ == '__main__':
    main()