def main():
    n = int(input())
    v = 3
    player = 1
    while n > 0:
        for i in range(v, 0, -1):
            print(f'До старта {i} секунд(ы)')
        print(f'Старт {player}!!!')
        v += 1
        n -= 1
        player += 1


if __name__ == '__main__':
    main()