from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QMessageBox, QPushButton


class Stats():
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('..\jiemian\demo01.ui')
        self.ui.btn.clicked.connect(self.showInfo)

    def showInfo(self):
        info = self.ui.textedit.toPlainText()
        QMessageBox.about(self.ui,
                          '统计结果',
                          f'''输入的数据为：{info}'''
                          )


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
