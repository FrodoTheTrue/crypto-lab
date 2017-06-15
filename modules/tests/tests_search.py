import os
import gzip
from unittest import TestCase, mock, main as unit_tests

from modules.search_by_index import search
from main import CDN

BASE_DIR = os.path.dirname(__file__)


def mocked_requests_get(url):
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

        def content(self):  # pylint: disable=E0202
            return self.content

    if url == '{}/1.txt.gz'.format(CDN):
        return MockResponse(gzip.compress(b'2 0.5 1 1 2 1 2 1 2'), 200)
    elif url == '{}/11.txt.gz'.format(CDN):
        return MockResponse(gzip.compress(b'467 6 4 2 4 2 3 6 1'), 200)

    return MockResponse(None, 404)


class TestBlocks(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.block_size = 10
        cls.blocks = 11

    @mock.patch('requests.get', mock.Mock(side_effect=mocked_requests_get))
    def test_search(self):
        number = search(7, self.blocks, self.block_size, CDN)
        self.assertEqual(number, 17)

        number = search(99, self.blocks, self.block_size, CDN)
        self.assertEqual(number, 523)

        number = search(100, self.blocks, self.block_size, CDN)  # Нет такого блока в наличии
        self.assertIsNone(number)

        number = search(1, self.blocks, self.block_size, 'lol')  # Ответ не 200
        self.assertIsNone(number)


if __name__ == '__main__':
    unit_tests()
