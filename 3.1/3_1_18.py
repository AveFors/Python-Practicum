def main():
    s = input()
    a = []
    left = 0
    right = 0
    for r in range(1, len(s)):
        if s[r] == s[r - 1]:
            right = r
        else:
            a.append(s[left:right + 1])
            left = r
            right = r
    a.append(s[left:right + 1])
    for i in a:
        print(i[0], len(i))


if __name__ == '__main__':
    main()
