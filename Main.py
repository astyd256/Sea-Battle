import sys

from PySide2 import QtWidgets


class Game (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Window preferences
        self.setWindowTitle("Морской Бой v0.0.4 pre alpha")
        self.setFixedSize(800, 600)

        # Initializing some parameters
        self.player_ships = [4, 3, 2, 1]
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
        # Need to add a layout probably to scale buttons but unknown
        # how to get a name from buttons after that change

        # Taking back name of a button
        # and translate it by fixed formula
        i = (int(self.sender().y()) - 40)/30
        j = (int(self.sender().x()) - 60)/30

        if self.player_grid[abs(i - 1), abs(j - 1)].styleSheet() == "background-color: red":
            return
        if i < 9 and j < 9 and self.player_grid[(i + 1, j + 1)].styleSheet() == "background-color: red":
            return
        if i < 9 and self.player_grid[(i + 1, abs(j - 1))].styleSheet() == "background-color: red":
            return
        if j < 9 and self.player_grid[(abs(i - 1), j + 1)].styleSheet() == "background-color: red":
            return

        k = i - 1
        counter = 0
        while k > -1 and self.player_grid[(k, j)].styleSheet() == "background-color: red":
            counter += 1
            k -= 1
        k = j - 1
        while k > -1 and self.player_grid[(i, k)].styleSheet() == "background-color: red":
            counter += 1
            k -= 1
        k = i + 1
        while k < 10 and self.player_grid[(k, j)].styleSheet() == "background-color: red":
            counter += 1
            k += 1
        k = j + 1
        while k < 10 and self.player_grid[(i, k)].styleSheet() == "background-color: red":
            counter += 1
            k += 1

        # Checks if there an active square or not
        # If not, active square and change counter
        if self.player_grid[(i, j)].styleSheet() == "background-color: cyan":
            if self.player_ships[counter] > 0:
                if counter > 0:
                    self.player_ships[counter - 1] += 1
                    self.player_ships[counter] -= 1
                elif counter == 0:
                    self.player_ships[counter] -= 1
                self.player_grid[(i, j)].setStyleSheet("background-color: red")
        # If is disable this square and change counter
        # TODO: Add a log to display exception error
        # TODO: Fix bug when you try divide 4, 3 or 2-squared ship
        #  in half
        else:
            if counter > 0:
                if self.player_ships[counter - 1] == 0:
                    return
                elif self.player_ships[counter - 1] > 0:
                    self.player_ships[counter - 1] -= 1
                    self.player_ships[counter] += 1
                    self.player_grid[(i, j)].setStyleSheet("background-color: cyan")
            elif counter == 0:
                self.player_ships[counter] += 1
                self.player_grid[(i, j)].setStyleSheet("background-color: cyan")

    def enemy_click(self):
        btn = self.sender()

        btn.setStyleSheet("background-color: red")
        btn.setDisabled(True)

    def clear(self):
        for i in range(10):
            for j in range(10):
                self.player_grid[(i, j)].setStyleSheet("background-color: cyan")
                self.player_grid[(i, j)].setDisabled(False)

    def start(self):
        self.generate_enemy()
        self.clear_button.setDisabled(True)
        self.start_button.setDisabled(True)
        for i in range(10):
            for j in range(10):
                self.player_grid[(i, j)].setDisabled(True)
        self.game_loop()

    def generate_enemy(self):
        # TODO: Create enemy generation
        pass

    def game_loop(self):
        # TODO: Create game loop
        pass


# Create the Qt Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Game = Game()

    Game.show()
    app.exec_()
    sys.exit(0)