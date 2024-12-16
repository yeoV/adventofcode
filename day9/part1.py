import sys
from collections import deque
read = sys.stdin.readline

disk_map = list(map(int, read()))

def create_blocks(disk_map) -> list:
    flag = True
    idx = 0
    blocks = list()
    for disk in disk_map:
        if flag:    # file turn
            blocks.extend([idx] * disk)
            idx += 1
        else:
            blocks.extend(["."] * disk)
        flag = not flag # reverse

    return blocks


def compact_disk(blocks):
    for s_idx, val in enumerate(blocks):
        if val == ".":
            for e_idx in range(len(blocks)-1, 0, -1):
                if blocks[e_idx] != "." and s_idx < e_idx:
                    blocks[s_idx], blocks[e_idx] = blocks[e_idx], blocks[s_idx]
                    break

    return  blocks


def calc_checksum(disk):
    return sum(idx * val for idx, val in enumerate(disk) if val != ".")


blocks = create_blocks(disk_map)
disk = compact_disk(blocks)
print(calc_checksum(disk))
