import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem
from demo import Ui_Dialog
from cassandra.cluster import Cluster


class RunDesignerGUI():
    def __init__(self):
        # Create body Dialog
        app = QApplication(sys.argv)
        self.Dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        # Call action's functions
        self.update_widgets()
        self.button_Action()

        # Display window
        self.Dialog.show()
        sys.exit(app.exec_())

    def button_Action(self):
        # Call functions
        self.ui.pushButton.clicked.connect(self.showtable)
        self.ui.Cancel.clicked.connect(self.exit)

    def exit(self):
        sys.exit()

    def update_widgets(self):
        # Set titles
        self.Dialog.setWindowTitle('Tracking')
        self.ui.pushButton.setText('Track')

    def showtable(self):
        # Textbox
        self.mmsi = self.ui.textEdit_MMSI.toPlainText()
        self.fDate = self.ui.textEdit_fDate.toPlainText()

        # Cassandra connection
        cluster = Cluster()
        session = cluster.connect('test')
        query = "select * from test.staticfeatures where mmsi={0} and date='{1}' allow filtering"\
            .format(self.mmsi, self.fDate)
        results = session.execute(query)

        # Create Table
        self.table = QTableWidget()
        crow = self.table.rowCount()
        self.table.setColumnCount(19)
        self.table.setGeometry(20, 20, 2000, 2000)
        self.table.setWindowTitle('Results')
        self.table.setHorizontalHeaderLabels(['mmsicode', 'mmsi', 'imo', 'vesseltypecode', 'flagname', 'callsign',
                                              'length', 'width', 'vesselname', 'vesselclass', 'date', 'destination',
                                              'draught', 'eta', 'extractedvesseltype', 'messagetype', 'source', 'time',
                                              'vesseltypemain'])
        # Add rows
        row = 0
        for items in results:
            self.table.setRowCount(crow + (row + 1))
            for i in range(0, 19):
                self.table.setItem(row, i, QTableWidgetItem(str(items[i])))
            row += 1

        self.table.show()


if __name__ == "__main__":
    RunDesignerGUI()
