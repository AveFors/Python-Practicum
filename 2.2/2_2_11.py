def main():
    a = input()
    a = sorted(list(map(int, a)))
    print('YES' if a[0] + a[-1] == a[1] * 2 else 'NO')


if __name__ == '__main__':
    main()


