from modules.search_by_index import search

BLOCK_SIZE = 10 ** 6
BLOCKS = 455
CDN = 'http://optimus-prime.surge.sh/split-zopfli/'


def get_prime(n):
    return search(n, BLOCKS, BLOCK_SIZE - 1, CDN)
