# Library Imports
# import * = import all (NOT RECOMMENDED)
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Title our application and set the size
        self.setWindowTitle("Basic Calendar App")
        self.setFixedSize(500, 300)

        # Create a Layout
        qgrid = QGridLayout()

        # Apply the layout to our window
        self.setLayout(qgrid)

        # Create instances of labels and initialise
        label = QLabel("Todays Date: ")
        self.labelDate = QLabel("16 Oct 2019")

        # Create an instance of a Calendar
        self.calendar1 = QCalendarWidget(self)
        # Set the Grid to True on the calendar
        self.calendar1.setGridVisible(True)

        # Read the date from the calendar
        dateSelected = self.calendar1.selectedDate()

        # Update labelDate with the Date Selected in the
        # calendar
        print(dateSelected.toString())

        # Update the label named labelDate
        dateStr = dateSelected.toString()
        self.labelDate.setText(dateStr)

        # If a user a clicks on a DATE in the calendar
        # we call a function to handle that click
        self.calendar1.clicked.connect(self.showDate)


        # Place the labels on the Grid Layout
        qgrid.addWidget(label,0,0)
        qgrid.addWidget(self.labelDate,0,1)

        # Place the calendar on the Grid Layout
        qgrid.addWidget(self.calendar1,1,0)


    def showDate(self):
        #Read the date from the calendar and display
        print("Updating Date")
        # Turn off the Grid
        self.calendar1.setGridVisible(False)
        # Get the date from the calendar
        dateSelected = self.calendar1.selectedDate()

        # Print to the console the dates selected
        print(dateSelected)
        print(dateSelected.toString())

        # Update the Date on the label
        self.labelDate.setText(dateSelected.toString())

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