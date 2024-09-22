def main():
    a, b, c = int(input()), int(input()), int(input())
    print('YES' if max(a, b, c) < min(a, b, c) + sum([a, b, c]) - (max(a, b, c) + min(a, b, c)) else 'NO')


if __name__ == '__main__':
    main()


