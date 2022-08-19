

lines = []
with open('link name.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        # print(line.strip())
        lines.append(line.strip())
print(lines)

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(time, name)
    # print(s[0][:5], s[0][5:], s[1:])
    # for line in s:
    #     s1 = line[:5]
    #     s2 = line[5：]
    # print(s[1:], s1, s2)
    # print(s[0])
    # print(s[1])
    # print(s[0:5])
    # print(s)

