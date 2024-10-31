def main():
    def prost(x):
        if x == 1:
            return False
        for i in range(2, int(x ** .5) + 1):
            if x % i == 0:
                return False
        return True

    n = int(input())
    a = [int(input()) for i in range(n)]
    res = sum([1 for k in a if prost(k)])
    print(res)

if __name__ == '__main__':
    main()