from PyQt4.QtCore import QSize
from PyQt4.QtGui import QAbstractItemDelegate, QItemDelegate


class Header_Delegate(QItemDelegate):
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return QItemDelegate.createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex)

    def setEditorData(self, QWidget, QModelIndex):
        QItemDelegate.setEditorData(self, QWidget, QModelIndex)

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex):
        QItemDelegate.setModelData(self, QWidget, QAbstractItemModel, QModelIndex)

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QItemDelegate.updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex)





