Input = [i.strip("\n").split() for i in open("input.txt", "r")]
lst1 = []
lst2 = []
for i in Input:
    lst1.append(int(i[0]))
    lst2.append(int(i[1]))
#part 1
# print(sum([abs(sorted(lst2)[i] - sorted(lst1)[i]) for i in range(len(Input))]))

# part 2
total = 0
for x in lst1:
    total += x*lst2.count(x)
print(total)