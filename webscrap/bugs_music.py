from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

# 벅스: https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01

    @staticmethod
    def scrap(url, class_name):
        soup = BeautifulSoup(urlopen(url), 'lxml')
        count = 0
        print(f'----------------------{class_name} ranking-------------------------')
        for i in soup.find_all(name='p', attrs=({"class": class_name[0]})): # "artist"
            count += 1
            print(f'{str(count)}위) {class_name}: {i.find("a").text}')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = (input('0. 프로그램 종료\n1. URL 입력\n2. 음악 순위\n숫자입력: '))
            if menu == '0':
                print('프로그램을 종료 합니다.')
                break
            elif menu == '1':
                bugs.url = input('URL 입력: ')
            elif menu == '2':
                url = input('URL 입력: ')
                print(f'URL: {bugs}')
                bugs.scrap(input(), "artist" or title: '))
            else:
                print('잘못된 선택 입니다.')
                continue


BugsMusic.main()
