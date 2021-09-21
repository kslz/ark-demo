from threading import Thread
from time import sleep

name = ''


def threadFunc(arg1, arg2):
    print('子线程开始！')
    print(f'子线程参数为：{arg1},{arg2}')
    while name != 'lizi':
        print('wait name...')
        print('name is'+name)
        sleep(1)


thread = Thread(
    target=threadFunc,
    args=('a', 'b')
)
thread.start()
name = input('请输入姓名：')

thread.join()
print('all ok')
