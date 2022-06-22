# Library Imports
# import * = import all (NOT RECOMMENDED)
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #Title our application and set the size
        self.setWindowTitle("Basic Calendar App")
        self.setFixedSize(400, 200)

        # Create a layout
        qGrid = QGridLayout()

        #apply the layout to the window
        self.setLayout(qGrid)

        # Create instances of labels and initialise
        label = QLabel("Todays date:")
        labelDate = QLabel("16 Oct 2019")

        # Create an instance of a Calendar
        calendar1 = QCalendarWidget(self)
        # set the grid to true on the calendar
        calendar1.setGridVisible(True)
        qGrid.addWidget(calendar1, 0, 0)

        # read the date from the calendar
        dateSelected = calendar1.selectedDate()

        # update labelDate with the date selected in the calendar
        # labelDate = dateSelected.toString()

        # print the selected date to the console
        print(dateSelected.toString())

        # Update the label named labelDate
        dateStr = dateSelected.toString()
        labelDate.setText(dateStr)

        # If a user clicks on a date in the calendar
        # we call a function to handle that click
        # calendar1.clicked.connect(self.showDate)

        # Place the labels on the Grid
        qGrid.addWidget(label, 0, 1)
        qGrid.addWidget(labelDate, 1, 1)






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