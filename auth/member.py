class Member(object):

    id = ''
    pw = ''
    name = ''
    email = ''

    def join(self):
        pass

    def login(self):
        pass

    def mypage(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    @staticmethod
    def main():
        member = Member()
        while 1:
            menu = (input('0. 프로그램종료\n1. 회원가입\n2. 로그인\n'
                          '3. 내정보\n4. 정보수정\n5.회원탈퇴\n번호 입력: '))
            if menu == '1':
                pass
            elif menu == '2':
                pass
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            elif menu == '5':
                pass
