import pandas as pd
from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        ls2 = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls2:
            self.artist_ls.append(i.find("a").text)

    def insert_title_dict(self):
        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        print(self.dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

    def df_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        melon = Melon()
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
                melon.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == '2':
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_ranking()
            elif menu == '3':
                melon.insert_title_dict()
            elif menu == '4':
                melon.dict_to_dataframe()
            elif menu == '5':
                melon.df_to_csv()
            else:
                print('Wrong number')
                continue


Melon.main()
