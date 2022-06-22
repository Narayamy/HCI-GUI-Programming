from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGridLayout, QAction, QMessageBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from board import Board
from score_board import ScoreBoard

class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        #set up menus
        mainMenu = self.menuBar() # create and a menu bar
        playMenu = mainMenu.addMenu("Play") # add the Play menu to the menu bar
        goalMenu = mainMenu.addMenu("Game Goal") # add the "Game Goal" menu to the menu bar
        hotToPlayMenu = mainMenu.addMenu("How to Play") # add the "How to Play" menu to the menu bar
        rulesMenu = mainMenu.addMenu("Rules") # add rules on the menu bar

        # adding the play menu options
        playAction = QAction(QIcon("./images/play.png"), "Play", self)
        playAction.setShortcut("Ctrl+P")
        playMenu.addAction(playAction)
        #playAction.triggered.connect(self.play)

        exitAction = QAction(QIcon("./images/exit.png"), "Quit Game", self)
        exitAction.setShortcut("Ctrl+Q")
        playMenu.addAction(exitAction)
        #exitAction.triggered.connect(self.exit)

        # adding the goal menu options
        howtToPlayAction = QAction(QIcon("./images/howto.png"), "How to Play", self)
        howtToPlayAction.setShortcut("Ctrl+H")
        goalMenu.addAction(howtToPlayAction)
        playAction.triggered.connect(self.howToPlay)

        goalAction = QAction(QIcon("./images/goal.png"), "Goal", self)
        goalAction.setShortcut("Ctrl+G")
        goalMenu.addAction(goalAction)
        goalAction.triggered.connect(self.goal)

        # set the how to play menu
        captureAction = QAction(QIcon("./images/howTo2.png"), "Capture", self)
        captureAction.setShortcut("Ctrl+C")
        hotToPlayMenu.addAction(captureAction)
        captureAction.triggered.connect(self.capture)

        defendAction = QAction(QIcon("./images/defend.png"), "Defend yourself", self)
        defendAction.setShortcut("Ctrl+D")
        hotToPlayMenu.addAction(defendAction)
        defendAction.triggered.connect(self.defend)

        endGameAction = QAction(QIcon("./images/end.png"), "End Game", self)
        endGameAction.setShortcut("Ctrl+E")
        hotToPlayMenu.addAction(endGameAction)
        endGameAction.triggered.connect(self.endGame)

        # set the rules menu
        sekiAction = QAction(QIcon("./images/seki.png"), "Seki Rule", self)
        sekiAction.setShortcut("Ctrl+S")
        rulesMenu.addAction(sekiAction)
        sekiAction.triggered.connect(self.sekiRule)

        koAction = QAction(QIcon("./images/ko.png"), "Ko Rule", self)
        koAction.setShortcut("Ctrl+K")
        rulesMenu.addAction(koAction)
        koAction.triggered.connect(self.koRule)

        suicideAction = QAction(QIcon("./images/suicide.png"), "Suicide Rule", self)
        suicideAction.setShortcut("Ctrl+R")
        rulesMenu.addAction(suicideAction)
        suicideAction.triggered.connect(self.suicideRule)

    #def play(self):
     #   ""

    #def exit(self):
     #   ""

    def howToPlay(self):
        QMessageBox.about(self, "How To Play", "Click on one of the junctions on the board to place a stone. \n"
                                                 "Capture as many opponent's stones as you can to expand your territory. \n"
                                                 "The more territory you have or stones you capture, the more points you will have. \n"
                                                 "You can pass if you can't or don't want to place a stone in your turn. \n"
                                                 "If there are two consecutive passes, the game is over. \n"
                                                 "Wins the one who has more points.")

    def goal(self):
        QMessageBox.about(self, 'Go objective', 'The goal of the game Go is to win as much territory as you can\n'
                                                'and get more points by capturing the opponents stones.')

    def capture(self):
        QMessageBox.about(self, "Capture", "You can capture stones which has liberty spots around then by surrounding them with your stones.")

    def defend(self):
        QMessageBox.about(self, "Defend yourself", "You can defend your stones by creating two eyes to keep your group alive")

    def endGame(self):
        QMessageBox.about(self, "End Game", "The game ends when there are no more good moves to make.\n"
                                        "In order to actually end the game both players must pass their turns.\n"
                                        "Thus the game is finished.")

    def sekiRule(self):
        QMessageBox.about(self, "Seki Rule", "The Seki rule states that you may not be able to capture\n"
                                                   "any stone but you can prevent from being captured.")

    def koRule(self):
        QMessageBox.about(self, "Ko Rule", "The Ko rule states that in order to prevent endlessly \n"
                                                 "re-capturing the same space, it is not allowed to \n"
                                                 "immediately recapture the same position")

    def suicideRule(self):
            QMessageBox.about(self, "Suicide Rule", "The Suicide rule states that you can not place a stone \n"
                                               "if it will immediately have not liberty")

    def getBoard(self):
        return self.board

    def getScoreBoard(self):
        return self.scoreBoard

    def initUI(self):
        '''initiates application UI'''
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.scoreBoard = ScoreBoard()
        self.addDockWidget(Qt.RightDockWidgetArea, self.scoreBoard)
        self.scoreBoard.make_connection(self.board)

        #self.setStyleSheet("MainWindow {background-image:url(:./image/goboard7x7.png)}")
        #bkgnd = QPixmap("./image/goboard7x7.png")
        #sImage = bkgnd.scaled(QSize(100,100))                   # resize Image to widgets size
        #palette = QPalette()
        #palette.setBrush(QPalette.Background, QBrush(sImage))
        #self.setPalette(palette)


        self.resize(800, 800)
        self.center()
        self.setWindowTitle('Go')
        self.show()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)
