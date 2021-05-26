import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        pass

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = input('0. 프로그램 종료\n1. URL 입력\n2. 음악 순위\n숫자입력: ')
            if menu == '0':
                print('프로그램을 종료 합니다.')
                break
            elif menu == '1':
                melon.set_url(input('날짜 입력: '))
            elif menu == '2':
                pass
            elif menu == '3':
                pass
            else:
                print('잘못 입력했습니다.')
                continue


Melon.main()
