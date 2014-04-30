from PyQt4.QtCore import QAbstractItemModel, QAbstractTableModel, QVariant, QModelIndex
from PyQt4.QtCore import Qt

from turing.turing import Turing, Rule


class Turing_Model(QAbstractTableModel):
    turing = Turing()
    states = None
    alphabet = None

    def __init__(self, QObject_parent=None, turing=None):
        QAbstractItemModel.__init__(self, QObject_parent)
        self.set_machine(turing)

    def set_machine(self, turing):
        self.beginResetModel()
        self.turing = turing
        self.states = self.turing.states
        self.alphabet = self.turing.alphabet
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.states)-1 if self.states else 0

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.alphabet) if self.alphabet else 0

    def data(self, index, int_role=None):
        assert (isinstance(index, QModelIndex))

        if not index.isValid():
            return QVariant()

        if int_role == Qt.DisplayRole:
            col = index.column()
            row = index.row() +1
            out = self.turing.rule(self.states[row], self.alphabet[col])
            if isinstance(out, Rule):
                out = out.preview
            return str(out)

        if int_role == Qt.EditRole:
            col = index.column()
            row = index.row() +1
            out = self.turing.rule(self.states[row], self.alphabet[col])
            if isinstance(out, Rule):
                out = out.preview
            return str(out)

        return QVariant()

    def flags(self, QModelIndex):
        return  Qt.ItemIsEditable | Qt.ItemIsEnabled

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role == Qt.DisplayRole:
            if Qt_Orientation == Qt.Horizontal:
                return self.alphabet[p_int]
            if Qt_Orientation == Qt.Vertical:
                return 'q{0}'.format(self.states[p_int+1])
        return QAbstractItemModel.headerData(self, p_int, Qt_Orientation, int_role)












