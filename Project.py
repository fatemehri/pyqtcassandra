import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QErrorMessage, QMessageBox
from demo import Ui_Dialog
from cassandra.cluster import Cluster
from datetime import datetime, timedelta


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
        self.ui.comboBox.addItems(['Select an item', 'One last day', 'The last three days',
                                   'The last seven days', 'Custom'])
        self.ui.comboBox.currentIndexChanged.connect(self.datefilter)
        self.ui.pushButton.clicked.connect(self.showtable)
        self.ui.Cancel.clicked.connect(self.exit)

    def exit(self):
        sys.exit()

    def update_widgets(self):
        # Set titles
        self.Dialog.setWindowTitle('Tracking')
        self.ui.pushButton.setText('Track')

    def checkenable(self):
        if self.ui.textEdit_toDate.isEnabled():
            self.ui.textEdit_fromDate.setEnabled(0)
            self.ui.textEdit_toDate.setEnabled(0)
            self.ui.label_fromDate.setEnabled(0)
            self.ui.label_toDate.setEnabled(0)

    def datefilter(self):
        self.curr_date = datetime.today().date()
        if self.ui.comboBox.currentIndex() == 1:
            self.checkenable()
            self.prev_date = (self.curr_date - timedelta(days=1))
        elif self.ui.comboBox.currentIndex() == 2:
            self.checkenable()
            self.prev_date = (self.curr_date - timedelta(days=3))
        elif self.ui.comboBox.currentIndex() == 3:
            self.checkenable()
            self.prev_date = (self.curr_date - timedelta(days=7))
        elif self.ui.comboBox.currentIndex() == 4:
            self.ui.textEdit_fromDate.setEnabled(1)
            self.ui.textEdit_toDate.setEnabled(1)
            self.ui.label_fromDate.setEnabled(1)
            self.ui.label_toDate.setEnabled(1)

    def connection(self):
        start_time = datetime.now()
        # Cassandra connection
        self.mmsi = self.ui.lineEdit.text()
        cluster = Cluster(['10.10.110.50'])
        session = cluster.connect('coastal')
        try:
            query = "select * from coastal.cais where mmsi={0} and date>='{1}' and date<='{2}' allow filtering" \
                .format(self.mmsi, self.prev_date, self.curr_date)
            results = session.execute(query)
            end_time = datetime.now()

            if not results:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("There is no record(s) for this filter")
                msg.exec_()
            else:
                # Create Table
                self.table = QTableWidget()
                crow = self.table.rowCount()
                self.table.setColumnCount(19)
                self.table.setGeometry(20, 20, 2000, 2000)
                self.table.setHorizontalHeaderLabels(
                    ['mmsicode', 'mmsi', 'date', 'time', 'coastcode', 'cog10x', 'flagcode',
                     'lat', 'long', 'messagebody', 'messagetype', 'navstatus', 'paccuracy',
                     'raimflag', 'rot', 'sog10x', 'sourcefile', 'trueheading',
                     'vesselclass'])
                # Add rows
                row = 0
                for items in results:
                    self.table.setRowCount(crow + (row + 1))
                    for i in range(0, 19):
                        self.table.setItem(row, i, QTableWidgetItem(str(items[i])))
                    row += 1
                self.table.setWindowTitle("Total rows: " + str(row) + "      " + "Total execution time: "
                                          + str(round((end_time - start_time).total_seconds(), 2)) + ' s')
                self.table.show()
                # info = QMessageBox()
                # info.setIcon(QMessageBox.Information)
                # info.setText("Total rows: " + str(row) + "\n" +"Total execution time: "
                #              + str((end_time - start_time).total_seconds()))
                # info.exec_()

        except AttributeError as ae:
            print('There is no filter value', ae)

    def showtable(self):
        if self.ui.lineEdit.text() == '' or self.ui.comboBox.currentIndex() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select a Date item or fill mmsi")
            msg.exec_()

        if self.ui.textEdit_toDate.isEnabled():
            self.curr_date = self.ui.textEdit_toDate.toPlainText()
            self.prev_date = self.ui.textEdit_fromDate.toPlainText()
            if (datetime.strptime(self.curr_date, '%Y-%m-%d') - datetime.strptime(self.prev_date, '%Y-%m-%d')).days > 7:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Do not enter more than seven days apart")
                msg.exec_()
            else:
                self.connection()

        else:
            self.connection()


if __name__ == "__main__":
    RunDesignerGUI()
