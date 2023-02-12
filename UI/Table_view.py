import sys
import re

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from UI.Table_view_ui import Table_Ui_Form
from Crawler.DB import DB


class Table_view(qtw.QWidget, Table_Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        # Set Title and Icon
        self.setWindowTitle("Offers")
        self.setWindowIcon(qtg.QIcon("./assets/Images/img.png"))

        # Set fixed window size
        self.setFixedSize(979, 814)

        # Call functions for Table setting and their filtering
        self.table_settings()
        self.filters()

        self.show()

    def table_settings(self):
        # Connect with database
        self.table.db = DB()

        # Get all the data from the database
        self.table.data = self.table.db.select_offers()

        # Get the column headers
        self.column_headers = ["ID", "Country", "City", "Price €"]

        model = self.model()

        # Create a sort and filter by default proxy model
        self.filter_proxy_model = qtc.QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(model)
        self.filter_proxy_model.setFilterCaseSensitivity(
            qtc.Qt.CaseSensitivity.CaseInsensitive
        )
        self.filter_proxy_model.setFilterKeyColumn(1)

        # Set the model for the table view
        self.table.setModel(self.filter_proxy_model)

        # Get rows and columns count
        rows_count = self.table.model().rowCount()
        column_count = self.table.model().columnCount()

        # Set minimum width and height
        self.table.setMinimumWidth(column_count * 200)
        self.table.setMinimumHeight(rows_count * 40)

        # Make Headers strechable
        self.table.horizontalHeader().setStretchLastSection(True)

        # Set column widths
        self.table.setColumnWidth(0, 0)
        self.table.setColumnWidth(1, 350)
        self.table.setColumnWidth(2, 350)

        # Hide id column
        self.table.setColumnHidden(0, True)

        # Add scrollbar and initialize its settings
        self.scroll = qtw.QScrollArea(self)
        self.scroll.setGeometry(10, 130, 959, 650)
        self.scroll.setWidget(self.table)
        self.scroll.setVerticalScrollBarPolicy(qtc.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)


    def model(self):
        ### Set a data model
        model = qtg.QStandardItemModel()

        # Set headers label for columns
        model.setHorizontalHeaderLabels(self.column_headers)

        # Loop through each row in the table data
        for i, row in enumerate(self.table.data):
            items = []
            # Loop through each field in the row
            for field in row:
                # Catch integer fields
                if isinstance(field, int):
                    item = qtg.QStandardItem()
                    item.setData(field, qtc.Qt.ItemDataRole.DisplayRole)
                # Catch prices
                else:
                    price = re.search(r"\d+", field)
                    if price:
                        item = qtg.QStandardItem()
                        item.setData(
                            int(price.group()), qtc.Qt.ItemDataRole.DisplayRole
                        )
                    # Catch other fields
                    else:
                        item = qtg.QStandardItem(str(field))

                items.append(item)

            model.insertRow(i, items)

        return model

    def filters(self):
        # Filter by Country
        self.leCountry.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

        # Filter by combobox
        self.filtercombobox.currentIndexChanged.connect(self.filter_by_combobox)

    def filter_by_combobox(self, index):
        if index == 0:
            self.filter_proxy_model.sort(0, qtc.Qt.SortOrder.AscendingOrder)
        elif index == 1:
            self.filter_proxy_model.sort(3, qtc.Qt.SortOrder.AscendingOrder)
        elif index == 2:
            self.filter_proxy_model.sort(3, qtc.Qt.SortOrder.DescendingOrder)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Table_view()
    sys.exit(app.exec())
