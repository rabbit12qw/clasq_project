import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from widgets.toggle_switch import ToggleSwitch
from PyQt5.QtGui import QIcon


class main(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('clasq')
        self.resize(1200, 800)
        QFontDatabase.addApplicationFont("font/Pretendard-Medium.otf")
        QFontDatabase.addApplicationFont("font/Pretendard-Regular.otf")
        QFontDatabase.addApplicationFont("font/Pretendard-SemiBold.otf")
        # font_id = QFontDatabase.addApplicationFont("font/Pretendard-Regular.otf")

        # print(QFontDatabase.applicationFontFamilies(font_id))
        
        self.center()
        self.layout() 
        with open("style.qss", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())        

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def layout(self):

        # 영역나누기
        mainLayout = QVBoxLayout()      # 전체 영역

        header = QHBoxLayout()          # 상단 영역

        option = QGroupBox('')          # 버튼 그룹
        optionlayout = QHBoxLayout()    # 버튼 배치용 레이아웃

        middlelayout = QHBoxLayout()          # 중간 영역

        # 테이블 영역
        tablebox = QGroupBox('')          # 테이블 그룹
        tablebox.setObjectName("tablebox")
        tablelayout = QVBoxLayout()  # 테이블 배치용 레이아웃
        btnlayout = QHBoxLayout()  # 버튼 배치용 레이아웃

        # 상단요소
        backbtn = QPushButton(' 메인화면')
        backbtn.setIcon(QIcon('icons/back2.svg'))
        backbtn.setObjectName("backbtn")
        title = QLabel('파일경로 지정')
        title.setObjectName("title")

        # 중간영역 버튼들
        savebtn = QPushButton('프리셋 저장하기')
        reloadbtn = QPushButton('프리셋 불러오기')
        togleName = QLabel('자동')
        toggle = ToggleSwitch()
        
        togleName.setObjectName("toglename")
        clearbtn = QPushButton('정리하기')

        addRoot = QPushButton('경로추가')
        addRoot.setObjectName("addRoot")
        addRoot.setIcon(QIcon('icons/add.svg'))



        # 테이블영역
        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["선택", "번호","폴더이름","파일경로"])
        table.verticalHeader().setVisible(False)
        table.setSelectionMode(QAbstractItemView.NoSelection)
        for row in range(3):
            checkbox = QCheckBox()

    # 체크박스를 가운데 배치할 레이아웃

            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            table.setCellWidget(row, 0, widget)
            numItem = QTableWidgetItem(str(row + 1))
            numItem.setTextAlignment(Qt.AlignCenter)
            table.setItem(row, 1, numItem)
            table.setItem(row, 2, QTableWidgetItem("폴더이름")) #폴더명 세팅
            table.setItem(row, 3, QTableWidgetItem("파일경로")) #경로 세팅
        
        tableheader = table.horizontalHeader()
        table.setColumnWidth(0, 50)
        table.setColumnWidth(1, 60)
        tableheader.setSectionResizeMode(0, QHeaderView.Fixed)
        tableheader.setSectionResizeMode(1, QHeaderView.Fixed)
        tableheader.setSectionResizeMode(2, QHeaderView.Stretch)
        tableheader.setSectionResizeMode(3, QHeaderView.Stretch)

        # 헤더요소 배치
        header.addWidget(title)
        header.addStretch()
        header.addWidget(backbtn)

        # 버튼 그룹 배치
        optionlayout.addWidget(savebtn)
        optionlayout.addWidget(reloadbtn)
        optionlayout.addStretch()
        optionlayout.addWidget(togleName)
        optionlayout.addWidget(toggle)
        optionlayout.addWidget(clearbtn)

        option.setLayout(optionlayout)

        
        



        # 테이블 배치
        btnlayout.addStretch()
        btnlayout.addWidget(addRoot)
        tablelayout.addLayout(btnlayout)
        tablelayout.addWidget(table)
        tablebox.setLayout(tablelayout)

        # 메인 레이아웃
        mainLayout.addLayout(header)
        mainLayout.addWidget(option)
        mainLayout.addLayout(middlelayout)
        mainLayout.addWidget(tablebox, 1)

        

        # 메인 레이아웃 적용
        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())