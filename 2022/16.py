import re


def get_input():
    global flows, non_null, distances
    with open("inputs/16.txt") as f:
        lines = [re.split("[\\s=;,]+", line) for line in f.read().splitlines()]
    valves = {x[1]: set(x[10:]) for x in lines}
    flows = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
    non_null = {x: 1 << i for i, x in enumerate(flows)}
    distances = floyd_warshall(valves)


def floyd_warshall(valves):
    distances = {
        x: {y: 1 if y in valves[x] else float("+inf") for y in valves} for x in valves
    }

    for k in distances:
        for i in distances:
            for j in distances:
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )

    return distances


def visit(valve, budget, state, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)
    for other in flows:
        newbudget = budget - distances[valve][other] - 1
        if non_null[other] & state or newbudget <= 0:
            continue
        visit(
            other,
            newbudget,
            state | non_null[other],
            flow + newbudget * flows[other],
            answer,
        )
    return answer


if __name__ == "__main__":
    get_input()
    p1 = max(visit("AA", 30, 0, 0, {}).values())
    visited = visit("AA", 26, 0, 0, {})
    p2 = max(
        v1 + v2
        for k1, v1 in visited.items()
        for k2, v2 in visited.items()
        if not k1 & k2
    )
    print(p1, p2)
