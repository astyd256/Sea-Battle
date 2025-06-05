import sys

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

    
# class Game (QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         # Window preferences
#         self.setWindowTitle("Морской Бой v0.1.1 pre alpha")
#         self.setFixedSize(800, 600)

#         # Initializing some parameters
#         self.player_ships = [4, 3, 2, 1]
#         self.enemy_ships = [[0 for i in range(10)] for j in range(10)]
#         self.player_grid = {}
#         self.enemy_grid = {}
#         self.player_turn = False

#         for y in range(10):
#             for x in range(10):
#                 self.player_grid[(y, x)] = QtWidgets.QPushButton('', self)
#                 self.player_grid[(y, x)].setGeometry(10, 10, 20, 20)
#                 self.player_grid[(y, x)].move(60 + y * 30, 40 + x * 30)
#                 self.player_grid[(y, x)].setStyleSheet("background-color: cyan")

#                 self.enemy_grid[(y, x)] = QtWidgets.QPushButton('', self)
#                 self.enemy_grid[(y, x)].setGeometry(10, 10, 20, 20)
#                 self.enemy_grid[(y, x)].move(440 + y * 30, 40 + x * 30)
#                 self.enemy_grid[(y, x)].setStyleSheet("background-color: cyan")
#                 self.enemy_grid[(y, x)].setDisabled(True)

#                 self.player_grid[(y, x)].clicked.connect(self.player_click)
#                 self.enemy_grid[(y, x)].clicked.connect(self.enemy_click)

#         # Clear button
#         self.clear_button = QtWidgets.QPushButton('&Clear', self)
#         self.clear_button.clicked.connect(self.clear)
#         self.clear_button.move(350, 400)

#         # Start button
#         self.start_button = QtWidgets.QPushButton('&Start', self)
#         self.start_button.clicked.connect(self.start)
#         self.start_button.move(350, 440)

#     def player_click(self):
#         """Handler of creating player’s grid"""
#         # Need to add a layout probably to scale buttons but unknown
#         # how to get a name from buttons after that change

#         # Taking back name of a button
#         # and translate it by fixed formula
#         y = (int(self.sender().y()) - 40)//30
#         x = (int(self.sender().x()) - 60)//30

#         if self.player_grid[abs(y - 1), abs(x - 1)].styleSheet() == "background-color: red":
#             return
#         if y < 9 and x < 9 and self.player_grid[(y + 1, x + 1)].styleSheet() == "background-color: red":
#             return
#         if y < 9 and self.player_grid[(y + 1, abs(x - 1))].styleSheet() == "background-color: red":
#             return
#         if x < 9 and self.player_grid[(abs(y - 1), x + 1)].styleSheet() == "background-color: red":
#             return
#         self.player_ships = [[0]*10]*10
#         self.enemy_ships = [[0]*10]*10
#         self.ships_stack = [4, 3, 2, 1]
#         self.player_turn = False
#         self.x = None
#         self.y = None

#     def ship_placer(self, y, x):
#         # TODO: synchronise UI and Game
#         # TODO: Add a log to display exception error
#         """
#         Handler of creating player’s grid

#         :return 0: square is empty
#         :return 1: square is reserved
#         """

#         if self.player_ships[y][x] == 1:
#             return False

#         # Counter of adjacent red squares
#         # k - temp parameter
#         k = y - 1
#         counter = 0
#         while k > -1 and self.player_ships[k][x] == 1:
#             counter += 1
#             k -= 1
#         k = x - 1
#         while k > -1 and self.player_ships[y][k] == 1:
#             counter += 1
#             k -= 1
#         k = y + 1
#         while k < 10 and self.player_ships[k][x] == 1:
#             counter += 1
#             k += 1
#         k = x + 1
#         while k < 10 and self.player_ships[y][k] == 1:
#             counter += 1
#             k += 1

#         '''
#         Checks if there is an active squire or not
#         If it's not, place the square and change counter
#         If it's, disable this square and change counter
#         '''
#         adjacent = 0
#         if self.player_ships[y][x] == 0:
#             if self.ships_stack[counter] > 0:
#                 if counter > 0:
#                     self.ships_stack[counter - 1] += 1
#                     self.ships_stack[counter] -= 1
#                 elif counter == 0:
#                     self.ships_stack[counter] -= 1
#                 self.player_ships[y][x] = 1
#                 return 1
#         else:
#             for j in [y + 1, y - 1]:
#                 for i in [x + 1, x - 1]:
#                     if -1 < y < 10 and -1 < x < 10 and self.player_ships[j][i] == 1:
#                         adjacent += 1
#             if adjacent > 1:
#                 return 0
#             if counter == 0:
#                 self.ships_stack[counter] += 1
#                 self.player_ships[y][x] = 0
#                 return 0
#             elif counter > 0:
#                 if self.ships_stack[counter - 1] == 0:
#                     return 0
#                 elif self.ships_stack[counter - 1] > 0:
#                     self.ships_stack[counter - 1] -= 1
#                     self.ships_stack[counter] += 1
#                     self.player_ships[y][x] = 0
#                     return 0

#     def enemy_click(self):
#         """
#         Handler of player’s clicks on enemy grid
#         """
#         # TODO: Create handler
#         btn = self.sender()
#         btn.setDisabled(True)

