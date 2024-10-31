def main():
    text = ''
    while (s := input()) != 'ФИНИШ':
        text += s.lower()
    text = text.replace(' ', '')
    mx = 0
    mx2 = ''
    for i in text:
        count = text.count(i)
        if count > mx:
            mx = count
            mx2 = i
        elif count == mx:
            if i < mx2:
                mx2 = i

    print(mx2.lower())

if __name__ == '__main__':
    main()
