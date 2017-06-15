import math
import gzip

from functools import reduce

import requests

# from modules.tools import time_it


# @time_it
def search(n, amount_blocks, block_size, cdn, path_files_blocks=None):
    block_size -= 1  # В блоке на одно число меньше

    total_numbers = amount_blocks * block_size

    if n > total_numbers:
        return None

    block_num = int(math.ceil(n / block_size))
    offset = n % block_size if n % block_size != 0 else block_size

    if path_files_blocks:
        with gzip.open('{}/{}.txt.gz'.format(path_files_blocks, block_num), 'rt') as f_block:
            numbers = [float(num) for num in f_block.readline().strip().split(' ')]
    else:
        response = requests.get('{}/{}.txt.gz'.format(cdn, block_num))

        if not response.status_code == 200:
            return None

        f_block = gzip.decompress(response.content)
        numbers = [float(num) for num in f_block.decode('utf-8').strip().split(' ')]

    return int(reduce(lambda previous, current: previous + current * 2, numbers[1:offset], numbers[0]))
