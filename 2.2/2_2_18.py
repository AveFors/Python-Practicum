def main():
    a, b, c = int(input()), int(input()), int(input())
    treug = sorted([a, b, c])
    if treug[-1] ** 2 == treug[0] ** 2 + treug[1] ** 2:
        print('100%')
    elif treug[-1] ** 2 < treug[0] ** 2 + treug[1] ** 2:
        print('крайне мала')
    elif treug[-1] ** 2 > treug[0] ** 2 + treug[1] ** 2:
        print('велика')



if __name__ == '__main__':
    main()


