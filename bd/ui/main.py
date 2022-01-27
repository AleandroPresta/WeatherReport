import sys
import platform

from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PAGES MENU
        ########################################################################

        # PAGE 1
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        # PAGE 2
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))
        # PAGE 3
        self.ui.Btn_Menu_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))
        # PAGE 3
        self.ui.Btn_Menu_4.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_4))

        # PAGES Weather Today
        ########################################################################
        self.ui.weather_table_button.clicked.connect(
            lambda: self.ui.weather_today_pages.setCurrentWidget(self.ui.weather_table_page))

        self.ui.temperature_chart_button.clicked.connect(
            lambda: self.ui.weather_today_pages.setCurrentWidget(self.ui.temperature_chart_page))

        self.ui.humidity_chart_button.clicked.connect(
            lambda: self.ui.weather_today_pages.setCurrentWidget(self.ui.humidity_chart_page))

        self.ui.wind_speed_chart_button.clicked.connect(
            lambda: self.ui.weather_today_pages.setCurrentWidget(self.ui.wind_speed_chart_page))

        self.ui.pressure_chart_button.clicked.connect(
            lambda: self.ui.weather_today_pages.setCurrentWidget(self.ui.pressure_chart_page))

        self.ui.condition_chart_button.clicked.connect(
            lambda: self.ui.weather_today_pages.setCurrentWidget(self.ui.condition_chart_page))

        # PAGES Weather Italy
        ########################################################################

        self.ui.italy_weather_table_button.clicked.connect(
            lambda: self.ui.Italy_Pages.setCurrentWidget(self.ui.italy_table_page))

        self.ui.italy_clustering_button.clicked.connect(
            lambda: self.ui.Italy_Pages.setCurrentWidget(self.ui.italy_clustering_page))

        # PAGES Weather Italy Clustering
        ########################################################################

        self.ui.pushButton.clicked.connect(
            # A causa di un errore di nomenclatura questa variabile è rimasta pushButton
            lambda: self.ui.clustering_pages.setCurrentWidget(self.ui.clustering_table_page)
        )

        self.ui.start_clustering_button.clicked.connect(
            lambda: self.ui.clustering_pages.setCurrentWidget(self.ui.clustering_chart_page)
        )

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END ##


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
