from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class Naver_Stock(object):

    url = 'https://finance.naver.com/item/sise_day.nhn?code=005930&page=1'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    code = ''
    page = ''
    date_ls = []
    info_ls = []
    dt = {}
    df = None

    def webdriver(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(f'{self.url}')
        # driver.get(f'{self.code}&page={self.page}')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        date = soup.find_all("td", {"align": "center"})
        info = soup.find_all("td", {"class": "num"})
        for i in date:
            self.date_ls.append(i.find("span").text)
        for i in info:
            self.info_ls.append(i.find("span").text)
        print(self.date_ls, self.info_ls)
        driver.close()

    def insert_dict(self):
        self.dt[self.date_ls[0]] = self.info_ls[0:6]
        print(self.dt)

    def dict_to_df(self):
        self.df = pd.DataFrame.from_dict(self.dt, orient='index')
        print(self.df)

    def save_to_csv(self):
        path = './data/naverstock.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


if __name__ == '__main__':
    naver = Naver_Stock()
    '''
    naver.code = input('코드 번호 입력: ')
    naver.page = input('가져올 페이지 수 입력: ')
    '''
    naver.webdriver()
    naver.insert_dict()
    naver.dict_to_df()
    naver.save_to_csv()