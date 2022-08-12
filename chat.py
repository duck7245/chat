
# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf8') as f:
    # with open('input.txt', 'r', encoding = 'utf8-sig') as f:
                                            # 如果遇到讀取時出現前面有怪編碼,需要加'-sig'
        for line in f:
            # line = line.strip()
            # lines.append(line)
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    # person = 'Temp'
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        # if person != 'Temp':
        if person: # 如果person有值的話
            new.append(person + ': ' + line)
        else:
            new.append(': ' + line)

    print(new)
    return new


def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines) # lines = []
    write_file('output.txt', lines)


main()