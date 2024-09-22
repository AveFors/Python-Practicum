def main():
    n, m, k1, k2 = int(input()), int(input()), int(input()), int(input())
    a = (n * m - n * k2) // (k1 - k2)
    print(a, n - a)

if __name__ == '__main__':
    main()