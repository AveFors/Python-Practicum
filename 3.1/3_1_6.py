def main():
    n = int(input())
    count = 0
    for i in range(n):
        count += input().count('зайка')
    print(count)

if __name__ == '__main__':
    main()
