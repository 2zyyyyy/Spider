import unittest


class Test(unittest.TestCase):

    def setUp(self):
        number = input('输入一个整数')
        self.number = int(number)

    def test_case(self):
        self.assertNotEqual(self.number, 10, msg='输入的数字不等于10!')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()