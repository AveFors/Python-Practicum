def main():
    p, v, t = int(input()), int(input()), int(input())
    mx, mn = max(p, v, t), min(p, v, t)
    m = p + v + t - mx - mn
    if mx == p:
        if mn == t:
            m1, m2, m3 = 'Петя', 'Вася', 'Толя'
        else:
            m1, m2, m3 = 'Петя', 'Толя', 'Вася'
    elif mx == v:
        if mn == t:
            m1, m2, m3 = 'Вася', 'Петя', 'Толя'
        else:
            m1, m2, m3 = 'Вася', 'Толя', 'Петя'
    elif mx == t:
        if mn == v:
            m1, m2, m3 = 'Толя', 'Петя', 'Вася'
        else:
            m1, m2, m3 = 'Толя', 'Вася', 'Петя'
    print(f'{m1: ^24}')
    print(f'  {m2: <22}')
    print(f'{m3: >22}  ')
    print('   II      I      III   ')


if __name__ == '__main__':
    main()
