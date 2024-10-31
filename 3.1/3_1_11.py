def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    zapros = input()
    [print(x) for x in a if x.lower().count(zapros.lower()) > 0]


if __name__ == '__main__':
    main()
