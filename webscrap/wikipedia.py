class Wikipedia(object):

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = input('0. 프로그램 종료\n1. URL 입력\n2. URL 조회\n숫자입력: ')
            if menu == '0':
                print('프로그램을 종료 합니다.')
                break
            elif menu == '1':
                wiki = input('URL 입력: ')
            elif menu == '2':
                print(f'URL: {wiki}')
            else:
                print('잘못된 선택입니다.')
                continue


Wikipedia.main()
