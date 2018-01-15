# 用于知执行所有用例的文件
import unittest
# 加载测试文件
import testAdd
import testSub

# 构造测试集
# suite = unittest.TestSuite()

# suite.addTest(testAdd.TestAdd('test_add'))
# suite.addTest(testAdd.TestAdd('test_add2'))
#
# suite.addTest(testSub.TestSub('test_sub'))
# suite.addTest(testSub.TestSub('test_sub2'))
'''
    discover(start_dir, pattern='test*.py', top_level_dir=None)
    start_dir : 要测试的模块名或测试用例的目录
    pattern=test*.py' : 表示用例文件名的匹配原则。
    top_level_dir=None :测试模块的顶层目录，如果没有顶层目录，默认为None
'''

# 定义测试用例的目录为动迁目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # runner.run(suite)
    runner.run(discover)