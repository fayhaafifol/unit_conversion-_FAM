import PyQt5.QtWidgets as qtw

from PyQt5.QtWidgets import QMainWindow, QApplication

from unit_converter.converter import convert, converts

from UC_design import Ui_MainWindow

class MainWindow(qtw.QMainWindow,Ui_MainWindow):

    def __init__(self):

        super().__init__()

        self.setupUi(self)

        global length_list ,mass_list , temp_list,time_list,freq_list,speed_list

        length_list=["m","mile","yard","inch","foot","mm","µm","cm","dm","km"]
        mass_list=["g","kg","mg","µg","ng","pg"]
        temp_list=["°C","°F","K"]
        time_list=["s","h","min"]
        freq_list=["kHz","MHz","GHz","Hz"]
        speed_list=["mile*h^-1","km*h^-1","foot*s^-1","m*s^-1"]

        self.FC.activated.connect(lambda:self.conversion())
        self.TC.activated.connect(lambda:self.conversion())

        self.check()
        self.shows() 



    def conversion (self):

        fc =self.FC.currentText()

        tc =self.TC.currentText()

        inp = self.Input.text()

        conv = convert(f'{inp}{fc}',tc)
        self.Output.setText(str(conv))
 

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

        elif "    Time( ' o ' )"==self.MC.currentText():
            
            self.FC.clear()
            self.TC.clear()
            self.FC.insertItems(0, time_list)
            self.TC.insertItems(0,time_list)  

        elif "    Frequency(OwO)"==self.MC.currentText():
            
            self.FC.clear()
            self.TC.clear()
            self.FC.insertItems(0,freq_list)
            self.TC.insertItems(0,freq_list) 

        elif "    Speed(- u -)"==self.MC.currentText():
            
            self.FC.clear()
            self.TC.clear()
            self.FC.insertItems(0, speed_list)
            self.TC.insertItems(0,speed_list)  

    def check(self):

        self.index= self.MC.currentIndex()
        self.MC.activated.connect(self.shows)
    
        
                   
     

app=qtw.QApplication([])
win=MainWindow()
win.show()
app.exec()