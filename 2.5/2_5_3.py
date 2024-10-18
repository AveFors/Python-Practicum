def main():
    nach, kon, shag = int(input()), int(input()), int(input())
    for i in range(nach, kon + 1, shag):
        print(f'{i} -', end=' ')
    for i in range(kon, nach - 1, -shag):
        print(f'{i} -' if i != nach else i, end=' ')


if __name__ == '__main__':
    main()