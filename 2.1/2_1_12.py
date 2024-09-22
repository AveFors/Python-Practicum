def main():
    a, b = int(input()), int(input())
    print(f'{(a // 100 + b // 100) % 10}{(a // 10 % 10 + b // 10 % 10) % 10}{(a % 10 + b % 10) % 10}')


if __name__ == '__main__':
    main()