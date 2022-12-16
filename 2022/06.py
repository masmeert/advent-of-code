def find_marker(buffer, marker_size):
    for i in range(len(buffer) - marker_size):
        slice = buffer[i : i + marker_size]
        if len(set(slice)) == marker_size:
            return marker_size + i


if __name__ == "__main__":
    buffer = open("inputs/06.txt").read()
    print(find_marker(buffer, 4))
    print(find_marker(buffer, 14))
