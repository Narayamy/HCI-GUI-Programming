'''
Please make sure you use the PEP guide for naming conventions in your submission
- detailed guide: https://www.python.org/dev/peps/pep-0008/
- some examples: https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names

This assignment is heavily based on
A Currency Converter GUI Program - Python PyQt5 Desktop Application Development Tutorial
- GitHub: https://github.com/DarBeck/PyQT5_Tutorial/blob/master/currency_converter.py
- YouTube: https://www.youtube.com/watch?v=weKpTw1SjM4

- Layout
    - I would suggest QGridLayout
    - Use a QCalendarWidget which you will get from Zetcode tutorial-deleteBeforeSubmission 8 called "Widgets"

User operations
- Allows the selection of the stock to be purchased
- Allows the selection of the quantity to be purchased
- Allows the selection of the purchase date
- Displays the purchase total
- Allows the selection of the sell date
- Displays the sell total
- Displays the profit total

PyCharm Configuration Options
- Viewing Documentation when working with PyCham https://www.jetbrains.com/help/pycharm/viewing-external-documentation.html
- Configuring Python external Documenation on PyCharm https://www.jetbrains.com/help/pycharm/settings-tools-python-external-documentation.html
'''

# standard imports
import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QComboBox, QCalendarWidget, QDialog, QApplication, QGridLayout, QSpinBox
from PyQt5 import QtCore
from decimal import Decimal
from PyQt5.QtWidgets import *

import sys

class StockTradeProfitCalculator(QDialog):
    '''
    Provides the following functionality:

    - Allows the selection of the stock to be purchased
    - Allows the selection of the quantity to be purchased
    - Allows the selection of the purchase date
    - Displays the purchase total
    - Allows the selection of the sell date
    - Displays the sell total
    - Displays the profit total

    '''

    def __init__(self):
        '''
        This method requires substantial updates
        Each of the widgets should be suitably initalized and layed out
        '''
        super().__init__()

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
        self.setFixedSize(450, 500)

        # create a QGrid layout and apply to window
        qgrid = QGridLayout()
        self.setLayout(qgrid)

        # create an instance of a QComboBox
        #self.qComboStock = QComboBox()

        # Create labels
        labelSelected = QLabel("Stock Purchased: ")
        quantityPurchased = QLabel("Quantity Purchased: ")
        purchaseDate = QLabel("Purchase Date: ")
        purchaseTotal = QLabel("Purchase Total: ")
        sellDate = QLabel("Sell Date: ")
        sellTotal = QLabel("Sell Total: ")
        profitTotal = QLabel("Profit Total: ")
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
        qgrid.addWidget(self.calendar1,2,1)
        qgrid.addWidget(self.calendar2,4,1)

        # choose a suitable start dates for QCalenderWidgets
        #self.date_newest_QDate
        #dateSelected = self.calendar1.selectedDate()
        #self.date_newest_QDate_minus_2weeks
        #dateSelected = self.calendar1.selectedDate()

        # create QLabel for stock purchased



        # create QComboBox and populate it with a list of stocks

        # create CalendarWidgets for selection of purchase and sell dates

        # create QSpinBox to select stock quantity purchased

        # create QLabels to show the stock purchase total

        # create QLabels to show the stock sell total

        # create QLabels to show the stock profit total

        # initialize the layout - 6 rows to start

        # row 0 - stock selection

        # row 1 - quantity selection

        # row 2 - purchase date selection

        # row 3 - display purchase total

        # row 4 - sell date selection

        # row 5 - display sell total

        # row 6 - display sell total

        # set the calendar values
        # purchase: two weeks before most recent
        # sell: two weeks before more recent

        # connecting signals to slots to that a change in one control updates the UI

        # set the window title
        # update the UI


    def updateUi(self):
        '''
        This requires substantial development
        Updates the Ui when control values are changed, should also be called when the app initializes
        :return:
        '''
        try:
            print("")
            # get selected dates from calendars

            # perform necessary calculations to calculate totals

            # update the label displaying totals
        except Exception as e:
            print(e)


    def make_data(self):
        '''
        This code is complete
        Data source is derived from https://www.kaggle.com/camnugent/sandp500/download but use the provided file to avoid confusion

        Converts a CSV file to a dictonary fo dictionaries like

            Stock   -> Date      -> Close
            AAL     -> 08/02/2013 -> 14.75
                    -> 11/02/2013 -> 14.46
                    ...
            AAPL    -> 08/02/2013 -> 67.85
                    -> 11/02/2013 -> 65.56

        Helpful tutorials to understand this
        - https://stackoverflow.com/questions/482410/how-do-i-convert-a-string-to-a-double-in-python
        - nested dictionaries https://stackoverflow.com/questions/16333296/how-do-you-create-nested-dict-in-python
        - https://www.tutorialspoint.com/python3/python_strings.htm
        :return: a dictionary of dictionaries
        '''
        file = open("./all_stocks_5yr.csv","r")  # open a CSV file for reading https://docs.python.org/3/library/functions.html#open
        data = {}         # empty data dictionary
        file_rows = []    # empty list of file rows
        # add rows to the file_rows list
        for row in file:
            file_rows.append(row.strip()) # https://www.geeksforgeeks.org/python-string-strip-2/
        print("len(file_rows):" + str(len(file_rows)))

        # get the column headings of the CSV file
        row0 = file_rows[0]
        line = row0.split(",")
        column_headings = line
        print(column_headings)

        # get the unique list of stocks from the CSV file
        non_unique_stocks = []
        file_rows_from_row1_to_end = file_rows[1:len(file_rows) - 1]
        for row in file_rows_from_row1_to_end:
            line = row.split(",")
            non_unique_stocks.append(line[6])
        stocks = self.unique(non_unique_stocks)
        print("len(stocks):" + str(len(stocks)))
        print("stocks:" + str(stocks))

        # build the base dictionary of stocks
        for stock in stocks:
            data[stock] = {}

        # build the dictionary of dictionaries
        for row in file_rows_from_row1_to_end:
            line = row.split(",")
            date = self.string_date_into_QDate(line[0])
            stock = line[6]
            close_price = line[4]
            #include error handeling code if close price is incorrect
            data[stock][date]= float(close_price)
        print("len(data):",len(data))
        return data


    def string_date_into_QDate(self, date_String):
        '''
        This method is complete
        Converts a data in a string format like that in a CSV file to QDate Objects for use with QCalendarWidget
        :param date_String: data in a string format
        :return:
        '''
        date_list = date_String.split("-")
        date_QDate = QDate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return date_QDate


    def unique(self, non_unique_list):
        '''
        This method is complete
        Converts a list of non-unique values into a list of unique values
        Developed from https://www.geeksforgeeks.org/python-get-unique-values-list/
        :param non_unique_list: a list of non-unique values
        :return: a list of unique values
        '''
        # intilize a null list
        unique_list = []

        # traverse for all elements
        for x in non_unique_list:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
                # print list
        return unique_list

# This is complete
if __name__ == '__main__':

    app = QApplication(sys.argv)
    currency_converter = StockTradeProfitCalculator()
    currency_converter.show()
    sys.exit(app.exec_())
