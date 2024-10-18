def main():
    string = input()
    print('YES' if string == string[::-1] else "NO")


if __name__ == '__main__':
    main()