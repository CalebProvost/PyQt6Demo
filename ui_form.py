# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DemoClass(object):
    def setupUi(self, DemoClass):
        DemoClass.setObjectName("DemoClass")
        DemoClass.resize(800, 465)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=DemoClass)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 781, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HelloWorld_lbl = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.HelloWorld_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HelloWorld_lbl.setObjectName("HelloWorld_lbl")
        self.verticalLayout.addWidget(self.HelloWorld_lbl)
        self.listWidget = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.bottom_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.bottom_btn.setObjectName("bottom_btn")
        self.verticalLayout.addWidget(self.bottom_btn)

        self.retranslateUi(DemoClass)
        self.bottom_btn.clicked.connect(self.listWidget.selectAll) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DemoClass)

    def retranslateUi(self, DemoClass):
        _translate = QtCore.QCoreApplication.translate
        DemoClass.setWindowTitle(_translate("DemoClass", "DemoClass"))
        self.HelloWorld_lbl.setText(_translate("DemoClass", "Hello World"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("DemoClass", "Item1"))
        item = self.listWidget.item(1)
        item.setText(_translate("DemoClass", "Item2"))
        item = self.listWidget.item(2)
        item.setText(_translate("DemoClass", "Item3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.bottom_btn.setText(_translate("DemoClass", "PushButton"))
