from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = ''
    title_ls = []
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', attrs=({"class": self.class_name}))
        for i in all_div:
            self.title_ls.append(i.find("a").text)
        print(self.title_ls)
        driver.close()

    def insert_dict(self):
        print(dict(zip([i+1 for i in range(len(self.title_ls))], self.title_ls)))

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict()

    def save_to_csv(self):
        pass


if __name__ == '__main__':
    naver = NaverMovie()
    naver.class_name = input("입력 ex) tit3: ")
    naver.scrap()
    naver.insert_dict()