#     def clear(self):
#         """
#         Clear button
#         """
#         for y in range(10):
#             for x in range(10):
#                 self.player_grid[(y, x)].setStyleSheet("background-color: cyan")
#                 self.player_grid[(y, x)].setDisabled(False)
#         self.player_ships = [4, 3, 2, 1]

#     def start(self):
#         """
#         Start button
#         """
#         self.generate_enemy_map()   
#         self.clear_button.setDisabled(True)
#         self.start_button.setDisabled(True)
#         for i in range(10):
#             for j in range(10):
#                 self.player_grid[(i, j)].setDisabled(True)
#         self.game_loop()
#         self.player_turn = True

#     def generate_enemy_map(self):
#         """
#         Generates random enemy ships
#         and write them down in self.enemy_ships
#         """
#         enemy_ships = 10
#         square_shift = 3
#         while enemy_ships > 0:
#             available_ships = []
#             # OX
#             for j in range(10):
#                 for i in range(10 - square_shift):
#                     iterator = 0
#                     while iterator <= square_shift and self.enemy_ships[j][i + iterator] == 0:
#                         if iterator == square_shift:
#                             available_ships.append([(temp, j) for temp in range(i, i + square_shift + 1)])
#                         iterator += 1
#             # OY
#             for i in range(10):
#                 for j in range(10 - square_shift):
#                     iterator = 0
#                     while iterator <= square_shift and self.enemy_ships[j + iterator][i] == 0:
#                         if iterator == square_shift:
#                             available_ships.append([(i, temp) for temp in range(j, j + square_shift + 1)])
#                         iterator += 1

#             # Take one random list with coordinates
#             # and iterate through it
#             for coordinate in random.choice(available_ships):
#                 x, y = coordinate
#                 self.enemy_ships[y][x] = 1
#                 for j in (y - 1, y, y + 1):
#                     if -1 < j < 10:
#                         for i in (x - 1, x, x + 1):
#                             if -1 < i < 10:
#                                 if self.enemy_ships[j][i] == 0:
#                                     self.enemy_ships[j][i] = 2

#             enemy_ships -= 1
#             if enemy_ships in (9, 7, 4):
#                 square_shift -= 1

#     def game_loop(self):
#         # TODO: Create game loop
#         pass


#     def enemy_turn(self):
#         # TODO: Create enemy turn handler
#         pass


# class MainWindow (QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Window preferences
#         self.setWindowTitle("Морской Бой v0.2.0a")

#         self.menu_init()
#         self.player_button = {}
#         self.enemy_button = {}

#         self.game = None

# """
#         self.main_frame = QtWidgets.QFrame()
#         self.menu_frame = QtWidgets.QFrame()
#         self.game_frame = QtWidgets.QFrame()
#         self.player_frame = QtWidgets.QFrame()
#         self.enemy_frame = QtWidgets.QFrame()
#         self.info_frame = QtWidgets.QFrame()

#         self.main_layout = QtWidgets.QVBoxLayout(self.main_frame)
#         self.menu_layout = QtWidgets.QVBoxLayout(self.menu_frame)
#         self.game_layout = QtWidgets.QHBoxLayout(self.game_frame)
#         self.player_layout = QtWidgets.QGridLayout(self.player_frame)
#         self.enemy_layout = QtWidgets.QGridLayout(self.enemy_frame)
#         self.info_layout = QtWidgets.QGridLayout(self.info_frame)

#         self.start_button = QtWidgets.QPushButton('Start Game')
#         self.start_button.clicked.connect(self.start)
#         self.fullscreen_button = QtWidgets.QPushButton('Enable Fullscreen')
#         self.fullscreen_button.clicked.connect(self.fullscreen)

#         for y in range(10):
#             for x in range(10):

#                 self.player_button[(y, x)] = QtWidgets.QPushButton(f'{y}{x}')
#                 self.player_button[(y, x)].clicked.connect(lambda: self.player_click(y, x))
#                 self.player_layout.addWidget(self.player_button[(y, x)], y, x)

#                 self.enemy_button[(y, x)] = QtWidgets.QPushButton(f'{y}{x}')
#                 self.enemy_button[(y, x)].clicked.connect(lambda: self.enemy_click(y, x))
#                 self.enemy_layout.addWidget(self.enemy_button[(y, x)], y, x)

#         self.game_init()
# """

#     def menu_init(self):

#         self.setCentralWidget(self.main_frame)
#         self.main_layout.addWidget(self.menu_frame)
#         self.main_layout.addWidget(self.game_frame)

#         self.menu_layout.addWidget(self.start_button)
#         self.menu_layout.addWidget(self.fullscreen_button)

#         self.game_layout.addWidget(self.player_frame, 1)
#         self.game_layout.addWidget(self.info_frame, 3)
#         self.game_layout.addWidget(self.enemy_frame, 1)
#         self.game_frame.setVisible(False)

#     def game_init(self):



#     def fullscreen(self):
#         if self.isFullScreen():
#             self.showNormal()
#         else:
#             self.showFullScreen()

#     def player_click(self, y, x):
#         pass

#     def enemy_turn(self):
#         # TODO: Create enemy turn handler
#         pass


# # Create the Qt Application
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Game = Game()

#     Game.show()
#     app.exec_()
#     sys.exit(0)
