import os
import shutil
from unittest import TestCase, main as unit_tests

from modules.blocks import generate_blocks, split

BASE_DIR = os.path.dirname(__file__)
TMP_DIR = os.path.join(BASE_DIR, 'fixtures/tmp')


class TestBlocks(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.primes_file = os.path.join(BASE_DIR, 'fixtures/100_primes.txt')
        cls.primes_in_line = 10
        cls.blocks_file = '{}/blocks.txt'.format(TMP_DIR)
        cls.block_size = 10
        cls.blocks_in_file = 1
        cls.split_blocks_path = os.path.join(BASE_DIR, TMP_DIR, 'split')

    def test_generator(self):
        generate_blocks(self.primes_file, self.blocks_file, self.block_size, self.primes_in_line)

        template = [
            '2 0.5 1 1 2 1 2 1 2',
            '29 1 3 2 1 2 3 3 1',
            '67 2 1 3 2 3 4 2 1',
            '107 1 2 7 2 3 1 5 1',
            '157 3 2 3 3 1 5 1 2',
            '199 6 6 2 1 2 3 1 5',
            '257 3 3 1 3 2 1 5 7',
            '311 1 2 7 3 5 1 2 3',
            '367 3 3 2 3 4 2 4 5',
            '421 5 1 3 2 3 4 2 1',
            '467 6 4 2 4 2 3 6 1'
        ]

        with open(self.blocks_file) as f_blocks:
            counter = 0

            for line in f_blocks:
                line = line.strip()

                with self.subTest(line=line):
                    self.assertEqual(line, template[counter])
                counter += 1

        self.assertEqual(counter, len(template))

    def test_split(self):
        split(self.blocks_file, self.blocks_in_file, self.block_size, self.split_blocks_path)

        self.assertEqual(len(os.listdir(self.split_blocks_path)), 11)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TMP_DIR)


if __name__ == '__main__':
    unit_tests()
