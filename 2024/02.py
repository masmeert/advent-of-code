from utils import aoc

def is_safe(report: list[int]) -> bool:
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return (all(d > 0 for d in differences) or all(d < 0 for d in differences)) and (all(1 <= abs(d) <= 3 for d in differences))

def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe(report): 
        return True
    for i in range(len(report)):
        modified = report[:i] + report[i+1:]
        if is_safe(modified): 
            return True
    return False

if __name__ == "__main__":
    input = aoc.get_input("02")
    reports = [list(map(int, report.split())) for report in input]
    print(sum(map(is_safe, reports)))
    print(sum(map(is_safe_with_dampener, reports)))

