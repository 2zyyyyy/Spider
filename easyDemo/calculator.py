# 计算器类


class Count:
    def __init__(self, a, b): # 在用这个类创建新的对象时 初始化
        self.a = int(a)
        self.b = int(b)

    # 计算加法
    def add(self):
        return self.a + self.b

    # 计算减法
    def sub(self):
        return self.a - self.b
