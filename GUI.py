# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys

import networkx as nx
from PyQt5 import QtCore, QtGui, QtWidgets

import controller as ct


class Ui_MainWindow(object):
    def __init__(self, g):
        self.g = g

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1080, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 310, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 20, 261, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.remove_edge_t2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_edge_t2.sizePolicy().hasHeightForWidth())
        self.remove_edge_t2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.remove_edge_t2.setFont(font)
        self.remove_edge_t2.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_edge_t2.setObjectName("remove_edge_t2")
        self.gridLayout.addWidget(self.remove_edge_t2, 3, 1, 1, 1)
        self.remove_node_t = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_node_t.sizePolicy().hasHeightForWidth())
        self.remove_node_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.remove_node_t.setFont(font)
        self.remove_node_t.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_node_t.setObjectName("remove_node_t")
        self.gridLayout.addWidget(self.remove_node_t, 1, 0, 1, 2)
        self.remove_edge_t3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_edge_t3.sizePolicy().hasHeightForWidth())
        self.remove_edge_t3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.remove_edge_t3.setFont(font)
        self.remove_edge_t3.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_edge_t3.setObjectName("remove_edge_t3")
        self.gridLayout.addWidget(self.remove_edge_t3, 3, 2, 1, 1)
        self.add_edge_t2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.add_edge_t2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_edge_t2.sizePolicy().hasHeightForWidth())
        self.add_edge_t2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.add_edge_t2.setFont(font)
        self.add_edge_t2.setAlignment(QtCore.Qt.AlignCenter)
        self.add_edge_t2.setObjectName("add_edge_t2")
        self.gridLayout.addWidget(self.add_edge_t2, 2, 1, 1, 1)
        self.add_edge_t3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_edge_t3.sizePolicy().hasHeightForWidth())
        self.add_edge_t3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.add_edge_t3.setFont(font)
        self.add_edge_t3.setAlignment(QtCore.Qt.AlignCenter)
        self.add_edge_t3.setObjectName("add_edge_t3")
        self.gridLayout.addWidget(self.add_edge_t3, 2, 2, 1, 1)
        self.add_edge_t1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_edge_t1.sizePolicy().hasHeightForWidth())
        self.add_edge_t1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.add_edge_t1.setFont(font)
        self.add_edge_t1.setAlignment(QtCore.Qt.AlignCenter)
        self.add_edge_t1.setObjectName("add_edge_t1")
        self.gridLayout.addWidget(self.add_edge_t1, 2, 0, 1, 1)
        self.remove_edge_t1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_edge_t1.sizePolicy().hasHeightForWidth())
        self.remove_edge_t1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.remove_edge_t1.setFont(font)
        self.remove_edge_t1.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_edge_t1.setObjectName("remove_edge_t1")
        self.gridLayout.addWidget(self.remove_edge_t1, 3, 0, 1, 1)
        self.add_node_t = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_node_t.sizePolicy().hasHeightForWidth())
        self.add_node_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.add_node_t.setFont(font)
        self.add_node_t.setAlignment(QtCore.Qt.AlignCenter)
        self.add_node_t.setObjectName("add_node_t")
        self.gridLayout.addWidget(self.add_node_t, 0, 0, 1, 2)

        # Solve button
        self.solve_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solve_b.sizePolicy().hasHeightForWidth())
        self.solve_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.solve_b.setFont(font)
        self.solve_b.setObjectName("solve_b")
        self.gridLayout.addWidget(self.solve_b, 4, 0, 1, 3)
        self.solve_b.clicked.connect(self.solve_clicked)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Add node button
        self.add_node_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_node_b.sizePolicy().hasHeightForWidth())
        self.add_node_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.add_node_b.setFont(font)
        self.add_node_b.setObjectName("add_node_b")
        self.verticalLayout.addWidget(self.add_node_b)
        self.add_node_b.clicked.connect(self.add_node_clicked)

        # Remove node button
        self.remove_node_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_node_b.sizePolicy().hasHeightForWidth())
        self.remove_node_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.remove_node_b.setFont(font)
        self.remove_node_b.setObjectName("remove_node_b")
        self.verticalLayout.addWidget(self.remove_node_b)
        self.remove_node_b.clicked.connect(self.remove_node_clicked)

        # Add edge button
        self.add_edge_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_edge_b.sizePolicy().hasHeightForWidth())
        self.add_edge_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.add_edge_b.setFont(font)
        self.add_edge_b.setObjectName("add_edge_b")
        self.verticalLayout.addWidget(self.add_edge_b)
        self.add_edge_b.clicked.connect(self.add_edge_clicked)

        # Remove edge button
        self.remove_edge_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_edge_b.sizePolicy().hasHeightForWidth())
        self.remove_edge_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.remove_edge_b.setFont(font)
        self.remove_edge_b.setObjectName("remove_edge_b")
        self.verticalLayout.addWidget(self.remove_edge_b)
        self.remove_edge_b.clicked.connect(self.remove_edge_clicked)

        # Clear all button
        self.clear_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_b.sizePolicy().hasHeightForWidth())
        self.clear_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.clear_b.setFont(font)
        self.clear_b.setObjectName("clear_b")
        self.verticalLayout.addWidget(self.clear_b)
        self.clear_b.clicked.connect(self.clear_all_clicked)

        # Helper text
        self.helper_t = QtWidgets.QTextEdit(self.centralwidget)
        self.helper_t.setEnabled(True)
        self.helper_t.setGeometry(QtCore.QRect(23, 477, 431, 241))
        self.helper_t.setReadOnly(True)
        self.helper_t.setObjectName("helper_t")
        self.helper_t.setFontPointSize(12)

        self.solve_t = QtWidgets.QTextEdit(self.centralwidget)
        self.solve_t.setEnabled(True)
        self.solve_t.setGeometry(QtCore.QRect(540, 170, 511, 551))
        self.solve_t.setReadOnly(True)
        self.solve_t.setObjectName("solve_t")
        self.solve_t.setFontPointSize(10)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 20, 241, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Source node button
        self.source_node_b = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_node_b.sizePolicy().hasHeightForWidth())
        self.source_node_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.source_node_b.setFont(font)
        self.source_node_b.setObjectName("source_node_b")
        self.verticalLayout_2.addWidget(self.source_node_b)
        self.source_node_b.clicked.connect(self.source_clicked)

        # Sink node button
        self.sink_node_b = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sink_node_b.sizePolicy().hasHeightForWidth())
        self.sink_node_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sink_node_b.setFont(font)
        self.sink_node_b.setObjectName("sink_node_b")
        self.verticalLayout_2.addWidget(self.sink_node_b)
        self.sink_node_b.clicked.connect(self.sink_clicked)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(800, 20, 241, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.source_node_t = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_node_t.sizePolicy().hasHeightForWidth())
        self.source_node_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.source_node_t.setFont(font)
        self.source_node_t.setAlignment(QtCore.Qt.AlignCenter)
        self.source_node_t.setObjectName("source_node_t")
        self.verticalLayout_3.addWidget(self.source_node_t)
        self.sink_node_t = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sink_node_t.sizePolicy().hasHeightForWidth())
        self.sink_node_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.sink_node_t.setFont(font)
        self.sink_node_t.setAlignment(QtCore.Qt.AlignCenter)
        self.sink_node_t.setObjectName("sink_node_t")
        self.verticalLayout_3.addWidget(self.sink_node_t)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 430, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setShortcut("")
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Flow Graph Solver"))
        self.remove_edge_t2.setPlaceholderText(_translate("MainWindow", "To"))
        self.remove_node_t.setPlaceholderText(_translate("MainWindow", "X2"))
        self.remove_edge_t3.setPlaceholderText(_translate("MainWindow", "Weight"))
        self.add_edge_t2.setPlaceholderText(_translate("MainWindow", "To"))
        self.add_edge_t3.setPlaceholderText(_translate("MainWindow", "Weight"))
        self.add_edge_t1.setPlaceholderText(_translate("MainWindow", "From"))
        self.remove_edge_t1.setPlaceholderText(_translate("MainWindow", "From"))
        self.add_node_t.setPlaceholderText(_translate("MainWindow", "X1"))
        self.solve_b.setText(_translate("MainWindow", "Solve"))
        self.add_node_b.setText(_translate("MainWindow", "Add node"))
        self.remove_node_b.setText(_translate("MainWindow", "Remove node"))
        self.add_edge_b.setText(_translate("MainWindow", "Add edge"))
        self.remove_edge_b.setText(_translate("MainWindow", "Remove edge"))
        self.clear_b.setText(_translate("MainWindow", "Clear all"))
        self.label_2.setText(_translate("MainWindow", "Helper"))
        self.source_node_b.setText(_translate("MainWindow", "Source Node"))
        self.sink_node_b.setText(_translate("MainWindow", "Sink Node"))
        self.source_node_t.setPlaceholderText(_translate("MainWindow", "Default: First node entered"))
        self.sink_node_t.setPlaceholderText(_translate("MainWindow", "Default: Last node entered"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.source_node_b.setText(_translate("MainWindow", "Source Node"))

    def add_node_clicked(self):
        txt = ct.add_node(self.g, self.add_node_t.text())
        txt = self.helper_t.toPlainText() + "\n" + txt
        print(G.nodes)
        self.helper_t.setText(txt)
        self.add_node_t.clear()
        ct.refresh(self.g)

    def remove_node_clicked(self):
        txt = ct.remove_node(self.g, self.remove_node_t.text())
        txt = self.helper_t.toPlainText() + "\n" + txt
        print(G.nodes)
        self.helper_t.setText(txt)
        self.remove_node_t.clear()
        ct.refresh(self.g)

    def add_edge_clicked(self):
        txt = ct.add_edge(self.g, self.add_edge_t1.text(), self.add_edge_t2.text(), self.add_edge_t3.text())
        txt = self.helper_t.toPlainText() + "\n" + txt
        print(G.edges(data=True))
        self.helper_t.setText(txt)
        self.add_edge_t1.clear()
        self.add_edge_t2.clear()
        self.add_edge_t3.clear()
        ct.refresh(self.g)

    def remove_edge_clicked(self):
        txt = ct.remove_edge(self.g, self.remove_edge_t1.text(), self.remove_edge_t2.text(), self.remove_edge_t3.text())
        txt = self.helper_t.toPlainText() + "\n" + txt
        print(G.edges)
        self.helper_t.setText(txt)
        self.remove_edge_t1.clear()
        self.remove_edge_t2.clear()
        self.remove_edge_t3.clear()
        ct.refresh(self.g)

    def clear_all_clicked(self):
        self.g.clear()
        txt = "Graph cleared"
        txt = self.helper_t.toPlainText() + "\n" + txt
        self.helper_t.setText(txt)
        ct.refresh(self.g)

    def solve_clicked(self):
        txt = ct.solve(self.g, self.source_node_t.text(), self.sink_node_t.text())
        self.solve_t.setText(txt)

    def source_clicked(self):
        txt = "Source node assigned successfully"
        txt = self.helper_t.toPlainText() + "\n" + txt
        self.helper_t.setText(txt)

    def sink_clicked(self):
        txt = "Sink node assigned successfully"
        txt = self.helper_t.toPlainText() + "\n" + txt
        self.helper_t.setText(txt)


if __name__ == "__main__":
    G = nx.MultiDiGraph()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(G)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
