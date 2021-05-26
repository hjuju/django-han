from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        pass

    def insert_title_dict(self):
        pass

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output,3. dictout')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력')) # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()
            else:
                print('Wrong Number')
                continue


BugsMusic.main()
