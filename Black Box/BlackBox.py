import sys, random

from PyQt6.QtCore import pyqtSignal, QSize, QRect, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QSizePolicy, QWidget, QGridLayout, QApplication, QFrame, QDialog, QVBoxLayout


class QLabelGridSquare(QLabel):
    submit_final_guess = pyqtSignal(list)
    probe = pyqtSignal(int)
    guessed = [[False for _ in range(10)] for _ in range(10)]
    count = 0

    def __init__(self, parent=None, num_label=False, position: tuple = (0, 0), num=1):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        self.num_label = num_label
        if self.num_label:
            self.setText(str(num))
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            self.position = position
            self.setScaledContents(True)

    def mousePressEvent(self, ev):
        if self.num_label:
            try:
                self.probe.emit(int(self.text()))
            except:
                pass
        else:
            row, col = self.position
            if QLabelGridSquare.guessed[row][col]:
                QLabelGridSquare.guessed[row][col] = False
                QLabelGridSquare.count -= 1
                self.setPixmap(QPixmap())
            else:
                if QLabelGridSquare.count >= 4:
                    return
                QLabelGridSquare.guessed[row][col] = True
                QLabelGridSquare.count += 1
                pic = QPixmap("ball.png")
                self.setPixmap(pic)
                if QLabelGridSquare.count == 4:
                    self.submit_final_guess.emit(QLabelGridSquare.guessed)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.my_frame = QFrame(self, objectName="my_frame")
        self.label = QLabel()
        self.grid_layout = QGridLayout(self.my_frame)
        self.grid_layout.setSpacing(0)
        self.grid_layout.addWidget(self.label, 10, 0, 1, 10)


        for i in range(1, 33):
            label = QLabelGridSquare(self, num_label=True, num=i)
            label.probe.connect(self.probe)
            [[row, col], _] = self.getPositionFromNum(i)
            self.grid_layout.addWidget(label, row, col)

        for row in range(8):
            for col in range(8):
                label = QLabelGridSquare(self, position=(row, col))
                self.grid_layout.addWidget(label, row+1, col+1, 1, 1)
                label.submit_final_guess.connect(self.checkSolution)

        self.solution = [[False for _ in range(8)] for _ in range(8)]
        for _ in range(4):
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            while self.solution[row][col]:
                row = random.randint(0, 7)
                col = random.randint(0, 7)
            self.solution[row][col] = True

    def getPositionFromNum(self, i: int):
        if i <= 8:
            return [[i, 0], [0, 1]]
        elif i <= 16:
            return [[9, i - 8], [-1, 0]]
        elif i <= 24:
            return [[25 - i, 9], [0, -1]]
        else:
            return [[0, 33 - i], [1, 0]]

    def resizeEvent(self, event):
        super().resizeEvent(event)

        l = min(self.width(), self.height())
        center = self.rect().center()

        rect = QRect(0, 0, int(l*10/11), l)
        rect.moveCenter(center)
        self.my_frame.setGeometry(rect)

    def checkSolution(self, guessed):
        check = [[entry1 == entry2 for entry1, entry2 in zip(row1, row2)] for row1, row2 in zip(self.solution, guessed)]
        if not any(False in row for row in check):
            self.label.setText("You Win")
        else:
            self.label.setText("That is incorrect, keep trying")

    def probe(self, i: int):
        position, direction = self.getPositionFromNum(i)
        initial_position = position.copy()
        while True:
            try:
                if self.solution[position[0] + direction[0] - 1][position[1] + direction[1] - 1]:
                    self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().setText(self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text() + " - *")
                    self.label.setText("That Ray Got Absorbed")
                    break
            except:
                pass

            initial_direction = direction.copy()
            try:
                if self.solution[position[0]-1 + (initial_direction[0] if initial_direction[0] != 0 else 1)][position[1]-1 + (initial_direction[1] if initial_direction[1] != 0 else 1)]:
                    if position == initial_position:
                        self.label.setText(f"That Ray cam out at {self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text()}")
                        self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().setText(self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text() + " - "  + self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text())
                        break
                    else:
                        direction = [direction[0] - (initial_direction[0] if initial_direction[0] != 0 else 1), direction[1] - (initial_direction[1] if initial_direction[1] != 0 else 1)]
            except:
                pass

            try:
                if self.solution[position[0]-1 + (initial_direction[0] if initial_direction[0] != 0 else -1)][position[1]-1 + (initial_direction[1] if initial_direction[1] != 0 else -1)]:
                    if position == initial_position:
                        self.label.setText(f"That Ray cam out at {self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text()}")
                        self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().setText(self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text() + " - "  + self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text())
                        break
                    else:
                        direction = [direction[0] - (initial_direction[0] if initial_direction[0] != 0 else -1), direction[1] - (initial_direction[1] if initial_direction[1] != 0 else -1)]
            except:
                pass

            position = [position[0] + direction[0], position[1] + direction[1]]
            if 0 in position or 9 in position:
                last_num = self.grid_layout.itemAtPosition(position[0], position[1]).widget().text()
                self.label.setText(f"That Ray cam out at {last_num}")
                self.grid_layout.itemAtPosition(position[0], position[1]).widget().setText(self.grid_layout.itemAtPosition(position[0], position[1]).widget().text() + " - " + self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text())
                if initial_position != position:
                    self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().setText(self.grid_layout.itemAtPosition(initial_position[0], initial_position[1]).widget().text() + " - " + last_num)
                break

app = QApplication(sys.argv)
app.setStyleSheet("QLabel {background-color: white; border: 1px solid DarkSlateGray;}")
window = MyWindow()
window.show()
sys.exit(app.exec())