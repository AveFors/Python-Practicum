def main():
    a = []
    n = int(input())
    res = sum([1 for i in range(n) if input().count('зайка') > 0])
    print(res)


if __name__ == '__main__':
    main()