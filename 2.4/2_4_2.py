def main():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{j} * {i} = {i * j}', end='\n')


if __name__ == '__main__':
    main()