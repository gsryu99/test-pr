'''
# ch 4.2.1 main.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,     # 애플르케이션 핸들러와 빈 GUI 위젯
                             QPushButton, QVBoxLayout, QMessageBox,  # QMessageBox : 메시지 박스 위젯
                             QPlainTextEdit,            # QPlainTextEdit 추가
                             QHBoxLayout)               # QHBoxLayout 추가

from PyQt5.QtGui import QIcon                           # icon을 추가하기 위한 라이브러리

class Calculator(QWidget):      # QWidget 클래스를 상속받아서 클래스를 정의

    def __init__(self):
        super().__init__()      # 부모 클래스 Qwidget을 초기화 
        self.initUI()           # 나머지 초기화는 initUI 함수에 정의

    def initUI(self):
        self.text1 = QPlainTextEdit()   # 텍스트 에디트 위젯 생성
        self.text1.setReadOnly(True)    # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self)    # 버튼 추가
        self.btn1.clicked.connect(self.activateMessage)     # 버튼 츨릭 시 핸들러 함수 연결

        self.btn2 = QPushButton('Clear', self)      # 버튼 2 추가
        self.btn2.clicked.connect(self.clearMessage)        # 버튼 2 핸들러 함수 연결

        hbox = QHBoxLayout()        # 수평 박스 레이아웃을 추가하고, 버튼 1, 2 추가
        hbox.addStretch(1)          # 공백
        hbox.addWidget(self.btn1)   # 버튼 1 배치
        hbox.addWidget(self.btn2)   # 버튼 2 배치

        vbox = QVBoxLayout()        # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.text1)  # 수직 레이아웃에 텍스트 에디트 추가
        vbox.addStretch(1)          # 빈공간
        # vbox.addWidget(self.btn1)   # 버튼 위치
        vbox.addLayout(hbox)        # btn1 위치에 hbox를 배치
        vbox.addStretch(1)          # 빈공간

        self.setLayout(vbox)    # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 설정
 
        self.setWindowTitle('Calculator')       # 윈도우에 표시되는 타이틀
        self.setWindowIcon(QIcon('icon.png'))   # 윈도우 아이콘 추가
        self.resize(256,256)                    # 윈도우 사이즈
        self.show()                             # 윈도우 화면이 표시되도록 호출

    def activateMessage(self):   # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        # 핸들러 함수 수정 : 메시지가 텍스트 에디터에 출력되도록 수정
        # QMessageBox.information(self, "information", "Button clicked!")
        self.text1.appendPlainText("Button clicked!")

    def clearMessage(self):     # 버튼 2 핸들러 함수 정의
        self.text1.clear()

if __name__=='__main__':            # pyqt는 애플리케이션 당 1개의 QApplication이 필요함
    app = QApplication(sys.argv)    # QApplication 인스턴스 생성
    view = Calculator()             # Calculator 윈도우 인스턴스 생성
    sys.exit(app.exec_())           # 애플리케이션이 이벤트 처리를 하도록 루프 구동
'''

# ch 5.2.1 main.py

import sys
from ui import View # ui.py의 View 클래스 추가
from ctrl import Control # ctrl.py의 Control 클래스 추가
from PyQt5.QtWidgets import QApplication

def main(): # 프로그램 실행(Application) 관련 내용 함수화
    calc = QApplication(sys.argv)
    app=QApplication(sys.argv)
    view = View() # View 인스턴스 선언
    Control(view=view) # Control 인스턴스 선언
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
