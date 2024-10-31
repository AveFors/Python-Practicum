def main():
    l, n = int(input()), int(input())
    a = [input() for i in range(n)]
    [print(f'{x[:l - 3]}...' if len(x) > l else x) for x in a]

if __name__ == '__main__':
    main()
