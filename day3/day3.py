import re

file = 'input_d3.txt'

with open(file) as f:
    instructions = f.read()

# print(instructions)
matches = re.findall('mul\((\d+){1,3},(\d+){1,3}\)', instructions)
result = sum([(int(x) * int(y)) for x, y in matches])

print(result)

# part 2
result = 0
flag = 1
mul_list = []

matches = re.findall('(mul\((?:\d+){1,3},(?:\d+){1,3}\))|(do(?:n\'t)?\(\))', instructions)
for match in matches:
    if len(match[0]):
        if flag:
            mul_list.append(match[0])
    else:
        if match[1] == 'don\'t()':
            flag = 0
        else:
            flag = 1

for instructions in mul_list:
    match = re.findall('mul\((\d+){1,3},(\d+){1,3}\)', instructions)
    result += sum([(int(x) * int(y)) for x, y in match])

print(result)
