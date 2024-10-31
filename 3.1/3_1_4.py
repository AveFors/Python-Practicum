def main():
    while (n := input()):
        if '@@@' in n[-3:]:
            continue
        elif '##' in n[:2]:
            print(n[2:])
        else:
            print(n if n != ' ' else ...)


if __name__ == '__main__':
    main()
