def main():
    print('YES' if (n := input()).lower() == n[::-1].lower() else 'NO')

if __name__ == '__main__':
    main()
