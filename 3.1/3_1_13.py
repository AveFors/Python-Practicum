def main():
    a = [int(input()) for i in range(int(input()))]
    p = int(input())
    [print(x ** p) for x in a]


if __name__ == '__main__':
    main()
