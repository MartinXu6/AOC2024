Input = [i.strip("\n").split() for i in open("input.txt", "r")]
total = 0


def check(lst):
    if int(lst[0]) > int(lst[1]):
        lst = lst[::-1]
    for element in range(1, len(lst)):
        if 1 <= int(lst[element]) - int(lst[element - 1]) <= 3:
            continue
        else:
            return False
    return True


for line in Input:
    if int(line[0]) > int(line[1]):
        line = line[::-1]
    for element in range(1, len(line)):
        if 1 <= int(line[element]) - int(line[element - 1]) <= 3:
            continue
        else:
            for i in range(len(line)):
                current = list(line)
                current.pop(i)
                if check(current):
                    break
            else:
                break
    else:
        total += 1
print(total)
