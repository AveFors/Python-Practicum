def main():
    n = int(input())
    res = -1
    pr_hash = 0
    for i in range(n):
        blok = int(input())
        hah, r, m = blok % 256, (blok // 256) % 256, blok // 256 ** 2
        h_n = (37 * (r + m + pr_hash)) % 256
        if h_n != hah or hah >= 100:
            res = i
            break
        pr_hash = hah
    print(res)

if __name__ == '__main__':
    main()