import sys

from PySide2 import QtWidgets
import random

class Game (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Window preferences
        self.setWindowTitle("Морской Бой v0.1.0 pre alpha")
        self.setFixedSize(800, 600)

        # Initializing some parameters
        self.player_ships = [4, 3, 2, 1]
        self.enemy_ships = [[0 for i in range(10)] for j in range(10)]
        self.player_grid = {}
        self.enemy_grid = {}

        for y in range(10):
            for x in range(10):
                self.player_grid[(y, x)] = QtWidgets.QPushButton('', self)
                self.player_grid[(y, x)].setGeometry(10, 10, 20, 20)
                self.player_grid[(y, x)].move(60 + y * 30, 40 + x * 30)
                self.player_grid[(y, x)].setStyleSheet("background-color: cyan")

                self.enemy_grid[(y, x)] = QtWidgets.QPushButton('', self)
                self.enemy_grid[(y, x)].setGeometry(10, 10, 20, 20)
                self.enemy_grid[(y, x)].move(440 + y * 30, 40 + x * 30)
                self.enemy_grid[(y, x)].setStyleSheet("background-color: cyan")
                self.enemy_grid[(y, x)].setDisabled(True)

                self.player_grid[(y, x)].clicked.connect(self.player_click)
                self.enemy_grid[(y, x)].clicked.connect(self.enemy_click)

        # Clear button
        self.clear_button = QtWidgets.QPushButton('&Clear', self)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.move(350, 400)

        # Start button
        self.start_button = QtWidgets.QPushButton('&Start', self)
        self.start_button.clicked.connect(self.start)
        self.start_button.move(350, 440)

    def player_click(self):
        """Handler of creating player’s grid"""
        # Need to add a layout probably to scale buttons but unknown
        # how to get a name from buttons after that change

        # Taking back name of a button
        # and translate it by fixed formula
        y = (int(self.sender().y()) - 40)//30
        x = (int(self.sender().x()) - 60)//30

        if self.player_grid[abs(y - 1), abs(x - 1)].styleSheet() == "background-color: red":
            return
        if y < 9 and x < 9 and self.player_grid[(y + 1, x + 1)].styleSheet() == "background-color: red":
            return
        if y < 9 and self.player_grid[(y + 1, abs(x - 1))].styleSheet() == "background-color: red":
            return
        if x < 9 and self.player_grid[(abs(y - 1), x + 1)].styleSheet() == "background-color: red":
            return

        # Counter of OTHER red squares
        k = y - 1
        counter = 0
        while k > -1 and self.player_grid[(k, x)].styleSheet() == "background-color: red":
            counter += 1
            k -= 1
        k = x - 1
        while k > -1 and self.player_grid[(y, k)].styleSheet() == "background-color: red":
            counter += 1
            k -= 1
        k = y + 1
        while k < 10 and self.player_grid[(k, x)].styleSheet() == "background-color: red":
            counter += 1
            k += 1
        k = x + 1
        while k < 10 and self.player_grid[(y, k)].styleSheet() == "background-color: red":
            counter += 1
            k += 1

        # Checks if there an active square or not
        # If not, active square and change counter
        if self.player_grid[(y, x)].styleSheet() == "background-color: cyan":
            if self.player_ships[counter] > 0:
                if counter > 0:
                    self.player_ships[counter - 1] += 1
                    self.player_ships[counter] -= 1
                elif counter == 0:
                    self.player_ships[counter] -= 1
                self.player_grid[(y, x)].setStyleSheet("background-color: red")
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
                    self.player_grid[(y, x)].setStyleSheet("background-color: cyan")
            elif counter == 0:
                self.player_ships[counter] += 1
                self.player_grid[(y, x)].setStyleSheet("background-color: cyan")

    def enemy_click(self):
        """
        Handler of player’s clicks on enemy grid
        """
        # TODO: Create handler
        btn = self.sender()
        btn.setDisabled(True)

    def clear(self):
        """
        Clear button
        """
        for y in range(10):
            for x in range(10):
                self.player_grid[(y, x)].setStyleSheet("background-color: cyan")
                self.player_grid[(y, x)].setDisabled(False)
        self.player_ships = [4, 3, 2, 1]

    def start(self):
        """
        Start button
        """
        # TODO: fix start button
        self.generate_enemy_map()   
        self.clear_button.setDisabled(True)
        self.start_button.setDisabled(True)
        for i in range(10):
            for j in range(10):
                self.player_grid[(i, j)].setDisabled(True)
        self.game_loop()

    def generate_enemy_map(self):
        """
        Generates random enemy ships
        and write them down in self.enemy_ships
        """
        # TODO: Create enemy generation
        # TODO: Create list of available squares
        enemy_ships = 10
        k = 4
        check = True
        while enemy_ships > 0:
            axis = random.choice('xy')
            y, x = random.choice([(j, i) for i in range(10) for j in range(10) if self.enemy_ships[j][i] == 0 ])
            print(x, y)
            # square checking temporary solution
            if -1 < (x * (axis == 'x') + y * (axis == 'y') + k) < 10:
                for s in range(k):
                    if self.enemy_ships[y + s * (axis == 'y')][x + s * (axis == 'x')] != 0:
                        check = False
                        break
            else:
                check = False

            if check:
                '''
                s - step
                k - number of available squares
                
                Because I know in what direction ship is building I can block the previous square.
                Even if it's out of range abs saving the day.
                Moreover it will work for any size of ship because it will either rewritten to 1
                in enemy map or be on next square after the ship.  
                '''
                for s in range(k):
                    self.enemy_ships[y + s*(axis == 'y')][x + s*(axis == 'x')] = 1
                    # TODO: make algorithm that checks neighbor squares
                    for j in (y+s*(axis == 'y') - 1, y+s*(axis == 'y'), y+s*(axis == 'y')+1):
                        if -1 < j < 10:
                            for i in (x+s*(axis == 'x') - 1, x+s*(axis == 'x'), x+s*(axis == 'x')+1):
                                if -1 < i < 10:
                                    if self.enemy_ships[j][i] == 0:
                                        self.enemy_ships[j][i] = 2

                enemy_ships -= 1
                if enemy_ships in (9, 7, 4):
                    k -= 1

            '''Debug'''
            for line in self.enemy_ships:
                print(line)

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