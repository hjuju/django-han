class Conversion(object):

    @staticmethod
    def create_tp() -> ():
        pass

    @staticmethod
    def convert_tp_ls(tp) -> []:
        pass

    @staticmethod
    def convert_ls_fls(ls) -> []:
        pass

    @staticmethod
    def convert_fls_ils(ls) -> []:
        pass

    @staticmethod
    def convert_ls_dt(ls) -> {}:
        pass

    @staticmethod
    def convert_hel_tp(string) -> ():
        pass

    @staticmethod
    def convert_hel_ls(tp) -> []:
        pass

    @staticmethod
    def convert_ls_df(dt) -> object:
        pass

    @staticmethod
    def main():

        while 1:
            m = input('0-exit\n'
                      '1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list\n'
                      '8-dictionary to dataframe\n'
                      '번호입력: ')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                pass
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                pass
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                pass
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                pass
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                pass
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                pass
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                pass
            elif m == '8':
                pass
            #  7번
            else:
                continue


Conversion.main()
