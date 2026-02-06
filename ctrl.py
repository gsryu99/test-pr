# ch 7.5.2 ctrl.py

class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):   # calculate 메소드 추가, 내용은 추후 작성
        try:    # 숫자가 아닌 값이 입력되었을 때도 프로그램이 동작하도록 예외 처리 구문 추가
            num1 = float(self.view.le1.text())      # 첫번째 라인 에디터에 입력된 숫자를 읽어옴
            num2 = float(self.view.le2.text())      # 두번째 라인 에디터에 입력된 숫자를 읽어옴
            operator = self.view.cb.currentText()   # 콤보 박스에 선택된 연산자 확인

            if operator == '+':     # 연산자가 '+'면 덧셈 결과를 문자열로 리턴
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == '-':
                return f'{num1} + {num2} = {self.sub(num1, num2)}'
            elif operator == '*':
                return f'{num1} + {num2} = {self.mul(num1, num2)}'
            elif operator == '/':
                return f'{num1} + {num2} = {self.div(num1, num2)}'
#            elif operator == '^':
#                return f'{num1} + {num2} = {self.pow(num1, num2)}'
#            elif operator == '%':       # '%'를 입력했을 때 mod 연산 결과를 출력하도록 추가
#                return f'{num1} + {num2} = {self.mod(num1, num2)}'
            else:
                return "Calculation Error 1"
        except:
            return "Calculator Error 2"

    def connectSignals(self):
#        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn1.clicked.connect(lambda:\
                                       self.view.setDisplay(self.calculate()))     # 버튼1 연결을 변경
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):    # 덧셈 함수 추가
        return a+b
#        try:
#            return(str(a+b))
#        except:
#            return "Calculation Error 222"

    def sub(self, a, b):    # 뺄셈 함수 추가
        return a-b

    def mul(self, a, b):    # 곱셈 함수 추가
        return a*b

    def div(self, a, b):    # 나눗셈 함수 추가
        try:
            if(b == 0):
                raise Exception("Divisor Error")
        
        except Exception as e:
            return e
        
        return a/b

#    def pow(self, a, b):    # 제곱 연산 함수 추가
#        try:
#            if (a==0):
#                raise Exception("Base Error")
#            
#        except Exception as e:
#            return e
#        
#        return pow(a, b)
#
#    def mod(self, a, b):    # 나눗셈 연산의 나머지를 리턴하는 함수 추가
#        try:
#            if(b==0):
#                raise Exception("Divisor Error")
#            
#        except Exception as e:
#            return e
#        
#        return a%b
    
