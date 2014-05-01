from PySide.QtCore import QModelIndex
from PySide.QtCore import Qt
from PySide.QtGui import QTableView, QAbstractItemView


class TableViewTuring(QTableView):
    def __init__(self, QWidget_parent=None):
        QTableView.__init__(self, QWidget_parent)
        self.clicked.connect(self.click)

    def click(self, index):
        assert (isinstance(index, QModelIndex))
        self.edit(index)








