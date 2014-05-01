from PyQt4.QtCore import QModelIndex
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTableView, QAbstractItemView


class TableViewTuring(QTableView):
    def __init__(self, QWidget_parent=None):
        QTableView.__init__(self, QWidget_parent)
        self.clicked.connect(self.click)

    def click(self, index):
        assert (isinstance(index, QModelIndex))
        self.edit(index)








