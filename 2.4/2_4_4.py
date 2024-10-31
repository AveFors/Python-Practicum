def main():
    n = int(input())
    summa = 0
    for i in range(n):
        k = input()
        for j in range(len(k)):
            summa += int(k[j])
    print(summa)


if __name__ == '__main__':
    main()