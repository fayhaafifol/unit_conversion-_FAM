import PyQt5.QtWidgets as qtw

from unit_converter.converter import convert, converts

from UC_design import Ui_MainWindow

class MainWindow(qtw.QMainWindow,Ui_MainWindow):

    def __init__(self):

        super().__init__()

        self.setupUi(self)

        self.button = qtw.QPushButton()
        self.button.show()
        self.button.clicked.connect(lambda:self.conversion())


    def conversion (self):

        inp = self.Input.text()

        conv = convert(f'{inp}','kg')# replace the fc with the variable thats in the FC, and replace tc with the variable thats in TC

        self.Output.setText(str(conv))
    
    #def pic (self):

        #label_2.setPixmap(QPixmap("blob.jpeg"))
        
app = qtw.QApplication([])

win = MainWindow()

win.show()

app.exec()


