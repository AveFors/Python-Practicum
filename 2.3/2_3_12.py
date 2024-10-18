def main():
    numb = input()
    v = 0
    for i in numb:
        v = max(v, int(i))
    print(v)


if __name__ == '__main__':
    main()