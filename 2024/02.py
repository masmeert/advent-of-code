from utils import aoc

def is_safe(report: list[int]) -> bool:
    differences = [b - a for a, b in zip(report, report[1:])]
    return (all(d > 0 for d in differences) or 
            all(d < 0 for d in differences)) and\
            all(1 <= abs(d) <= 3 for d in differences)

def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe(report): 
        return True
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

if __name__ == "__main__":
    input = aoc.get_input("02")
    reports = [list(map(int, report.split())) for report in input]
    print(sum(map(is_safe, reports)))
    print(sum(map(is_safe_with_dampener, reports)))

