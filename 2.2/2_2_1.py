def main():
    a = input('Как Вас зовут?\n')
    print(f'Здравствуйте, {a}!')
    b = input('Как дела?\n')
    match b:
        case 'плохо' | 'Плохо':
            print('Всё наладится!')
        case 'хорошо' | 'Хорошо':
            print('Я за вас рада!')
        case _:
            print('Отлично')


if __name__ == '__main__':
    main()


