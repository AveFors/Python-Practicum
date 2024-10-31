def main():
    n = int(input())
    k = 0
    mxs = ''
    for i in range(n):
        s = ''
        for j in range(i):
            k += 1
            if k > n:
                break
            s += str(k) + ' '
        if len(s) > len(mxs):
            mxs = s

    tch = 0

    for i in range(1, n + 1):
        r = ''
        for j in range(i):
            tch += 1
            if tch > n:
                break
            r += str(tch) + ' '
        print(f'{r:^{len(mxs)}}')

if __name__ == '__main__':
    main()