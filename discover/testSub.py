from easyDemo.calculator import Count
import unittest


class TestSub(unittest.TestCase):
    def setUp(self):
        print('test cast start')

    def tearDown(self):
        print('test cast end')

    def test_sub(self):
        j = Count(1, 8)
        self.assertEqual(j.sub(), -7)

    def test_sub2(self):
        j = Count(12, 7)
        self.assertEqual(j.sub(), 5)


if __name__ == '__main__':
    unittest.main()
