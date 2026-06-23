import math


def humanbytes(size):

    if not size:
        return "0 B"

    power = 1024
    n = 0
    dic_powerN = {
        0: 'B',
        1: 'KB',
        2: 'MB',
        3: 'GB',
        4: 'TB'
    }

    while size > power:
        size /= power
        n += 1

    return f"{round(size,2)} {dic_powerN[n]}"
