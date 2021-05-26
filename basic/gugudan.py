'''
구구단 프로그램은 단을 입력받아서, 입력받은 단의 1~9의 곱을 출력하는 어플
단, 단은 정수이다.
'''


class Gugudan(object):

    dan = 0
    dict = {}

    def print_selected_dan(self):
        for i in range(2, 10):
            print(f'{self.dan} * {i} = {self.dan*i}')

    def print_all_dan(self):
        for i in range(2, 10):
            print(f'----{i}단----')
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')

    def print_dict_dan(self):
        d = self.dict
        for i in range(1, 10):
            d[i] = self.dan * i
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.dan} * {k} = {d.get(k)}')


    @staticmethod
    def main():
        g = Gugudan()
        while 1:
            menu = input('0. Exit, 1. Create 2. Read 3. input dan with dict')
            if menu == '0':
                pass
            elif menu == '1':
                g.dan = (int(input('단 입력: ')))
                g.print_selected_dan()
            elif menu == '2':
                g.print_all_dan()
            elif menu == '3':
                g.dan = (int(input('단 입력: ')))
                g.print_dict_dan()



Gugudan.main()
