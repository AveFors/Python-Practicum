def main():
    string = input()
    string_res = ''
    for i in string:
        if int(i) % 2 != 0:
            string_res += i
    print(string_res)


if __name__ == '__main__':
    main()