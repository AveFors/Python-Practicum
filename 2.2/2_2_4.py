def main():
    p, v, t = int(input()), int(input()), int(input())
    if p > t and p > v and t < v:
        print('1. Петя', '2. Вася', '3. Толя', sep='\n')
    elif p > t and p > v and t > v:
        print('1. Петя', '2. Толя', '3. Вася', sep='\n')
    elif p < t and p < v and t > v:
        print('1. Толя', '2. Вася', '3. Петя', sep='\n')
    elif p < t and p > v and t > v:
        print('1. Толя', '2. Петя', '3. Вася', sep='\n')
    elif v > t and p < t and v > p:
        print('1. Вася', '2. Толя', '3. Петя', sep='\n')
    else:
        print('1. Вася', '2. Петя', '3. Толя', sep='\n')


if __name__ == '__main__':
    main()
