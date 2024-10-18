def main():
    a = []
    n = int(input())
    m = int(input())
    b = []
    for i in range(n):
        a.append(int(input()))
    for i in range(len(a) - 1):
        if abs(a[i + 1] - a[i]) < m:
            b.append(a[i + 1])
    print(max(b))

if __name__ == '__main__':
    main()