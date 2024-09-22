def main():
    a, d, c = input(), input(), input()
    b = []
    for i in a, d, c:
        if 'зайка' in i:
            b.append(i)
    if len(b) == 1:
        print(b[0], len(b[0]))
    elif len(b) == 2:
        if b[0] < b[1]:
            print(b[0], len(b[0]))
        else:
            print(b[1], len(b[1]))
    elif len(b) == 3:
        if b[0] < b[1] and b[0] < b[2]:
            print(b[0], len(b[0]))
        elif b[1] < b[0] and b[1] < b[2]:
            print(b[1], len(b[1]))
        else:
            print(b[2], len(b[2]))



if __name__ == '__main__':
    main()


