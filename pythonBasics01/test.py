# Library Imports
# import * = import all (NOT RECOMMENDED)
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # setting up dictionary of stocks
        #self.data = self.make_data()
        # sorting dictonary
        #self.stocks = sorted(self.data.keys())

        # print all the dates and close prices for AAL
        #print("all the dates and close prices for AAL", self.data['AAL'])
        # print the close price for AAL on 12/2/2013
        #print("the close price for AAL on 12/2/2013",self.data['AAL'][QDate(2013,2,12)])

        # set window title and size
        self.setWindowTitle("Stock Trade Profit Calculator")
        # first is width, second height
        self.setFixedSize(600, 500)

        # create a QGrid layout and apply to window
        qgrid = QGridLayout()
        self.setLayout(qgrid)

        # create an instance of a QComboBox
        #self.qComboStock = QComboBox()

        # Create labels
        labelSelected = QLabel("Stock Purchased: ")
        quantityPurchased = QLabel("Quantity Purchased")
        purchaseDate = QLabel("Purchase Date")
        purchaseTotal = QLabel("Purchase Total")
        sellDate = QLabel("Sell Date")
        sellTotal = QLabel("Sell Total")
        profitTotal = QLabel("Profit Total")
        #self.labelDisplayCombo = QLabel("####")

        # Create instances of a Calendar
        self.calendar1 = QCalendarWidget(self)
        self.calendar2 = QCalendarWidget(self)
        # Set the Grid to True on the calendar
        self.calendar1.setGridVisible(True)
        self.calendar2.setGridVisible(True)

        # Place the labels on the Grid Layout
        qgrid.addWidget(labelSelected,0,0)
        qgrid.addWidget(quantityPurchased,1,0)
        qgrid.addWidget(purchaseDate,2,0)
        qgrid.addWidget(purchaseTotal,3,0)
        qgrid.addWidget(sellDate,4,0)
        qgrid.addWidget(sellTotal,5,0)
        qgrid.addWidget(profitTotal,6,0)

        # Place the calendar on the Grid Layout
        qgrid.addWidget(self.calendar1,3,1)
        qgrid.addWidget(self.calendar2,5,1)






# Every GUI we create using Python and
# the PyQt5 framework will contain an instance
# of the QApplication class
app = QApplication(sys.argv)

# Create an instance of a Window
window = MainWindow()

# Display the window instance when the application runs
window.show()

# Create an event loop
app.exec_()