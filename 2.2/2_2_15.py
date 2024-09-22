def main():
    a, b = input(), input()
    d = sorted(map(int, a + b))
    c, f = str(d.pop(-1)), str(d.pop(0))
    v = c + str(sum(d) % 10) + f
    print(v)



if __name__ == '__main__':
    main()


