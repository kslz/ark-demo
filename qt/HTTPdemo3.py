import traceback
from threading import Thread
from time import sleep

from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QHeaderView, QTextBrowser
import requests


class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(QTextBrowser, str)

    # 还可以定义其他种类的信号
    update_table = Signal(str)


global_ms = MySignals()


class Stats:
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('..\jiemian\demo02.ui')
        # self.ui.requestMethod.addItem('GET')
        # self.ui.requestMethod.addItem('POST')
        """居中 但是不好用"""""
        # self.ui.requestMethod.setEditable(True)
        # self.ui.requestMethod.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        global_ms.text_print.connect(self.printToGui)
        self.ui.headerTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.addBtn.clicked.connect(self.add_line)
        self.ui.removeBtn.clicked.connect(self.remove_line)
        self.ui.sendBtn.clicked.connect(self.send_request)
        self.ui.clearBtn.clicked.connect(self.clear)

    def printToGui(self,fb,text):
        fb.append(str(text))
        fb.ensureCursorVisible() # 确保光标可见，即滚动文本到最下方光标处

    def task1(self):
        def threadFunc():
            global_ms.text_print.emit(self.ui.responseShow,'输出内容')

        thread = Thread(target= threadFunc)
        thread.start()

    def add_line(self):
        rowcount = self.ui.headerTable.rowCount()
        self.ui.headerTable.insertRow(rowcount)
        print(rowcount)

    def remove_line(self):
        rowcount = self.ui.headerTable.rowCount()
        self.ui.headerTable.removeRow(rowcount - 1)
        print(rowcount)

    def send_request(self):
        headers = {}
        tbl = self.ui.headerTable
        rowcount = tbl.rowCount()

        for r in range(0, rowcount):
            headers[tbl.item(r, 0).text()] = tbl.item(r, 1).text()
            # print(tbl.item(r,0).text()+':'+tbl.item(r,1).text())

        mtd = self.ui.requestMethod.currentText()
        print(mtd)

        # 创建新的线程去执行发送方法，
        # 服务器慢，只会在新线程中阻塞
        # 不影响主线程
        thread = Thread(target=self.threadSend,
                        # args=(s, prepared)
                        )
        thread.start()

        # if mtd == 'GET':
        #     url = self.ui.urlText.text()
        #     res = requests.get(url, headers=headers, params=self.ui.bodyText.toPlainText())
        # elif mtd == 'POST':
        #     url = self.ui.UrlText.text()
        #     res = requests.post(url, headers=headers, params=self.ui.bodyText.toPlainText())

        # print(res.text)
        # sleep(5)
        # self.ui.responseShow.append('response...')

    def threadSend(self):
        try:
            sleep(5)
            global_ms.text_print.emit(self.ui.responseShow, '输出内容')
        except:
            self.ui.outputWindow.append(
                traceback.format_exc())  # 打印异常

    def clear(self):
        self.ui.responseShow.setText('')


def main():
    print('OK')
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()


if __name__ == '__main__':
    main()
