def main():
    a = input()
    a = list(map(int, a))
    a1 = str(max(a)) + str(sum(a) - max(a) - min(a))
    a2 = (str(min(a)) if 0 not in a else str(sum(a) - max(a) - min(a))) + \
         (str(sum(a) - max(a) - min(a)) if 0 not in a else str(min(a)))
    print(a2, a1)



if __name__ == '__main__':
    main()


