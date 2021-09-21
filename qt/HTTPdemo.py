from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QHeaderView
import requests


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
        self.ui.headerTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.addBtn.clicked.connect(self.add_line)
        self.ui.removeBtn.clicked.connect(self.remove_line)
        self.ui.sendBtn.clicked.connect(self.send_request)

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
        if mtd == 'GET':
            url = self.ui.urlText.text()
            res = requests.get(url, headers=headers, params=self.ui.bodyText.toPlainText())
        elif mtd == 'POST':
            url = self.ui.UrlText.text()
            res = requests.post(url, headers=headers, params=self.ui.bodyText.toPlainText())

        print(res.text)
        self.ui.responseShow.append(res.text)



def main():
    print('OK')
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()


if __name__ == '__main__':
    main()
