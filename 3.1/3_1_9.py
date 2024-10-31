def main():
    while (n := input()):
        if n[0] == '#':
            continue
        elif '#' in n:
            print(n[:n.find('#')])
        else:
            print(n)


if __name__ == '__main__':
    main()
