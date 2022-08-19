
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
    # new = []
    # new1 = []
    Neo_word_count = 0
    Neo_sticker_count = 0
    Neo_image_count = 0
    Queenie_word_count = 0
    Queenie_sticker_count = 0
    Queenie_image_count = 0
    # person = None
    for line in lines:
        s = line.strip().split(' ')
        # print(s)
        time = s[0]
        name = s[1]
        if name == 'Neo':
            if s[2] == '貼圖':
                Neo_sticker_count += 1
            elif s[2] == '圖片':
                Neo_image_count += 1
            else:
                for msg in s[2:]:
                    # new.append(msg)
                    Neo_word_count += len(msg)
        elif name == 'Queenie':
            if s[2] == '貼圖':
                Queenie_sticker_count += 1
            elif s[2] == '圖片':
                Queenie_image_count += 1
            else:
                for msg in s[2:]:
                    # new1.append(msg)
                    Queenie_word_count += len(msg)


    print('Neo說了', Neo_word_count, '個字')
    print('Neo傳了', Neo_sticker_count, '個貼圖')
    print('Neo傳了', Neo_image_count, '張圖片')
    print('Queenie說了', Queenie_word_count, '個字')
    print('Queenie傳了', Queenie_sticker_count, '個貼圖')
    print('Queenie傳了', Queenie_image_count, '張圖片')
    # print(len(new))
    # print(len(new1))
    # print(new)
    # return new


def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('[LINE]Queenie.txt')
    lines = convert(lines) # lines = []
    # write_file('output.txt', lines)


main()