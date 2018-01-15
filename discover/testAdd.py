from easyDemo.calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test cast start')

    def tearDown(self):
        print('test cast end')

    def test_add(self):
        j = Count(1, 8)
        self.assertEqual(j.add(), 9)

    def test_add2(self):
        j = Count(3, 7)
        self.assertEqual(j.add(), 10)


if __name__ == '__main__':
    unittest.main()
