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

    



    


   

    
   