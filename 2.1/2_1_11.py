def main():
    a = int(input())
    print(f'{a // 100 % 10}{a // 1000}{a % 10}{a // 10 % 10}')

if __name__ == '__main__':
    main()