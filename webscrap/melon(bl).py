import pandas as pd
import requests
from bs4 import BeautifulSoup



class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all("p", attrs={"class": self.class_name[0]})
        for i, in ls1:
            self.artist_ls.append(i.find("a").text)
        ls2 = soup.find_all("p", attrs={"class": self.artist_ls[1]})
        for i in ls2:
            self.title_ls.append(i.find("a").text)

    def insert_title_dict(self):
        pd.DataFrame.from_dict(self.dict, )

    def dict_to_dataframe(self):
        pass

    def df_to_csv(self):
        pass

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
                print('프로그램을 종료 합니다.')
                break
            elif menu == '1':
                melon.set_url(input('날짜 입력: '))
            elif menu == '2':
                melon.class_name.append("title")
                melon.class_name.append("artist")
                melon.get_ranking()
            elif menu == '3':
                melon.insert_title_dict()
            elif menu == '4':
                melon.dict_to_dataframe()
            elif menu == '5':
                melon.df_to_csv()
            else:
                print('잘못 입력했습니다.')
                continue


Melon.main()
