# Import Packages
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# Import Modules
from UI.Main_Window_UI import Ui_Form
from Crawler.crawler import Crawler
from Crawler.DB import DB
from UI.Table_view import Table_view


# URL of the webpage that we are scraping information from
BASE_URL = "https://www.esky.bg/oferti/co/bg/0/0/balgariya"


class Main_Window(qtw.QMainWindow, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Ui_Form.__init__(self)

        self.setupUi(self)

        # Set Title and Icon
        self.setWindowTitle("SkyScanner")
        self.setWindowIcon(qtg.QIcon("./assets/Images/img.png"))

        # Set fixed window size
        self.setFixedSize(786, 654)

        # Make click connections
        self.btnRunCrawler.clicked.connect(self.onBtnRunCrawlerClick)
        self.btnShowData.clicked.connect(self.onBtnShowDataClick)

        self.show()

    @qtc.pyqtSlot(bool)
    def onBtnRunCrawlerClick(self):
        # Scrape through the website
        crawler = Crawler(BASE_URL)
        crawler.start()
        crawler_info = crawler.info
        crawler.stop()

        # Delete old table and make new with new data
        self.db = DB()
        self.db.remove_table()
        self.db.create_table()

        # Insert information into db
        self.db.intert_rows(offers=crawler_info)

        # Open Table View
        self.onBtnShowDataClick()
        self.close()

    @qtc.pyqtSlot(bool)
    def onBtnShowDataClick(self):
        self.table_view = Table_view()
        self.table_view.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = Main_Window()

    sys.exit(app.exec())
