def main():
    n = int(input())
    ncc = 0
    mx = 0
    for cc in range(2, 11):
        s = 0
        novn = n
        while novn > 0:
            s += novn % cc
            novn //= cc
        if s > mx:
            mx = s
            ncc = cc
    print(ncc)

if __name__ == '__main__':
    main()