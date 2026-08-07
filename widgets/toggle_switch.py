from PyQt5.QtCore import (
    Qt,
    QSize,
    QRectF,
    pyqtProperty,
    QPropertyAnimation
)
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QCheckBox


class ToggleSwitch(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(50, 28)

        self._offset = 3

        self._animation = QPropertyAnimation(self, b"offset")
        self._animation.setDuration(180)

        self.toggled.connect(self.animate)

    def sizeHint(self):
        return QSize(50, 28)

    # ---------- 애니메이션 ----------
    def animate(self, checked):
        self._animation.stop()

        if checked:
            self._animation.setStartValue(3)
            self._animation.setEndValue(25)
        else:
            self._animation.setStartValue(25)
            self._animation.setEndValue(3)

        self._animation.start()

    # ---------- Property ----------
    def getOffset(self):
        return self._offset

    def setOffset(self, value):
        self._offset = value
        self.update()

    offset = pyqtProperty(float, getOffset, setOffset)

    # ---------- 그림 ----------
    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 배경
        if self.isChecked():
            background = QColor("#5B8DEF")
        else:
            background = QColor("#D8D8D8")

        painter.setPen(Qt.NoPen)
        painter.setBrush(background)
        painter.drawRoundedRect(QRectF(0, 0, 50, 28), 14, 14)

        # 동그라미
        painter.setBrush(QColor("#FFFFFF"))
        painter.drawEllipse(QRectF(self._offset, 3, 22, 22))