def main():
    Petya, Vanya, Tolya = int(input()), int(input()), int(input())
    if Vanya > Petya and Vanya > Tolya:
        print('Вася')
    elif Petya > Tolya:
        print('Петя')
    else:
        print('Толя')



if __name__ == '__main__':
    main()



