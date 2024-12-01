file = "input_d1.txt"
list1 = []
list2 = []
total = 0

with open(file) as f:
    input = f.read().splitlines()
    for line in input:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

list1_ordered = sorted(list1)
list2_ordered = sorted(list2)
for i in range(len(list1_ordered)):
    total += abs(list1_ordered[i] - list2_ordered[i])

print(total)

# part2
total2 = 0
num_times = {}
for num in list1:
    if num not in num_times:
        count = 0
        for num2 in list2:
            if num == num2:
                count += 1
        num_times[num] = count
    total2 += num * num_times[num]

print(total2)
