def main():
    length = int(input())
    newline = '\n'
    header = ''
    newlines = []
    for _ in range(stings_number := int(input())):
        header += input() + newline
    header.strip('\n')
    for pos in range(len(header)):
        if header[pos] == newline:
            newlines.append(pos)
    header = header.replace(newline, "")
    if len(header) > length:
        header = header[:length - 3] + '...'
    for pos in newlines:
        if (header[-3:] != '...') or (length - pos >= 4):
            header = header[:pos] + newline + header[pos:]
            length += 1
    print(header)


if __name__ == '__main__':
    main()
