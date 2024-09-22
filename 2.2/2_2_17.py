def main():
    a, b, c = float(input()), float(input()), float(input())
    d = (b ** 2) - (4 * a * c)
    if a == 0 and b == 0 and c == 0:
        print('Infinite solutions')
    elif a == 0 and b != 0 and c != 0:
        x = -(c / b)
        print(f'{x:.2f}')
    elif a == 0 and c == 0:
        x = 0
        print(f'{x:.2f}')
    elif a == 0 and b == 0:
        print('No solution')
    else:
        if d < 0:
            print('No solution')
        elif d == 0:
            x = (-b) / (2 * a)
            print(f'{x:.2f}')
        elif d > 0:
            x1 = (-b - (d ** 0.5)) / (2 * a)
            x2 = (-b + (d ** 0.5)) / (2 * a)
            print(f'{min(x1, x2):.2f}', f'{max(x1, x2):.2f}')


if __name__ == '__main__':
    main()
