def main():
    n = int(input())
    s = 0
    for i in range(n):
        a = input()
        if len(a) == 1:
            s += 1
        else:
            k = 0
            for j in range(len(a) // 2):
                if a[j] == a[len(a) - j - 1]:
                    k += 1
            if k == len(a) // 2:
                s += 1

    print(s)

if __name__ == '__main__':
    main()