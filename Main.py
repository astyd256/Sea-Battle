import sys

from PySide2 import QtWidgets

LARGE = 1
BIG = 2
MEDIUM = 3
SMALL = 4
TURNS = 0


class Game (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Window preferences
        self.setWindowTitle("Морской Бой v0.0.4 pre alpha")
        self.setFixedSize(800, 600)

        # Creating battle grid
        self.player_grid = {}
        self.enemy_grid = {}
        self.grid_create()

        # Clear button
        self.clear_button = QtWidgets.QPushButton('&Clear', self)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.move(350, 400)

        # Start button
        self.start_button = QtWidgets.QPushButton('&Start', self)
        self.start_button.clicked.connect(self.start)
        self.start_button.move(350, 440)

    def grid_create(self):
        for i in range(10):
            for j in range(10):
                self.player_grid[(i, j)] = QtWidgets.QPushButton('', self)
                self.player_grid[(i, j)].setGeometry(10, 10, 20, 20)
                self.player_grid[(i, j)].move(60+j*30, 40+i*30)
                self.player_grid[(i, j)].setStyleSheet("background-color: cyan")

                self.enemy_grid[(i, j)] = QtWidgets.QPushButton('', self)
                self.enemy_grid[(i, j)].setGeometry(10, 10, 20, 20)
                self.enemy_grid[(i, j)].move(440 + j * 30, 40 + i * 30)
                self.enemy_grid[(i, j)].setStyleSheet("background-color: cyan")
                self.enemy_grid[(i, j)].setDisabled(True)

                self.player_grid[(i, j)].clicked.connect(self.player_click)
                self.enemy_grid[(i, j)].clicked.connect(self.enemy_click)

    def player_click(self):
        # Taking back name of a button
        i = (int(self.sender().y()) - 40)/30
        j = (int(self.sender().x()) - 60)/30
        # TODO: fix player grid
        if self.player_grid[(i, j)].styleSheet() == "background-color: cyan":
            self.player_grid[(i, j)].setStyleSheet("background-color: red")

            self.player_grid[(abs(i - 1), abs(j - 1))].setDisabled(True)

            if abs(i + 1) < 10:
                self.player_grid[(i + 1, abs(j - 1))].setDisabled(True)
            if abs(j + 1) < 10:
                self.player_grid[(abs(i - 1), j + 1)].setDisabled(True)
            if abs(i + 1) < 10 and abs(j + 1) < 10:
                self.player_grid[(i + 1, j + 1)].setDisabled(True)

            """Debug part"""
            self.player_grid[(abs(i - 1), abs(j - 1))].setStyleSheet("background-color: gray")

            if abs(i+1) < 10:
                self.player_grid[(i + 1, abs(j - 1))].setStyleSheet("background-color: gray")
            if abs(j+1) < 10:
                self.player_grid[(abs(i - 1), j + 1)].setStyleSheet("background-color: gray")
            if abs(i+1) < 10 and abs(j+1) < 10:
                self.player_grid[(i + 1, j + 1)].setStyleSheet("background-color: gray")
        else:
            self.player_grid[(i, j)].setStyleSheet("background-color: cyan")

            self.player_grid[(abs(i - 1), abs(j - 1))].setDisabled(False)

            if abs(i + 1) < 10:
                self.player_grid[(i + 1, abs(j - 1))].setDisabled(False)
            if abs(j + 1) < 10:
                self.player_grid[(abs(i - 1), j + 1)].setDisabled(False)
            if abs(i + 1) < 10 and abs(j + 1) < 10:
                self.player_grid[(i + 1, j + 1)].setDisabled(False)

            """Debug part"""
            self.player_grid[(abs(i - 1), abs(j - 1))].setStyleSheet("background-color: cyan")

            if abs(i + 1) < 10:
                self.player_grid[(i + 1, abs(j - 1))].setStyleSheet("background-color: cyan")
            if abs(j + 1) < 10:
                self.player_grid[(abs(i - 1), j + 1)].setStyleSheet("background-color: cyan")
            if abs(i + 1) < 10 and abs(j + 1) < 10:
                self.player_grid[(i + 1, j + 1)].setStyleSheet("background-color: cyan")

    def enemy_click(self):
        btn = self.sender()

        btn.setStyleSheet("background-color: red")
        btn.setDisabled(True)

    def clear(self):
        global LARGE, BIG, MEDIUM, SMALL
        LARGE = 1
        BIG = 2
        MEDIUM = 3
        SMALL = 4
        for i in range(10):
            for j in range(10):
                self.player_grid[(i, j)].setStyleSheet("background-color: cyan")
                self.player_grid[(i, j)].setDisabled(False)

    def start(self):
        self.generate_enemy()
        self.game_loop()
        self.clear_button.setDisabled(True)
        self.start_button.setDisabled(True)
        for i in range(10):
            for j in range(10):
                self.player_grid[(i, j)].setDisabled(True)
        global TURNS
        TURNS = 1

    def generate_enemy(self):
        # TODO: Create enemy generation
        pass

    def game_loop(self):
        # TODO: Create game loop
        while LARGE + BIG + MEDIUM + SMALL > 0:
            pass


# Create the Qt Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Game = Game()

    Game.show()
    app.exec_()
    sys.exit(0)
