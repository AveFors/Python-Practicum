def main():
    a = []
    summa = 0
    while (n := float(input())) != 0:
        a.append(n)
    else:
        for i in range(len(a)):
            if a[i] >= 500:
                summa += a[i] * 0.9
            else:
                summa += a[i]
    print(summa)


if __name__ == '__main__':
    main()