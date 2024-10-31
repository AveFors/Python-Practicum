def main():
    r = int(input())
    v = r

    def f(n, *kwargs):
        while n >= 0:
            for i in range(len(kwargs[0]) - 1):
                if n < 0:
                    break
                a, b = kwargs[0][i], kwargs[0][i + 1]
                if a < b:
                    a, b = b, a
                while b != 0:
                    a, b = b, a % b
                n -= 1
                kwargs[0][i + 1] = a
        return kwargs[0][-1]

    print(f(r, [int(input()) for i in range(v)]))


if __name__ == '__main__':
    main()