def main():
    n = int(input())
    name1 = input()
    i = 1
    while i != n:
        name2 = input()
        if name1 > name2:
            name1 = name2
        i += 1
    print(name1)


if __name__ == '__main__':
    main()