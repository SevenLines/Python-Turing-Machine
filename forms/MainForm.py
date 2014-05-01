from PyQt4 import QtCore

from PySide.QtCore import QSettings
from PySide.QtGui import QMainWindow
from PySide.QtGui import QFileDialog
from forms.delegates.CellDelegate import Cell_Delegate
from forms.delegates.header_delegate import Header_Delegate

from forms.ui.FormMain_ui import Ui_MainForm
from models.turing_model import Turing_Model
from turing.turing import Turing


class MainForm(QMainWindow, Ui_MainForm):
    turing_model = Turing_Model(turing=Turing(path='turing/samples/2x'))
    last_path = ''

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.load_ini()
        self.tblTuring.setModel(self.turing_model)

        self.actionLoad.triggered.connect(self.load_machine)
        self.tblTuring.setItemDelegate(Cell_Delegate())

    def __del__(self):
        self.save_ini()

    def load_machine(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', self.last_path)
        if not path:
            return
        self.last_path = path
        self.turing_model.set_machine(turing=Turing(path=path))


    def save_ini(self):
        settings = QSettings('config.ini', QSettings.IniFormat)

        settings.beginGroup(self.__class__.__name__)
        settings.setValue('Geometry', self.saveGeometry())
        settings.setValue('splitter', self.splitter.saveState())
        settings.endGroup()

    def load_ini(self):
        settings = QSettings('config.ini', QSettings.IniFormat)

        settings.beginGroup(self.__class__.__name__)
        self.restoreGeometry(settings.value('Geometry'))
        self.splitter.restoreState(settings.value('splitter'))
        settings.endGroup()




