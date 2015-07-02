# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui.ui'
#
# Created: Thu Jul  2 08:53:01 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(765, 582)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gui-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPlayer.sizePolicy().hasHeightForWidth())
        self.videoPlayer.setSizePolicy(sizePolicy)
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.verticalLayout.addWidget(self.videoPlayer)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seekSlider.sizePolicy().hasHeightForWidth())
        self.seekSlider.setSizePolicy(sizePolicy)
        self.seekSlider.setIconVisible(False)
        self.seekSlider.setIconSize(QtCore.QSize(16, 16))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayout_2.addWidget(self.seekSlider)
        self.track_time = QtGui.QLabel(self.centralwidget)
        self.track_time.setObjectName(_fromUtf8("track_time"))
        self.horizontalLayout_2.addWidget(self.track_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_previous = QtGui.QToolButton(self.centralwidget)
        self.toolButton_previous.setStyleSheet(_fromUtf8("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
""))
        self.toolButton_previous.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_previous.setIcon(icon1)
        self.toolButton_previous.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_previous.setObjectName(_fromUtf8("toolButton_previous"))
        self.horizontalLayout.addWidget(self.toolButton_previous)
        self.toolButton_play_pause = QtGui.QToolButton(self.centralwidget)
        self.toolButton_play_pause.setStyleSheet(_fromUtf8("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
""))
        self.toolButton_play_pause.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_play_pause.setIcon(icon2)
        self.toolButton_play_pause.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_play_pause.setObjectName(_fromUtf8("toolButton_play_pause"))
        self.horizontalLayout.addWidget(self.toolButton_play_pause)
        self.toolButton_next = QtGui.QToolButton(self.centralwidget)
        self.toolButton_next.setStyleSheet(_fromUtf8("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
""))
        self.toolButton_next.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_next.setIcon(icon3)
        self.toolButton_next.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_next.setObjectName(_fromUtf8("toolButton_next"))
        self.horizontalLayout.addWidget(self.toolButton_next)
        self.toolButton_stop = QtGui.QToolButton(self.centralwidget)
        self.toolButton_stop.setStyleSheet(_fromUtf8("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
""))
        self.toolButton_stop.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_stop.setIcon(icon4)
        self.toolButton_stop.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_stop.setObjectName(_fromUtf8("toolButton_stop"))
        self.horizontalLayout.addWidget(self.toolButton_stop)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.toolButton_fullscreen = QtGui.QToolButton(self.centralwidget)
        self.toolButton_fullscreen.setStyleSheet(_fromUtf8("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
""))
        self.toolButton_fullscreen.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/full-screen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_fullscreen.setIcon(icon5)
        self.toolButton_fullscreen.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_fullscreen.setObjectName(_fromUtf8("toolButton_fullscreen"))
        self.horizontalLayout.addWidget(self.toolButton_fullscreen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFiel = QtGui.QMenu(self.menubar)
        self.menuFiel.setObjectName(_fromUtf8("menuFiel"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setStyleSheet(_fromUtf8("QPushButton{\n"
"background : trasperent\n"
"}\n"
""))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_2.addWidget(self.listWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionMy_playlist = QtGui.QAction(MainWindow)
        self.actionMy_playlist.setObjectName(_fromUtf8("actionMy_playlist"))
        self.menuFiel.addAction(self.actionLoad)
        self.menuFiel.addAction(self.actionExit)
        self.menuView.addAction(self.actionMy_playlist)
        self.menubar.addAction(self.menuFiel.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPlayer", None))
        self.seekSlider.setToolTip(_translate("MainWindow", "Seek", None))
        self.track_time.setToolTip(_translate("MainWindow", "Current time | Total time", None))
        self.track_time.setText(_translate("MainWindow", "00:00 | 00:00", None))
        self.toolButton_previous.setToolTip(_translate("MainWindow", "Previous track", None))
        self.toolButton_play_pause.setToolTip(_translate("MainWindow", "Play or Pause", None))
        self.toolButton_next.setToolTip(_translate("MainWindow", "Next track", None))
        self.toolButton_stop.setToolTip(_translate("MainWindow", "Stop", None))
        self.volumeSlider.setToolTip(_translate("MainWindow", "Volume", None))
        self.toolButton_fullscreen.setToolTip(_translate("MainWindow", "Fullscreen (Press Esc key to exit)", None))
        self.menuFiel.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "My playlist", None))
        self.listWidget.setToolTip(_translate("MainWindow", "Playlist", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionMy_playlist.setText(_translate("MainWindow", "My_playlist", None))

from PyQt4 import phonon
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

