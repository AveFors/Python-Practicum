def main():
    def f(a, b):
        if a > b:
            a, b = b, a
        while a != 0:
            a, b = b % a, a
        return b

    a, b = int(input()), int(input())
    print(f(a, b))


if __name__ == '__main__':
    main()