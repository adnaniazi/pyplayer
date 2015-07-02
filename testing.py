import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyListWidget(QListWidget):
  def __init__(self, parent):
    super(MyListWidget, self).__init__(parent)
    self.setAcceptDrops(True)
    self.setDragDropMode(QAbstractItemView.InternalMove)

  def dragEnterEvent(self, event):
    if event.mimeData().hasUrls():
      event.acceptProposedAction()
    else:
      super(MyListWidget, self).dragEnterEvent(event)

  def dragMoveEvent(self, event):
    super(MyListWidget, self).dragMoveEvent(event)

  def dropEvent(self, event):
    if event.mimeData().hasUrls():
      for url in event.mimeData().urls():
        self.addItem(url.path())
      event.acceptProposedAction()
    else:
      super(MyListWidget,self).dropEvent(event)

class MyWindow(QWidget):
  def __init__(self):
    super(MyWindow,self).__init__()
    self.setGeometry(100,100,300,400)
    self.setWindowTitle("Filenames")

    self.list = MyListWidget(self)
    layout = QVBoxLayout(self)
    layout.addWidget(self.list)

    self.setLayout(layout)

if __name__ == '__main__':

  app = QApplication(sys.argv)
  app.setStyle("plastique")

  window = MyWindow()
  window.show()

  sys.exit(app.exec_())
