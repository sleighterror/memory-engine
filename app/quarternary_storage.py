# quaternary_storage.py

import json

# DNA-inspired quaternary code: A=0, C=1, G=2, T=3
QUAT_MAP = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
REV_QUAT_MAP = {v: k for k, v in QUAT_MAP.items()}


def to_quaternary_string(data):
    """
    Encode a memory dict as a quaternary string.
    """
    json_str = json.dumps(data, sort_keys=True)
    binary = ''.join(f'{ord(c):08b}' for c in json_str)
    quats = [QUAT_MAP[int(binary[i:i+2], 2)] for i in range(0, len(binary), 2)]
    return ''.join(quats)


def from_quaternary_string(quat_str):
    """
    Decode a quaternary string into memory dict.
    """
    binary = ''.join(f'{REV_QUAT_MAP[c]:02b}' for c in quat_str)
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    json_str = ''.join(chars)
    return json.loads(json_str)


def save_memories_to_quat(memories, filepath="memory_quat.txt"):
    with open(filepath, "w") as f:
        for mem in memories:
            f.write(to_quaternary_string(mem) + "\n")


def load_memories_from_quat(filepath="memory_quat.txt"):
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    return [from_quaternary_string(line) for line in lines]
