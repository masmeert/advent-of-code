def get_input():
    history = open("inputs/07.txt").read().split("\n")
    sizes = {"/": 0}
    path = "/"
    for command in history:
        if command[0] == "$":
            if command[2:4] == "cd":
                if command[5:6] == "/":
                    path = "/"
                elif command[5:7] == "..":
                    path = path[0 : path.rfind("/")]
                else:
                    _dir = command[5:]
                    path = path + "/" + _dir
                    sizes.update({path: 0})
        elif command[0:3] != "dir":
            size = int(command[: command.find(" ")])
            _dir = path
            for _ in range(path.count("/")):
                sizes[_dir] += size
                _dir = _dir[: _dir.rfind("/")]

    return sizes


if __name__ == "__main__":
    sizes = get_input()
    p1 = 0
    p2 = float("inf")
    for _dir in sizes:
        if sizes[_dir] < 100000:
            p1 += sizes[_dir]
        if 30000000 - (70000000 - sizes["/"]) <= sizes[_dir]:
            if sizes[_dir] < p2:
                p2 = sizes[_dir]

    print(p1)
    print(p2)
