import urllib.request
from bs4 import BeautifulSoup


class Melon2(object):

    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        print('-----------제목-----------')
        for i in soup.find_all("div", {"class": self.class_name[0]}):
            print(f'{i.find("a").text}')
        print('-----------가수-----------')
        for i in soup.find_all("div", {"class": self.class_name[1]}):
            print(f'{i.find("a").text}')

    @staticmethod
    def main():
        m = Melon2()
        while 1:
            menu = input('0. 프로그램 종료\n1. 시간 입력\n2. 출력\n번호 입력: ')
            if menu == '1':
                m.set_url(input('예)2021052511: '))
            elif menu == '2':
                m.class_name.append('ellipsis rank01')
                m.class_name.append('ellipsis rank02')
                m.get_ranking()
            else:
                print('잘못 선택했습니다.')


Melon2.main()