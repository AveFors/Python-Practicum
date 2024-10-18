def main():
    a, b, c = int(input()), int(input()), int(input())
    print(f'({a} ^ {b}) mod ({a} + {c}) = {(a ** b) % (a + c)}')


if __name__ == '__main__':
    main()