from calculator import Count
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        print('test add start')

    def tearDown(self):
        print('test add end')


class TestAdd(MyTest):
    def test_add(self):
        j = Count(2, 5)
        self.assertEqual(j.add(), 7)

    def test_add2(self):
        j = Count(12, 55)
        self.assertEqual(j.add(), 67)


class TestSub(MyTest):
    def test_sub(self):
        j = Count(2, 5)
        self.assertEqual(j.sub(), -3)

    def test_sub2(self):
        j = Count(12, 55)
        self.assertEqual(j.sub(), -43)


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('test_add'))
    suite.addTest(TestAdd('test_add2'))
    suite.addTest(TestSub('test_sub'))
    suite.addTest(TestSub('test_sub2'))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
