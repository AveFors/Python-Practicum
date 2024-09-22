def main():
    a, b, c = input(), input(), input()
    print((a if a < b else b) if (a if a < b else b) < c else c)



if __name__ == '__main__':
    main()


