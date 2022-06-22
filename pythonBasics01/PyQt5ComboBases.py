# Library Imports
# import * = import all (NOT RECOMMENDED)
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # set window title and size
        self.setWindowTitle("Combo Boxes in PyQt5")
        # first is width, second height
        self.setFixedSize(250, 150)

        # create a QGrid layout and apply to window
        qGrid = QGridLayout()
        self.setLayout(qGrid)

        # create an instance of a QComboBox
        self.qComboCars = QComboBox()

        # Create two labels
        labelSelected = QLabel("You Selected: ")
        self.labelDisplayCombo = QLabel("Audi")

        # Create an instance of a Button
        buttonUpdate = QPushButton("Update")

        # Add items to the ComboBox
        self.qComboCars.addItem("Audi")
        self.qComboCars.addItem("BMW")
        self.qComboCars.addItem("Ferrari")
        self.qComboCars.addItem("Ford")

        # Add labels to display
        qGrid.addWidget(labelSelected, 1, 0)
        qGrid.addWidget(self.labelDisplayCombo, 1, 1)

        # Add the comboBox to the layout
        qGrid.addWidget(self.qComboCars, 0, 0)

        # Add the button to the layout
        qGrid.addWidget(buttonUpdate, 2, 0)

        # State the function to call when the button is pressed
        buttonUpdate.clicked.connect(self.readCombo)

    def readCombo(self):
        print("Updating label")
        # read the selection of the comboBox
        comboValue = self.qComboCars.currentText()
        print(str(comboValue))
        # Update the label to reflect ComboBox selection
        self.labelDisplayCombo.setText(str(comboValue))


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