#Import Packages
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

#Import Modules
from UI.Main_Window_UI import Ui_Form


#URL of the webpage that we are scraping information from
BASE_URL="https://www.esky.bg/oferti/co/bg/0/0/balgariya"

class Main_Window(qtw.QMainWindow,Ui_Form):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        Ui_Form.__init__(self)

        self.setupUi(self)

        self.setWindowTitle("SkyScanner")
        self.setWindowIcon(qtg.QIcon("./assets/Images/8bfa5d6a52a03e83b995fec69a4d8c2c.png"))

        self.show()



if __name__ == '__main__':
    app=qtw.QApplication(sys.argv)

    window=Main_Window()

    sys.exit(app.exec())
