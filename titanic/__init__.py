from titanic.views.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    while 1:
        menu = input('0. Exit\n'
                     '1. Pre_process\n'
                     '번호입력: ')
        if menu == '0':
            break
        elif menu == '1':
            controller.preprocessing('train.csv')
        elif menu == '2':
            pass
        elif menu == '3':
            pass
        elif menu == '4':
            pass
        else:
            continue