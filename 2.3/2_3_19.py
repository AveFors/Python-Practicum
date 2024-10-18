def main():
    n = 500
    chislo = n // 2
    print(n)
    while (k := input()) != 'Угадал!':
        if k == 'Меньше':
            n -= chislo
        if k == 'Больше':
            n += chislo
        if chislo >= 2:
            chislo = (chislo) // 2
        print(n)


if __name__ == '__main__':
    main()