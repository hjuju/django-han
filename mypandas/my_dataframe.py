class MyDataframe(object):

    def __init__(self, columns, index):
        self.columns = columns
        self.index = index

    @staticmethod
    def main():
        df = MyDataframe(10, 3)


MyDataframe.main()
