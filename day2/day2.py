def is_it_safe(report_levels):
    if len(report_levels) != len(set(report_levels)):
        return False
    if sorted(report_levels) != report_levels and sorted(report_levels, reverse=True) != report_levels:
        return False
    for level in range(len(report_levels) - 1):
        if abs(report_levels[level] - report_levels[level + 1]) > threshold:
            return False
    return True


file = "input_d2.txt"

safe = 0
threshold = 3
with open(file) as f:
    inp = f.read().strip().splitlines()

for report in inp:
    report_levels = [int(x) for x in report.split()]
    if is_it_safe(report_levels):
        safe += 1

print(safe)

# part 2
safe = 0

not_safe_list = []
for report in inp:
    report_levels = [int(x) for x in report.split()]
    if is_it_safe(report_levels):
        safe += 1
    else:
        not_safe_list.append(report)
failed = []
for report in not_safe_list:
    report_levels = [int(x) for x in report.split()]
    # check first-last remove
    if is_it_safe(report_levels[1:]):
        safe += 1
    elif is_it_safe(report_levels[:-1]):
        safe += 1

    else:
        for idx, level in enumerate(report_levels[1:-1], start=1):
            if abs(level - report_levels[idx + 1]) > threshold or level == report_levels[idx + 1] \
                    or not (report_levels[idx - 1] < level < report_levels[idx + 1] or report_levels[idx - 1] > level >
                            report_levels[idx + 1]):
                curr = report_levels.copy()
                del curr[idx]
                next = report_levels.copy()
                del next[idx]
                prev = report_levels.copy()
                del prev[idx]

                if is_it_safe(curr) or is_it_safe(prev) or is_it_safe(next):
                    safe += 1
                    break

print(safe)
