from collections import deque
from utils import aoc


def read_input():
    diskmap = aoc.get_input("09", None)
    disk, current_val = [], 0
    for i, block_size in enumerate(map(int, diskmap)):
        disk.extend([current_val] * block_size if i % 2 == 0 else [-1] * block_size)
        if i % 2 == 0:
            current_val += 1
    return disk


def get_checksum(disk):
    free_space = deque(i for i, v in enumerate(disk) if v == -1)
    updated_disk = disk[:]
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != -1 and free_space and free_space[0] < i:
            empty_index = free_space.popleft()
            updated_disk[empty_index], updated_disk[i] = updated_disk[i], -1
    return sum(i * n for i, n in enumerate(updated_disk) if n != -1)


def find_fragments(disk):
    occupied, empty = [], []
    start = 0
    for i in range(1, len(disk)):
        if disk[i] != disk[start]:
            (empty if disk[start] == -1 else occupied).append([start, i - 1])
            start = i
    if disk[start] != -1:
        occupied.append([start, len(disk) - 1])
    return occupied, empty


def defragment(disk):
    defragmented = disk[:]
    occupied, empty = find_fragments(disk)
    for start, end in occupied[::-1]:
        block_size = end - start + 1
        for empty_block in empty:
            empty_start, empty_end = empty_block
            if empty_start > start:
                break
            if empty_end - empty_start + 1 >= block_size:
                (
                    defragmented[empty_start : empty_start + block_size],
                    defragmented[start : start + block_size],
                ) = (disk[start : start + block_size], [-1] * block_size)
                empty_block[0] += block_size
                if empty_block[0] > empty_block[1]:
                    empty.remove(empty_block)
                break
    return sum(i * n for i, n in enumerate(defragmented) if n != -1)


if __name__ == "__main__":
    diskmap = read_input()
    print(get_checksum(diskmap))
    print(defragment(diskmap))
