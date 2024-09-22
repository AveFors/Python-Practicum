def main():
    a, b, c = int(input()), int(input()), int(input())
    minute = a * 60 + b + c
    hour = minute // 60 % 24
    minute2 = minute % 60
    print(f'{hour:0>2}:{minute2:0>2}')


if __name__ == '__main__':
    main()
