import re

file = 'input_d3.txt'

with open(file) as f:
    instructions = f.read()

# print(instructions)
result = re.findall('mul\((\d+){1,3},(\d+){1,3}\)', instructions)
s = sum([(int(x) * int(y)) for x, y in result])

print(s)
