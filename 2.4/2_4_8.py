def main():
    n = int(input())
    a = {input(): input() for i in range(n)}
    res_summa = 0
    res = ''
    for i in a.items():
        summa = 0
        for k in i[1]:
            summa += int(k)
        if summa >= res_summa:
            res_summa = summa
            res = i[0]
    print(res)


if __name__ == '__main__':
    main()