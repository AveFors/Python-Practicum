def main():
    def f(*kwargs):
        for i in range(len(kwargs[0]) - 1):
            a, b = kwargs[0][i], kwargs[0][i + 1]
            if a < b:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            kwargs[0][i + 1] = a
        return kwargs[0][-1]

    print(f(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
