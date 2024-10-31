def main():
    alf = ['а', 'б', 'в']
    for i in range(int(input())):
        if input()[0].lower() not in alf:
            print('NO')
            break
    else:
        print('YES')


if __name__ == '__main__':
    main()
