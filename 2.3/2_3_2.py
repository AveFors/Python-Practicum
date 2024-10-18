def main():
    a = []
    count = 0
    while (n := input()) != 'Приехали!':
        a.append(n)
    else:
        for i in a:
            count += i.count('зайка')
    print(count)


if __name__ == '__main__':
    main()