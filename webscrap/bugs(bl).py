from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}

    def set_url(self):
        pass

    def get_ranking(self):
        pass

    def insert_title_dict(self):
        pass

    def dict_to_dataframe(self):
        pass

    def df_to_csv(self):
        pass

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit\n'
                         '1. input time\n'
                         '2. output\n'
                         '3. dictout\n'
                         '4. dict to dataframe\n'
                         '5. save to csv\n'
                         '숫자입력: ')
            if menu == '0':
                break
            elif menu == '1':
                pass
            elif menu == '2':
                pass
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            elif menu == '5':
                pass
            else:
                pass
                continue


BugsMusic.main()
