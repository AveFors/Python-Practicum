def main():
    a, b, c = int(input()), input(), int(input())
    if b.count(' ') > 0 and len(b) % 2 == 0:
        print(a + c)
    elif len(b) % 2 == 0 and b.count(' ') == 0:
        print(a - c)
    elif len(b) % 2 != 0 and b.count(' ') > 0:
        print(a * c)
    else:
        print(a // c)


if __name__ == '__main__':
    main()