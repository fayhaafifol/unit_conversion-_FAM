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


=======
#write your code here ('u')
from unit_converter.converter import convert, converts
from UC_design import Ui_MainWindow
import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global length_list ,mass_list , temp_list
        length_list=["m","ml","yd","in","ft","mm","µm","cm","dm","km"]
        mass_list=["g","kg","mg","µg","ng","pg"]
        temp_list=["°C","°F"]
        self.check()
        self.shows()            

    

    def shows(self):
       
        if "    Length ('u')"==self.MC.currentText() :
            self.FC.clear()
            self.TC.clear()
            self.FC.insertItems(0, length_list)
            self.TC.insertItems(0,length_list)
        

        
        elif "    Mass (^w^)"==self.MC.currentText():
            
            self.FC.clear()
            self.TC.clear()
            self.FC.insertItems(0, mass_list)
            self.TC.insertItems(0,mass_list)
            
        elif "    Temprature (>u<)"==self.MC.currentText():
            
            self.FC.clear()
            self.TC.clear()
            self.FC.insertItems(0, temp_list)
            self.TC.insertItems(0,temp_list)    
            
    def check(self):
        self.index= self.MC.currentIndex()
        self.MC.activated.connect(self.shows)
        
                   
            

app=qtw.QApplication([])
win=MainWindow()


win.show()


    
app.exec()