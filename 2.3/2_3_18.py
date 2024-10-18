def main():
    n = int(input())
    i = 2
    res = ''
    while n != 1:
        if n % i == 0:
            if len(res) == 0:
                res += f'{i}'
            else:
                res += f' * {i}'
            n //= i
            i = 1
        i += 1
    print(res)


if __name__ == '__main__':
    main()