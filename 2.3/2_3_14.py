def main():
    def prost(x):
        if x == 1:
            return 'NO'
        if x == 0:
            return 'NO'
        for i in range(2, int(x ** .5) + 1):
            if x % i == 0:
                return 'NO'
        return 'YES'

    print(prost(int(input())))


if __name__ == '__main__':
    main()