import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase

font_id = QFontDatabase.addApplicationFont("font/Pretendard-Regular.otf")

print(QFontDatabase.applicationFontFamilies(font_id))