# Inspired by PyQt5 Creating Paint Application In 40 Minutes
#  https://www.youtube.com/watch?v=qEgyGyVA1ZQ

# NB If the menus do not work then click on another application ad then click back
# and they will work https://python-forum.io/Thread-Tkinter-macOS-Catalina-and-Python-menu-issue

# PyQt documentation links are prefixed with the word 'documentation' in the code below and can be accessed automatically
#  in PyCharm using the following technique https://www.jetbrains.com/help/pycharm/inline-documentation.html

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox, QColorDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QPixmap, QColor
import sys
from PyQt5.QtCore import Qt, QPoint
import random

class PaintingApplication(QMainWindow): # documentation https://doc.qt.io/qt-5/qmainwindow.html
    '''
    Painting Application class
    '''

    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Paint Application")

        # set the windows dimensions
        top = 400
        left = 400
        width = 800
        height = 600
        self.setGeometry(top, left, width, height)

        # set the icon
        # windows version
        self.setWindowIcon(QIcon("./icons/paint-brush.png")) # documentation: https://doc.qt.io/qt-5/qwidget.html#windowIcon-prop

        # image settings (default)
        self.image = QImage(self.size(), QImage.Format_RGB32) # documentation: https://doc.qt.io/qt-5/qimage.html#QImage-1
        self.image.fill(Qt.white) # documentation: https://doc.qt.io/qt-5/qimage.html#fill-1

        # draw settings (default)
        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.black # documenation: https://doc.qt.io/qtforpython/PySide2/QtCore/Qt.html
        self.lineType = Qt.SolidLine # documentation: https://doc.qt.io/qtforpython/PySide2/QtGui/QPen.html?highlight=cap%20types#PySide2.QtGui.PySide2.QtGui.QPen
        self.capType = Qt.RoundCap # documentation: https://doc.qt.io/qtforpython/PySide2/QtGui/QPen.html?highlight=cap%20types#PySide2.QtGui.PySide2.QtGui.QPen.capStyle
        self.joinType = Qt.RoundJoin

        # reference to last point recorded by mouse
        self.lastPoint = QPoint() # documentation: https://doc.qt.io/qt-5/qpoint.html

        # set up menus
        mainMenu = self.menuBar() # create and a menu bar
        fileMenu = mainMenu.addMenu(" File") # add the file menu to the menu bar, the space is required as "File" is reserved in Mac
        brushSizeMenu = mainMenu.addMenu(" Brush Size") # add the "Brush Size" menu to the menu bar
        brushColorMenu = mainMenu.addMenu(" Brush Colour") # add the "Brush Colour" menu to the menu bar
        penStyleMenu = mainMenu.addMenu("Line Type") # add a line style to pen on the menu bar
        capMenu = mainMenu.addMenu("Cap Type") # add a cap style to pen on the menu bar
        joinMenu = mainMenu.addMenu("Join Type") # add a join style to pen on the menu bar
        helpMenu = mainMenu.addMenu("Help") # add a help menu with information in popups


        # save menu item
        saveAction = QAction(QIcon("./icons/save.png"), "Save", self)   # create a save action with a png as an icon, documenation: https://doc.qt.io/qt-5/qaction.html
        saveAction.setShortcut("Ctrl+S")                                # connect this save action to a keyboard shortcut, documentation: https://doc.qt.io/qt-5/qaction.html#shortcut-prop
        fileMenu.addAction(saveAction)                                  # add the save action to the file menu, documentation: https://doc.qt.io/qt-5/qwidget.html#addAction
        saveAction.triggered.connect(self.save)                         # when the menu option is selected or the shortcut is used the save slot is triggered, documenation: https://doc.qt.io/qt-5/qaction.html#triggered

        # clear
        clearAction = QAction(QIcon("./icons/clear.png"), "Clear", self) # create a clear action with a png as an icon
        clearAction.setShortcut("Ctrl+C")                                # connect this clear action to a keyboard shortcut
        fileMenu.addAction(clearAction)                                  # add this action to the file menu
        clearAction.triggered.connect(self.clear)                        # when the menu option is selected or the shortcut is used the clear slot is triggered

        # Open
        openAction = QAction(QIcon("./icons/open.png"), "Open", self)   # create a open action with a png as an icon
        openAction.setShortcut("Ctrl+O")                                # connect this open action to a keyboard shortcut
        fileMenu.addAction(openAction)                                  # add the open action to the file menu
        openAction.triggered.connect(self.open)

        # exit
        exitAction = QAction(QIcon("./icons/exit.png"), "Exit", self)   # create a exit action with a png as an icon
        exitAction.setShortcut("Ctrl+X")                                # connect this exit action to a keyboard shortcut
        fileMenu.addAction(exitAction)                                  # add the exit action to the file menu
        exitAction.triggered.connect(self.exit)

        # brush thickness
        threepxAction = QAction(QIcon("./icons/three.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+3") #TODO changed the control options to be numbers
        brushSizeMenu.addAction(threepxAction) # connect the action to the function below
        threepxAction.triggered.connect(self.threepx)

        fivepxAction = QAction(QIcon("./icons/five.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+5")
        brushSizeMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivepx)

        sevenpxAction = QAction(QIcon("./icons/seven.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+7")
        brushSizeMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenpx)

        ninepxAction = QAction(QIcon("./icons/nine.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+9")
        brushSizeMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninepx)

        # brush colors
        blackAction = QAction(QIcon("./icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColorMenu.addAction(blackAction);
        blackAction.triggered.connect(self.black)

        redAction = QAction(QIcon("./icons/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColorMenu.addAction(redAction);
        redAction.triggered.connect(self.red)

        greenAction = QAction(QIcon("./icons/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColorMenu.addAction(greenAction);
        greenAction.triggered.connect(self.green)

        yellowAction = QAction(QIcon("./icons/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColorMenu.addAction(yellowAction);
        yellowAction.triggered.connect(self.yellow)

        # adding the pen style types
        dashLineAction = QAction(QIcon("./icons/dashLine.png"), "Dash Line", self)
        dashLineAction.setShortcut("Ctrl+D")
        penStyleMenu.addAction(dashLineAction)
        dashLineAction.triggered.connect(self.dashLine)

        dashDotDotAction = QAction(QIcon("./icons/dashDotDot.png"), "Dash Dot Dot Line", self)
        dashDotDotAction.setShortcut("Ctrl+V")
        penStyleMenu.addAction(dashDotDotAction)
        dashDotDotAction.triggered.connect(self.dottedLine)

        dotLineAction = QAction(QIcon("./icons/dottedLine.png"), "Dot Line", self)
        dotLineAction.setShortcut("Ctrl+T")
        penStyleMenu.addAction(dotLineAction)
        dotLineAction.triggered.connect(self.dashDotDOtLine)

        dashDotLineAction = QAction(QIcon("./icons/dashDot.png"), "Dash Dot Line", self)
        dashDotLineAction.setShortcut("Ctrl+W")
        penStyleMenu.addAction(dashDotLineAction)
        dashDotLineAction.triggered.connect(self.dashDotLine)

        solidLineAction = QAction(QIcon("./icons/solidLine.png"), "Solid Line", self)
        solidLineAction.setShortcut("Ctrl+l")
        penStyleMenu.addAction(solidLineAction)
        solidLineAction.triggered.connect(self.solidLine)

        # adding the cap Types menu options
        squareCapAction = QAction(QIcon("./icons/square.png"), "Square Cap", self)
        squareCapAction.setShortcut("Ctrl+Q")
        capMenu.addAction(squareCapAction)
        squareCapAction.triggered.connect(self.squareCap)

        flatCapAction = QAction(QIcon("./icons/flat.png"), "Flat Cap", self)
        flatCapAction.setShortcut("Ctrl+F")
        capMenu.addAction(flatCapAction)
        flatCapAction.triggered.connect(self.flatCap)

        roundCapAction = QAction(QIcon("./icons/round.png"), "Round Cap", self)
        roundCapAction.setShortcut("Ctrl+E")
        capMenu.addAction(roundCapAction)
        roundCapAction.triggered.connect(self.roundCap)

        # adding the join Types menu options
        bevelJoinAction = QAction(QIcon("./icons/bevel.png"), "Bevel join", self)
        bevelJoinAction.setShortcut("Ctrl+J")
        joinMenu.addAction(bevelJoinAction)
        bevelJoinAction.triggered.connect(self.bevelJoin)

        miterJoinAction = QAction(QIcon("./icons/miter.png"), "Miter Join", self)
        miterJoinAction.setShortcut("Ctrl+M")
        joinMenu.addAction(miterJoinAction)
        miterJoinAction.triggered.connect(self.miterJoin)

        roundJoinAction = QAction(QIcon("./icons/roundJoin.png"), "Round join", self)
        roundJoinAction.setShortcut("Ctrl+I")
        joinMenu.addAction(roundJoinAction)
        roundJoinAction.triggered.connect(self.roundJoin)

        # adding the help menu options
        aboutAction = QAction(QIcon("./icons/about.png"), "About", self)
        aboutAction.setShortcut("Ctrl+A")
        helpMenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.about)

        helpAction = QAction(QIcon("./icons/help.png"), "Help", self)
        helpAction.setShortcut("Ctrl+H")
        helpMenu.addAction(helpAction)
        helpAction.triggered.connect(self.help)


    # event handlers
    def mousePressEvent(self, event):       # when the mouse is pressed, documentation: https://doc.qt.io/qt-5/qwidget.html#mousePressEvent
        if event.button() == Qt.LeftButton:  # if the pressed button is the left button
            self.drawing = True             # enter drawing mode
            self.lastPoint = event.pos()    # save the location of the mouse press as the lastPoint
            print(self.lastPoint)           # print the lastPoint for debugging purposes

    def mouseMoveEvent(self, event):                        # when the mouse is moved, documenation: https://doc.qt.io/qt-5/qwidget.html#mouseMoveEvent
        if event.buttons() & Qt.LeftButton & self.drawing:     # if there was a press, and it was the left button and we are in drawing mode
            painter = QPainter(self.image)                  # object which allows drawing to take place on an image
            # allows the selection of brush colour, brush size, line type, cap type, join type. Images available here http://doc.qt.io/qt-5/qpen.html
            painter.setPen(QPen(self.brushColor, self.brushSize, self.lineType, self.capType, self.joinType))
            painter.drawLine(self.lastPoint, event.pos())   # draw a line from the point of the orginal press to the point to where the mouse was dragged to
            self.lastPoint = event.pos()                     # set the last point to refer to the point we have just moved to, this helps when drawing the next line segment
            self.update()                                   # call the update method of the widget which calls the paintEvent of this class

    def mouseReleaseEvent(self, event):                     # when the mouse is released, documentation: https://doc.qt.io/qt-5/qwidget.html#mouseReleaseEvent
        if event.button == Qt.LeftButton:                   # if the released button is the left button, documenation: https://doc.qt.io/qt-5/qt.html#MouseButton-enum ,
            self.drawing = False                            # exit drawing mode

    # paint events
    def paintEvent(self, event):
        # you should only create and use the QPainter object in this method, it should be a local variable
        canvasPainter = QPainter(self)                                          # create a new QPainter object, documenation: https://doc.qt.io/qt-5/qpainter.html
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())     # draw the image , documentation: https://doc.qt.io/qt-5/qpainter.html#drawImage-1

    # resize event
    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    # slots
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image","", "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath =="":               # if the file path is empty
            return                      # do nothing and return
        self.image.save(filePath)       # save file image to the file path


    def clear(self):
        self.image.fill(Qt.white)   # fill the image with white, documentaiton: https://doc.qt.io/qt-5/qimage.html#fill-2
        self.update()               # call the update method of the widget which calls the paintEvent of this class

    def threepx(self):              # the brush size is set to 3
        self.brushSize = 3

    def fivepx(self):               # the brush size is set to 5
        self.brushSize = 5

    def sevenpx(self):              # the brush size is set to 7
        self.brushSize = 7

    def ninepx(self):               # the brush size is set to 9
        self.brushSize = 9

    def black(self):                # the brush color is set to black
        self.brushColor = Qt.black

    def red(self):                  # the brush color is set to red
        self.brushColor = Qt.red

    def green(self):                # the brush color is set to green
        self.brushColor = Qt.green

    def yellow(self):               # the brush color is set to yellow
        self.brushColor = Qt.yellow

    # methods to set the already existent lineType to a
    # new lineType using the Qt class and the selected style
    def dashLine(self):
        self.lineType = Qt.DashLine

    def dottedLine(self):
        self.lineType = Qt.DotLine

    def dashDotDOtLine(self):
        self.lineType = Qt.DashDotDotLine

    def dashDotLine(self):
        self.lineType = Qt.DashDotLine

    def solidLine(self):
        self.lineType = Qt.SolidLine

    # methods to set the already existent capType to a
    # new capType using the Qt class and the selected style
    def squareCap(self):
        self.capType = Qt.SquareCap

    def flatCap(self):
        self.capType = Qt.FlatCap

    def roundCap(self):
        self.capType = Qt.RoundCap

    # methods to set the already existent joinType to a
    # new joinType using the Qt class and the selected style
    def bevelJoin(self):
        self.joinType = Qt.BevelJoin

    def miterJoin(self):
        self.joinType = Qt.MiterJoin

    def roundJoin(self):
        self.joinType = Qt.RoundJoin

    # exit method using the app class and the quit method
    def exit(self):
        app.quit()

    # About method using a QMessageBox class and the about method from it
    # in order to create the pop up message, passing in three parameters
    # the self, a Title for the pop up window and the message
    def about(self):
        QMessageBox.about(self, 'About Painting Application', 'Painting Application\n'
                                                              'Version 2019\n'
                                                              '© 2019 Sarah Narayamy Tavares Silva. All rights reserved\n'
                                                              '\n'
                                                              'The painting Application 2019 and its user interface is made\n'
                                                              'with the purpose of learning Python using the PyQt5 package.')

    # About method using the QMessageBox class and the about method from it
    # in order to create the pop up message, passing in three parameters
    # the self, a Title for the pop up window and the message
    def help(self):
        QMessageBox.about(self, "Let's get Started", 'Start by creating a new document\n'
                                                              'Save the document\n'
                                                              'Clear the page if you want to create a new document\n'
                                                              'Open an already saved document\n'
                                                              'Select the desired Brush Size\n'
                                                              'Select the desired Brush Colour\n'
                                                              'Select the desired Pen Style\n'
                                                              'Exit the Application')

    # open a file
    def open(self):
        '''
        This is an additional function which is not part of the tutorial. It will allow you to:
         - open a file doalog box,
         - filter the list of files according to file extension
         - set the QImage of your application (self.image) to a scaled version of the file)
         - update the widget
        '''
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if filePath == "":   # if not file is selected exit
            return
        with open(filePath, 'rb') as f: #open the file in binary mode for reading
            content = f.read() # read the file
        self.image.loadFromData(content) # load the data into the file
        width = self.width() # get the width of the current QImage in your application
        height = self.height() # get the height of the current QImage in your application
        self.image = self.image.scaled(width, height) # scale the image from file and put it in your QImage
        self.update() # call the update method of the widget which calls the paintEvent of this class


# this code will be executed if it is the main module but not if the module is imported
#  https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = PaintingApplication()
    window.show()
    app.exec() # start the event loop running