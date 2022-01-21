import pandas as pd
from PySide2 import QtCore, QtGui, QtWidgets
from bd.modules.web_scraping import *
from bd.modules.plotting import *
from bd.modules.preprocessing import *
from bd.modules.data_generator import *
from bd.modules.clustering import *

from functools import partial

table_on = False
clustering_on = False
df_now_italy = pd.DataFrame(columns=['DF vuoto'])


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toggle.sizePolicy().hasHeightForWidth())
        self.frame_toggle.setSizePolicy(sizePolicy)
        self.frame_toggle.setMaximumSize(QtCore.QSize(140, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Menu = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Menu.sizePolicy().hasHeightForWidth())
        self.Btn_Menu.setSizePolicy(sizePolicy)
        self.Btn_Menu.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "border: 0px solid;")
        self.Btn_Menu.setObjectName("Btn_Menu")
        self.verticalLayout_2.addWidget(self.Btn_Menu)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LineEdit_Search1 = QtWidgets.QLineEdit(self.frame_top)
        self.LineEdit_Search1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit_Search1.sizePolicy().hasHeightForWidth())
        self.LineEdit_Search1.setSizePolicy(sizePolicy)
        self.LineEdit_Search1.setMinimumSize(QtCore.QSize(500, 40))
        self.LineEdit_Search1.setMaximumSize(QtCore.QSize(600, 40))
        self.LineEdit_Search1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border: 0px solid;\n"
                                            "border-bottom: 3px solid rgb(45, 45, 45)\n"
                                            "")
        self.LineEdit_Search1.setObjectName("LineEdit_Search1")
        self.horizontalLayout_4.addWidget(self.LineEdit_Search1)
        self.Btn_Search1 = QtWidgets.QPushButton(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Search1.sizePolicy().hasHeightForWidth())
        self.Btn_Search1.setSizePolicy(sizePolicy)
        self.Btn_Search1.setMinimumSize(QtCore.QSize(40, 40))
        self.Btn_Search1.setMaximumSize(QtCore.QSize(40, 40))
        self.Btn_Search1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Btn_Search1.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(35, 35, 35);\n"
                                       "    border: 0px solid;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(45, 45, 45);\n"
                                       "}")
        self.Btn_Search1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/icons8-search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Search1.setIcon(icon)
        self.Btn_Search1.setIconSize(QtCore.QSize(32, 32))
        self.Btn_Search1.setObjectName("Btn_Search1")
        self.horizontalLayout_4.addWidget(self.Btn_Search1)
        self.loading_label = QtWidgets.QLabel(self.frame_top)
        self.loading_label.setMinimumSize(QtCore.QSize(100, 0))
        self.loading_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.loading_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.loading_label.setText("")
        self.loading_label.setObjectName("loading_label")
        self.horizontalLayout_4.addWidget(self.loading_label)
        self.horizontalLayout.addWidget(self.frame_top, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_Menu_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_1.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "}")
        self.Btn_Menu_1.setObjectName("Btn_Menu_1")
        self.verticalLayout_4.addWidget(self.Btn_Menu_1)
        self.Btn_Menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_2.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "}")
        self.Btn_Menu_2.setObjectName("Btn_Menu_2")
        self.verticalLayout_4.addWidget(self.Btn_Menu_2)
        self.Btn_Menu_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_3.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "}")
        self.Btn_Menu_3.setObjectName("Btn_Menu_3")
        self.verticalLayout_4.addWidget(self.Btn_Menu_3)
        self.Btn_Menu_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_4.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_4.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "}")
        self.Btn_Menu_4.setObjectName("Btn_Menu_4")
        self.verticalLayout_4.addWidget(self.Btn_Menu_4)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.Pages_Widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Pages_Widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Pages_Widget.setLineWidth(0)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("")
        self.page_1.setObjectName("page_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Temperature_Frame = QtWidgets.QFrame(self.frame_3)
        self.Temperature_Frame.setEnabled(True)
        self.Temperature_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Temperature_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Temperature_Frame.setObjectName("Temperature_Frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Temperature_Frame)
        self.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.temperature_text_label = QtWidgets.QLabel(self.Temperature_Frame)
        self.temperature_text_label.setEnabled(True)
        self.temperature_text_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.temperature_text_label.setTextFormat(QtCore.Qt.AutoText)
        self.temperature_text_label.setObjectName("temperature_text_label")
        self.horizontalLayout_7.addWidget(self.temperature_text_label)
        self.temperature_icon_label = QtWidgets.QLabel(self.Temperature_Frame)
        self.temperature_icon_label.setEnabled(True)
        self.temperature_icon_label.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setKerning(True)
        self.temperature_icon_label.setFont(font)
        self.temperature_icon_label.setText("")
        self.temperature_icon_label.setPixmap(QtGui.QPixmap("../icons/temperature.png"))
        self.temperature_icon_label.setScaledContents(True)
        self.temperature_icon_label.setObjectName("temperature_icon_label")
        self.horizontalLayout_7.addWidget(self.temperature_icon_label)
        self.verticalLayout_7.addWidget(self.Temperature_Frame)
        self.Wind_Speed_Frame = QtWidgets.QFrame(self.frame_3)
        self.Wind_Speed_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Wind_Speed_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Wind_Speed_Frame.setObjectName("Wind_Speed_Frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Wind_Speed_Frame)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.wind_text_label = QtWidgets.QLabel(self.Wind_Speed_Frame)
        self.wind_text_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.wind_text_label.setObjectName("wind_text_label")
        self.horizontalLayout_6.addWidget(self.wind_text_label)
        self.wind_icon_label = QtWidgets.QLabel(self.Wind_Speed_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wind_icon_label.sizePolicy().hasHeightForWidth())
        self.wind_icon_label.setSizePolicy(sizePolicy)
        self.wind_icon_label.setMaximumSize(QtCore.QSize(100, 100))
        self.wind_icon_label.setText("")
        self.wind_icon_label.setPixmap(QtGui.QPixmap("../icons/wind.png"))
        self.wind_icon_label.setScaledContents(True)
        self.wind_icon_label.setObjectName("wind_icon_label")
        self.horizontalLayout_6.addWidget(self.wind_icon_label)
        self.verticalLayout_7.addWidget(self.Wind_Speed_Frame)
        self.Humidity_Frame = QtWidgets.QFrame(self.frame_3)
        self.Humidity_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Humidity_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Humidity_Frame.setObjectName("Humidity_Frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Humidity_Frame)
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.humidity_text_label = QtWidgets.QLabel(self.Humidity_Frame)
        self.humidity_text_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.humidity_text_label.setObjectName("humidity_text_label")
        self.horizontalLayout_8.addWidget(self.humidity_text_label)
        self.humidity_icon_label = QtWidgets.QLabel(self.Humidity_Frame)
        self.humidity_icon_label.setMaximumSize(QtCore.QSize(100, 100))
        self.humidity_icon_label.setText("")
        self.humidity_icon_label.setPixmap(QtGui.QPixmap("../icons/humidity.png"))
        self.humidity_icon_label.setScaledContents(True)
        self.humidity_icon_label.setObjectName("humidity_icon_label")
        self.horizontalLayout_8.addWidget(self.humidity_icon_label)
        self.verticalLayout_7.addWidget(self.Humidity_Frame)
        self.Pressure_Frame = QtWidgets.QFrame(self.frame_3)
        self.Pressure_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pressure_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pressure_Frame.setObjectName("Pressure_Frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Pressure_Frame)
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pressure_text_label = QtWidgets.QLabel(self.Pressure_Frame)
        self.pressure_text_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.pressure_text_label.setObjectName("pressure_text_label")
        self.horizontalLayout_5.addWidget(self.pressure_text_label)
        self.pressure_icon_label = QtWidgets.QLabel(self.Pressure_Frame)
        self.pressure_icon_label.setMaximumSize(QtCore.QSize(100, 100))
        self.pressure_icon_label.setText("")
        self.pressure_icon_label.setPixmap(QtGui.QPixmap("../icons/pressure.png"))
        self.pressure_icon_label.setScaledContents(True)
        self.pressure_icon_label.setObjectName("pressure_icon_label")
        self.horizontalLayout_5.addWidget(self.pressure_icon_label)
        self.verticalLayout_7.addWidget(self.Pressure_Frame)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Weather_Frame = QtWidgets.QFrame(self.frame_2)
        self.Weather_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Weather_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Weather_Frame.setObjectName("Weather_Frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Weather_Frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.weather_text_label = QtWidgets.QLabel(self.Weather_Frame)
        self.weather_text_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.weather_text_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.weather_text_label.setObjectName("weather_text_label")
        self.horizontalLayout_9.addWidget(self.weather_text_label)
        self.weather_icon_label = QtWidgets.QLabel(self.Weather_Frame)
        self.weather_icon_label.setMaximumSize(QtCore.QSize(100, 100))
        self.weather_icon_label.setText("")
        self.weather_icon_label.setObjectName("weather_icon_label")
        self.horizontalLayout_9.addWidget(self.weather_icon_label)
        self.verticalLayout_8.addWidget(self.Weather_Frame)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8.addWidget(self.frame_9)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_6.addWidget(self.frame)
        self.Pages_Widget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Italy_top_buttons = QtWidgets.QFrame(self.page_3)
        self.Italy_top_buttons.setMinimumSize(QtCore.QSize(0, 40))
        self.Italy_top_buttons.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Italy_top_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Italy_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Italy_top_buttons.setObjectName("Italy_top_buttons")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.Italy_top_buttons)
        self.horizontalLayout_15.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.italy_weather_table_button = QtWidgets.QPushButton(self.Italy_top_buttons)
        self.italy_weather_table_button.setMinimumSize(QtCore.QSize(0, 30))
        self.italy_weather_table_button.setStyleSheet("QPushButton {\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(35, 35, 35);\n"
                                                      "    border: 0px solid;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: rgb(45, 45, 45);\n"
                                                      "}")
        self.italy_weather_table_button.setObjectName("italy_weather_table_button")
        self.horizontalLayout_15.addWidget(self.italy_weather_table_button, 0, QtCore.Qt.AlignVCenter)
        self.italy_clustering_button = QtWidgets.QPushButton(self.Italy_top_buttons)
        self.italy_clustering_button.setMinimumSize(QtCore.QSize(0, 30))
        self.italy_clustering_button.setStyleSheet("QPushButton {\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(35, 35, 35);\n"
                                                   "    border: 0px solid;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: rgb(45, 45, 45);\n"
                                                   "}")
        self.italy_clustering_button.setObjectName("italy_clustering_button")
        self.horizontalLayout_15.addWidget(self.italy_clustering_button)
        self.verticalLayout_9.addWidget(self.Italy_top_buttons)
        self.frame_5 = QtWidgets.QFrame(self.page_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Italy_Pages = QtWidgets.QStackedWidget(self.frame_5)
        self.Italy_Pages.setObjectName("Italy_Pages")
        self.italy_table_page = QtWidgets.QWidget()
        self.italy_table_page.setObjectName("italy_table_page")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.italy_table_page)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_6 = QtWidgets.QFrame(self.italy_table_page)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.today_weather_table_widget = QtWidgets.QTableWidget(self.frame_6)
        self.today_weather_table_widget.setMaximumSize(QtCore.QSize(620, 16777215))
        self.today_weather_table_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.today_weather_table_widget.setObjectName("today_weather_table_widget")
        self.today_weather_table_widget.setColumnCount(7)
        self.today_weather_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.today_weather_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.today_weather_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.today_weather_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.today_weather_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.today_weather_table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.today_weather_table_widget.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_14.addWidget(self.today_weather_table_widget)
        self.horizontalLayout_13.addWidget(self.frame_6)
        self.Italy_Pages.addWidget(self.italy_table_page)
        self.italy_clustering_page = QtWidgets.QWidget()
        self.italy_clustering_page.setObjectName("italy_clustering_page")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.italy_clustering_page)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_4 = QtWidgets.QFrame(self.italy_clustering_page)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.clustering_k_bar = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clustering_k_bar.sizePolicy().hasHeightForWidth())
        self.clustering_k_bar.setSizePolicy(sizePolicy)
        self.clustering_k_bar.setMinimumSize(QtCore.QSize(0, 40))
        self.clustering_k_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.clustering_k_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.clustering_k_bar.setObjectName("clustering_k_bar")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.clustering_k_bar)
        self.horizontalLayout_17.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.LineEdit_K = QtWidgets.QLineEdit(self.clustering_k_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit_K.sizePolicy().hasHeightForWidth())
        self.LineEdit_K.setSizePolicy(sizePolicy)
        self.LineEdit_K.setMinimumSize(QtCore.QSize(300, 30))
        self.LineEdit_K.setMaximumSize(QtCore.QSize(300, 16777215))
        self.LineEdit_K.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;\n"
                                      "border-bottom: 3px solid rgb(45, 45, 45)\n"
                                      "")
        self.LineEdit_K.setObjectName("LineEdit_K")
        self.horizontalLayout_17.addWidget(self.LineEdit_K)
        self.pushButton = QtWidgets.QPushButton(self.clustering_k_bar)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_17.addWidget(self.pushButton)
        self.start_clustering_button = QtWidgets.QPushButton(self.clustering_k_bar)
        self.start_clustering_button.setMinimumSize(QtCore.QSize(200, 30))
        self.start_clustering_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.start_clustering_button.setStyleSheet("QPushButton {\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(35, 35 35);\n"
                                                   "    border: 0px solid;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: rgb(45, 45, 45);\n"
                                                   "}")
        self.start_clustering_button.setObjectName("start_clustering_button")
        self.horizontalLayout_17.addWidget(self.start_clustering_button)
        self.verticalLayout_13.addWidget(self.clustering_k_bar, 0, QtCore.Qt.AlignLeft)
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.clustering_pages = QtWidgets.QStackedWidget(self.frame_10)
        self.clustering_pages.setObjectName("clustering_pages")
        self.clustering_table_page = QtWidgets.QWidget()
        self.clustering_table_page.setObjectName("clustering_table_page")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.clustering_table_page)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.clustering_table = QtWidgets.QTableWidget(self.clustering_table_page)
        self.clustering_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.clustering_table.setObjectName("clustering_table")
        self.clustering_table.setColumnCount(6)
        self.clustering_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clustering_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustering_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustering_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustering_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustering_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustering_table.setHorizontalHeaderItem(5, item)
        self.verticalLayout_15.addWidget(self.clustering_table)
        self.clustering_pages.addWidget(self.clustering_table_page)
        self.clustering_chart_page = QtWidgets.QWidget()
        self.clustering_chart_page.setObjectName("clustering_chart_page")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.clustering_chart_page)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.clustering_chart_label = QtWidgets.QLabel(self.clustering_chart_page)
        self.clustering_chart_label.setText("")
        self.clustering_chart_label.setObjectName("clustering_chart_label")
        self.verticalLayout_16.addWidget(self.clustering_chart_label)
        self.clustering_pages.addWidget(self.clustering_chart_page)
        self.verticalLayout_14.addWidget(self.clustering_pages)
        self.verticalLayout_13.addWidget(self.frame_10)
        self.verticalLayout_12.addWidget(self.frame_4)
        self.Italy_Pages.addWidget(self.italy_clustering_page)
        self.horizontalLayout_12.addWidget(self.Italy_Pages)
        self.verticalLayout_9.addWidget(self.frame_5)
        self.Pages_Widget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.page2_topbar = QtWidgets.QFrame(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_topbar.sizePolicy().hasHeightForWidth())
        self.page2_topbar.setSizePolicy(sizePolicy)
        self.page2_topbar.setMinimumSize(QtCore.QSize(0, 40))
        self.page2_topbar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.page2_topbar.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.page2_topbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.page2_topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page2_topbar.setObjectName("page2_topbar")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.page2_topbar)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.weather_table_button = QtWidgets.QPushButton(self.page2_topbar)
        self.weather_table_button.setStyleSheet("QPushButton {\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(40, 40, 40);\n"
                                                "    border: 0px solid;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(45, 45, 45);\n"
                                                "}")
        self.weather_table_button.setObjectName("weather_table_button")
        self.horizontalLayout_10.addWidget(self.weather_table_button)
        self.temperature_chart_button = QtWidgets.QPushButton(self.page2_topbar)
        self.temperature_chart_button.setStyleSheet("QPushButton {\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(40, 40, 40);\n"
                                                    "    border: 0px solid;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {\n"
                                                    "    background-color: rgb(45, 45, 45);\n"
                                                    "}")
        self.temperature_chart_button.setObjectName("temperature_chart_button")
        self.horizontalLayout_10.addWidget(self.temperature_chart_button)
        self.humidity_chart_button = QtWidgets.QPushButton(self.page2_topbar)
        self.humidity_chart_button.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(40, 40, 40);\n"
                                                 "    border: 0px solid;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(45, 45, 45);\n"
                                                 "}")
        self.humidity_chart_button.setObjectName("humidity_chart_button")
        self.horizontalLayout_10.addWidget(self.humidity_chart_button)
        self.wind_speed_chart_button = QtWidgets.QPushButton(self.page2_topbar)
        self.wind_speed_chart_button.setStyleSheet("QPushButton {\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(40, 40, 40);\n"
                                                   "    border: 0px solid;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: rgb(45, 45, 45);\n"
                                                   "}")
        self.wind_speed_chart_button.setObjectName("wind_speed_chart_button")
        self.horizontalLayout_10.addWidget(self.wind_speed_chart_button)
        self.pressure_chart_button = QtWidgets.QPushButton(self.page2_topbar)
        self.pressure_chart_button.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(40, 40, 40);\n"
                                                 "    border: 0px solid;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(45, 45, 45);\n"
                                                 "}")
        self.pressure_chart_button.setObjectName("pressure_chart_button")
        self.horizontalLayout_10.addWidget(self.pressure_chart_button)
        self.condition_chart_button = QtWidgets.QPushButton(self.page2_topbar)
        self.condition_chart_button.setStyleSheet("QPushButton {\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(40, 40, 40);\n"
                                                  "    border: 0px solid;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgb(45, 45, 45);\n"
                                                  "}")
        self.condition_chart_button.setObjectName("condition_chart_button")
        self.horizontalLayout_10.addWidget(self.condition_chart_button)
        self.verticalLayout_10.addWidget(self.page2_topbar, 0, QtCore.Qt.AlignVCenter)
        self.frame_pages_2 = QtWidgets.QFrame(self.page_2)
        self.frame_pages_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages_2.setObjectName("frame_pages_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_pages_2)
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.weather_today_pages = QtWidgets.QStackedWidget(self.frame_pages_2)
        self.weather_today_pages.setObjectName("weather_today_pages")
        self.weather_table_page = QtWidgets.QWidget()
        self.weather_table_page.setObjectName("weather_table_page")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.weather_table_page)
        self.horizontalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.weather_table_widget = QtWidgets.QTableWidget(self.weather_table_page)
        self.weather_table_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weather_table_widget.setObjectName("weather_table_widget")
        self.weather_table_widget.setColumnCount(6)
        self.weather_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.weather_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.weather_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.weather_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.weather_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.weather_table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.weather_table_widget.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_11.addWidget(self.weather_table_widget)
        self.weather_today_pages.addWidget(self.weather_table_page)
        self.temperature_chart_page = QtWidgets.QWidget()
        self.temperature_chart_page.setObjectName("temperature_chart_page")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.temperature_chart_page)
        self.horizontalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.temperature_chart_label = QtWidgets.QLabel(self.temperature_chart_page)
        self.temperature_chart_label.setObjectName("temperature_chart_label")
        self.horizontalLayout_19.addWidget(self.temperature_chart_label)
        self.weather_today_pages.addWidget(self.temperature_chart_page)
        self.humidity_chart_page = QtWidgets.QWidget()
        self.humidity_chart_page.setObjectName("humidity_chart_page")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.humidity_chart_page)
        self.horizontalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.humidity_chart_label = QtWidgets.QLabel(self.humidity_chart_page)
        self.humidity_chart_label.setObjectName("humidity_chart_label")
        self.horizontalLayout_20.addWidget(self.humidity_chart_label)
        self.weather_today_pages.addWidget(self.humidity_chart_page)
        self.wind_speed_chart_page = QtWidgets.QWidget()
        self.wind_speed_chart_page.setObjectName("wind_speed_chart_page")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.wind_speed_chart_page)
        self.horizontalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.wind_speed_chart_label = QtWidgets.QLabel(self.wind_speed_chart_page)
        self.wind_speed_chart_label.setObjectName("wind_speed_chart_label")
        self.horizontalLayout_21.addWidget(self.wind_speed_chart_label)
        self.weather_today_pages.addWidget(self.wind_speed_chart_page)
        self.pressure_chart_page = QtWidgets.QWidget()
        self.pressure_chart_page.setObjectName("pressure_chart_page")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.pressure_chart_page)
        self.horizontalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pressure_chart_label = QtWidgets.QLabel(self.pressure_chart_page)
        self.pressure_chart_label.setObjectName("pressure_chart_label")
        self.horizontalLayout_22.addWidget(self.pressure_chart_label)
        self.weather_today_pages.addWidget(self.pressure_chart_page)
        self.condition_chart_page = QtWidgets.QWidget()
        self.condition_chart_page.setObjectName("condition_chart_page")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.condition_chart_page)
        self.horizontalLayout_23.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.condition_chart_label = QtWidgets.QLabel(self.condition_chart_page)
        self.condition_chart_label.setObjectName("condition_chart_label")
        self.horizontalLayout_23.addWidget(self.condition_chart_label)
        self.weather_today_pages.addWidget(self.condition_chart_page)
        self.verticalLayout_11.addWidget(self.weather_today_pages)
        self.verticalLayout_10.addWidget(self.frame_pages_2)
        self.Pages_Widget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_7 = QtWidgets.QFrame(self.page_4)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.intervals_label = QtWidgets.QLabel(self.frame_7)
        self.intervals_label.setMinimumSize(QtCore.QSize(100, 0))
        self.intervals_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.intervals_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.intervals_label.setObjectName("intervals_label")
        self.horizontalLayout_16.addWidget(self.intervals_label, 0, QtCore.Qt.AlignLeft)
        self.intervals_combo_box = QtWidgets.QComboBox(self.frame_7)
        self.intervals_combo_box.setMinimumSize(QtCore.QSize(150, 0))
        self.intervals_combo_box.setMaximumSize(QtCore.QSize(200, 16777215))
        self.intervals_combo_box.setObjectName("intervals_combo_box")
        self.intervals_combo_box.addItem("")
        self.intervals_combo_box.addItem("")
        self.intervals_combo_box.addItem("")
        self.horizontalLayout_16.addWidget(self.intervals_combo_box)
        self.generate_data_button = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_data_button.sizePolicy().hasHeightForWidth())
        self.generate_data_button.setSizePolicy(sizePolicy)
        self.generate_data_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.generate_data_button.setStyleSheet("QPushButton {\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(40, 40, 40);\n"
                                                "    border: 0px solid;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(45, 45, 45);\n"
                                                "}")
        self.generate_data_button.setObjectName("generate_data_button")
        self.horizontalLayout_16.addWidget(self.generate_data_button)
        self.verticalLayout_17.addWidget(self.frame_7, 0, QtCore.Qt.AlignLeft)
        self.frame_8 = QtWidgets.QFrame(self.page_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.generated_data_table_widget = QtWidgets.QTableWidget(self.frame_8)
        self.generated_data_table_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.generated_data_table_widget.setObjectName("generated_data_table_widget")
        self.generated_data_table_widget.setColumnCount(5)
        self.generated_data_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.generated_data_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_data_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_data_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_data_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.generated_data_table_widget.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_18.addWidget(self.generated_data_table_widget)
        self.verticalLayout_17.addWidget(self.frame_8)
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.Pages_Widget.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_Widget.setCurrentIndex(0)
        self.Italy_Pages.setCurrentIndex(0)
        self.clustering_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Btn_Search1.clicked.connect(self.search_button_action)
        self.Btn_Menu_3.clicked.connect(self.italy_table_action)
        self.pushButton.clicked.connect(self.italy_clustering_action)
        self.generate_data_button.clicked.connect(self.generate_button_action)

    def search_button_action(self, MainWindow):
        print("WeatherReport> Search Button Routine")
        self.loading_label.setText("Loading...")

        self.temperature_text_label.setText("Temperature : Loading...")
        self.wind_text_label.setText("Wind Speed : Loading...")
        self.pressure_text_label.setText("Pressure : Loading...")
        self.humidity_text_label.setText("Humidity : Loading...")
        self.weather_text_label.setText("Weather condition : Loading...")

        sensor = self.LineEdit_Search1.text()

        # Weather Now - uso del modulo web_scraping.py
        print("WeatherReport> Loading weather now...")

        df_now = get_weather_now(sensor_name=sensor)

        temp = df_now['Temperature'].iloc[0]
        self.temperature_text_label.setText("Temperature : " + temp)

        hum = df_now['Humidity'].iloc[0]
        self.humidity_text_label.setText("Humidity : " + hum)

        ws = df_now['Wind Speed'].iloc[0]
        self.wind_text_label.setText("Wind Speed : " + ws)

        pre = df_now['Pressure'].iloc[0]
        self.pressure_text_label.setText("Pressure : " + pre)

        cond = df_now['Condition'].iloc[0]
        # Imposta la corretta icona
        self.weather_text_label.setText("Weather condition : " + cond)
        if cond == 'Fair' or cond == 'Mostly Sunny':
            self.weather_icon_label.setPixmap(QtGui.QPixmap("../icons/fair.png"))
        if cond == 'Partly Cloudy' or cond == 'Cloudy' or cond == 'Mostly Cloudy':
            self.weather_icon_label.setPixmap(QtGui.QPixmap("../icons/cloudy.png"))
        if 'Rain' in cond:
            self.weather_icon_label.setPixmap(QtGui.QPixmap("../icons/rainy.png"))
        if 'rain' in cond:
            self.weather_icon_label.setPixmap(QtGui.QPixmap("../icons/rainy.png"))
        if 'snow' in cond:
            self.weather_icon_label.setPixmap(QtGui.QPixmap("../icons/snow.png"))
        if 'Snow' in cond:
            self.weather_icon_label.setPixmap(QtGui.QPixmap("../icons/snow.png"))

        # TODO estendere ad altre condizioni climatiche

        self.weather_icon_label.setScaledContents(True)

        self.loading_label.setText("")

        # Weather Today
        print("WeatherReport> Loading weather today...")

        # Ottiene la tabella meteorologica
        df_today = get_today_weather_table(sensor_name=sensor)
        self.weather_table_widget.setRowCount(df_today.shape[0])

        # Popola l'apposito widget
        for i in range(0, df_today.shape[0]):
            self.weather_table_widget.setItem(i, 0, QtWidgets.QTableWidgetItem(df_today['Time'].iloc[i]))
            self.weather_table_widget.setItem(i, 1, QtWidgets.QTableWidgetItem(df_today['Temperature'].iloc[i]))
            self.weather_table_widget.setItem(i, 2, QtWidgets.QTableWidgetItem(df_today['Humidity'].iloc[i]))
            self.weather_table_widget.setItem(i, 3, QtWidgets.QTableWidgetItem(df_today['Wind Speed'].iloc[i]))
            self.weather_table_widget.setItem(i, 4, QtWidgets.QTableWidgetItem(df_today['Pressure'].iloc[i]))
            self.weather_table_widget.setItem(i, 5, QtWidgets.QTableWidgetItem(df_today['Condition'].iloc[i]))

        print("WeatherReport> Plotting Charts")

        # Grafico a torta prima del preprocessing (nel preprocessing quella riga viene eliminata

        plot_condition_today(df_today)
        self.condition_chart_label.setPixmap(QtGui.QPixmap("../out/today_condition_chart.png"))
        self.condition_chart_label.setScaledContents(True)

        df_today = preprocessing(df_today)  # Necessario altrimenti l'asse delle y dei grafici non viene ordinata

        plot_temperature_today(df_today)
        self.temperature_chart_label.setPixmap(QtGui.QPixmap("../out/today_temperature_chart.png"))
        self.temperature_chart_label.setScaledContents(True)

        plot_humidity_today(df_today)
        self.humidity_chart_label.setPixmap(QtGui.QPixmap("../out/today_humidity_chart.png"))
        self.humidity_chart_label.setScaledContents(True)

        plot_wind_speed_today(df_today)
        self.wind_speed_chart_label.setPixmap(QtGui.QPixmap("../out/today_wind_speed_chart.png"))
        self.wind_speed_chart_label.setScaledContents(True)

        plot_pressure_today(df_today)
        self.pressure_chart_label.setPixmap(QtGui.QPixmap("../out/today_pressure_chart.png"))
        self.pressure_chart_label.setScaledContents(True)

        self.loading_label.setText("")
        return

    def generate_button_action(self, MainWindow):
        print("WeatherReport> Generating data")

        sensor = self.LineEdit_Search1.text()
        df_today = get_today_weather_table(sensor_name=sensor)
        df_today = pr.preprocessing(df_today)
        df = df_today.drop('Condition', axis=1)
        freq = str(self.intervals_combo_box.currentText())
        df_expanded = expand_dataset(dataset=df, freq=freq)
        self.generated_data_table_widget.setRowCount(df_expanded.shape[0])

        for i in range(0, df_expanded.shape[0]):
            self.generated_data_table_widget.setItem(i, 0, QtWidgets.QTableWidgetItem(df_expanded['Time'].iloc[i]))
            self.generated_data_table_widget.setItem(i, 1, QtWidgets.QTableWidgetItem(
                str(df_expanded['Temperature'].iloc[i])))
            self.generated_data_table_widget.setItem(i, 2,
                                                     QtWidgets.QTableWidgetItem(str(df_expanded['Humidity'].iloc[i])))
            self.generated_data_table_widget.setItem(i, 3,
                                                     QtWidgets.QTableWidgetItem(str(df_expanded['Wind Speed'].iloc[i])))
            self.generated_data_table_widget.setItem(i, 4,
                                                     QtWidgets.QTableWidgetItem(str(df_expanded['Pressure'].iloc[i])))

        return

    def italy_table_action(self, MainWindow):
        global table_on
        global df_now_italy
        if (table_on):
            return
        print("WeatherReport> Initiating Today Weather Italy procedure")
        df_now_italy = get_weather_now_italy()
        df_now_italy = preprocessing_italy(df_now_italy)
        self.today_weather_table_widget.setRowCount(df_now_italy.shape[0])
        self.today_weather_table_widget.setColumnCount(6)

        for i in range(0, df_now_italy.shape[0]):
            self.today_weather_table_widget.setItem(i, 0, QtWidgets.QTableWidgetItem(df_now_italy['City'].iloc[i]))
            self.today_weather_table_widget.setItem(i, 1, QtWidgets.QTableWidgetItem(
                str(df_now_italy['Temperature'].iloc[i])))
            self.today_weather_table_widget.setItem(i, 2,
                                                    QtWidgets.QTableWidgetItem(str(df_now_italy['Humidity'].iloc[i])))
            self.today_weather_table_widget.setItem(i, 3,
                                                    QtWidgets.QTableWidgetItem(str(df_now_italy['Wind Speed'].iloc[i])))
            self.today_weather_table_widget.setItem(i, 4,
                                                    QtWidgets.QTableWidgetItem(str(df_now_italy['Pressure'].iloc[i])))
            self.today_weather_table_widget.setItem(i, 5, QtWidgets.QTableWidgetItem(df_now_italy['Condition'].iloc[i]))

        table_on = True

    def italy_clustering_action(self, MainWindow):
        print("WeatherReport> Initializing clustering procedure...")
        global clustering_on
        global df_now_italy
        if (clustering_on):
            return

        k = int(self.LineEdit_K.text())
        df_clustering = my_kmeans_cities(df=df_now_italy, k=k)

        self.clustering_table.setRowCount(df_clustering.shape[0])

        for i in range(0, df_clustering.shape[0]):
            self.clustering_table.setItem(i, 0, QtWidgets.QTableWidgetItem(df_clustering['City'].iloc[i]))
            self.clustering_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(df_clustering['prediction'].iloc[i])))
            self.clustering_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(df_clustering['Temperature'].iloc[i])))
            self.clustering_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(df_clustering['Humidity'].iloc[i])))
            self.clustering_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(df_clustering['Wind Speed'].iloc[i])))
            self.clustering_table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(df_clustering['Pressure'].iloc[i])))

        self.clustering_chart_label.setPixmap(QtGui.QPixmap("../out/clustering_plot.png"))
        self.clustering_chart_label.setScaledContents(True)

        clustering_on = True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Report"))
        self.Btn_Menu.setText(_translate("MainWindow", "Menu"))
        self.LineEdit_Search1.setPlaceholderText(_translate("MainWindow", "Search sensor..."))
        self.Btn_Menu_1.setText(_translate("MainWindow", "Weather Now"))
        self.Btn_Menu_2.setText(_translate("MainWindow", "Weather Today"))
        self.Btn_Menu_3.setText(_translate("MainWindow", "Weather Italy"))
        self.Btn_Menu_4.setText(_translate("MainWindow", "Generate Data"))
        self.temperature_text_label.setText(_translate("MainWindow", "Temperature : None"))
        self.wind_text_label.setText(_translate("MainWindow", "Wind Speed : None"))
        self.humidity_text_label.setText(_translate("MainWindow", "Humidity : None"))
        self.pressure_text_label.setText(_translate("MainWindow", "Pressure : None"))
        self.weather_text_label.setText(_translate("MainWindow", "Weather condition : None"))
        self.italy_weather_table_button.setText(_translate("MainWindow", "Weather Table"))
        self.italy_clustering_button.setText(_translate("MainWindow", "Clustering"))

        item = self.today_weather_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "City"))
        item = self.today_weather_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.today_weather_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.today_weather_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Wind Speed"))
        item = self.today_weather_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pressure"))
        item = self.today_weather_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Condition"))

        self.LineEdit_K.setPlaceholderText(_translate("MainWindow", "Number of clusters (k)..."))
        self.pushButton.setText(_translate("MainWindow", "Clustering Table"))
        self.start_clustering_button.setText(_translate("MainWindow", "Clustering Chart"))
        item = self.clustering_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "City"))
        item = self.clustering_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Prediction"))
        item = self.clustering_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.clustering_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.clustering_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Wind Speed"))
        item = self.clustering_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pressure"))
        self.weather_table_button.setText(_translate("MainWindow", "Weather Table"))
        self.temperature_chart_button.setText(_translate("MainWindow", "Temperature Chart"))
        self.humidity_chart_button.setText(_translate("MainWindow", "Humidity Chart"))
        self.wind_speed_chart_button.setText(_translate("MainWindow", "Wind Speed Chart"))
        self.pressure_chart_button.setText(_translate("MainWindow", "Pressure Chart"))
        self.condition_chart_button.setText(_translate("MainWindow", "Condition Chart"))
        item = self.weather_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.weather_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.weather_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.weather_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Wind Speed"))
        item = self.weather_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pressure"))
        item = self.weather_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Condition"))
        self.temperature_chart_label.setText(_translate("MainWindow", ""))
        self.humidity_chart_label.setText(_translate("MainWindow", ""))
        self.wind_speed_chart_label.setText(_translate("MainWindow", ""))
        self.pressure_chart_label.setText(_translate("MainWindow", ""))
        self.condition_chart_label.setText(_translate("MainWindow", ""))
        self.intervals_label.setText(_translate("MainWindow", "Intervals"))
        self.intervals_combo_box.setItemText(0, _translate("MainWindow", "1min"))
        self.intervals_combo_box.setItemText(1, _translate("MainWindow", "5min"))
        self.intervals_combo_box.setItemText(2, _translate("MainWindow", "10min"))
        self.generate_data_button.setText(_translate("MainWindow", "Generate"))
        item = self.generated_data_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.generated_data_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.generated_data_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.generated_data_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Wind Speed"))
        item = self.generated_data_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pressure"))
