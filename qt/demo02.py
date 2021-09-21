from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QMessageBox, QPushButton


class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('统计')

        self.textFdit = QPlainTextEdit(self.window)
        self.textFdit.setPlaceholderText('输入薪资列表')
        self.textFdit.move(10, 25)
        self.textFdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)
        self.button.clicked.connect(self.showInfo)

    def showInfo(self):
        info = self.textFdit.toPlainText()
        QMessageBox.about(self.window, '结果', f'''输入的数据为：{info}''')


app = QApplication([])
stats = Stats()
# stats.window.show()
app.exec_()
