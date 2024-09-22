def main():
    a = int(input())
    sum1 = int(str(a)[1]) + int(str(a)[2])
    sum2 = int(str(a)[0]) + int(str(a)[1])
    print(str(max(sum1, sum2)) + str(min(sum1, sum2)))



if __name__ == '__main__':
    main()


