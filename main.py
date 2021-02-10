from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import  QIcon
import os
# 解决Mac刷新问题
os.putenv("QT_MAC_WANTS_LAYER", "1")
# 初始化窗口
app = QApplication([])
app.setWindowIcon(QIcon('logo.icns'))
# 加载UI
qfile_stats = QFile('ui.ui')
qfile_stats.open(QFile.ReadOnly)
windows = QUiLoader().load(qfile_stats)
windows.setWindowTitle('崔的记账工具v1.0')
def ok():
    # 日历
    date = windows.calendarWidget.selectedDate().toString('yyyy-MM-dd')
    # 获取消费标签
    list=windows.listWidget.currentItem().text()
    # 金额
    money = windows.money.text()
    # 是否报销
    reim = '不可报销'
    if windows.reimButton.isChecked():
        reim='可报销'
    if '工作性' in list :
        reim = '可报销'
    # 备注
    remarks = windows.remarks.text()
    # 填入表
    windows.plainTextEdit.appendPlainText(date+' '+list+' '+money+' '+reim+' '+remarks)
    windows.money.clear()
    windows.remarks.clear()

windows.remarks.returnPressed.connect(ok)
windows.money.returnPressed.connect(ok)
windows.okButton.clicked.connect(ok)
windows.show()
app.exec_()
