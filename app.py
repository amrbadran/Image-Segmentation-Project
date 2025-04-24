# Segemntation Filters Project
# Done By Amr Badran (12113636)
# DeadLine : 26/12/2023 11:59 PM
# Last Modification : 24/12/2023 8:20 PM

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,QMessageBox ,QInputDialog,QDialog,QTextEdit,QSizePolicy,QCheckBox,QLabel
from PyQt5.QtGui import QColor,QPalette
from fractions import Fraction
from PyQt5.QtCore import Qt

import filters
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Segemntation Project")
        MainWindow.resize(1235, 744)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("*{\n"
"    font-family:\'Courier New\', Courier, monospace\n"
"}\n"
"QMainWindow{\n"
"    background-color:#222;\n"
"\n"
"}\n"
"QFrame{\n"
"    background-color:#222;\n"
"}\n"
"#frame_2{\n"
"    background-color:#555;\n"
"}\n"
"#FileNametxt{\n"
"\n"
"    padding:5px;\n"
"       margin:5px;\n"
"    border: 1px solid #fff;\n"
"    border-radius: 5px;\n"
"    outline: none;\n"
"    font-size: 14px;\n"
"    background-color:#222;\n"
"    color:#fff;\n"
"   \n"
"}\n"
"#LoadFileBtn{\n"
"\n"
"\n"
"        padding: 10px 20px;\n"
"        background-color: #333; \n"
"        color: #fff; \n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        \n"
"        font-size: 16px;\n"
"        \n"
"    \n"
"  \n"
"}\n"
"#LoadFileBtn:hover {\n"
"    background-color: #555; \n"
"}\n"
"#img_preview{\n"
"    border:7px solid #333;\n"
"    \n"
"}\n"
"QPushButton{\n"
"\n"
"\n"
"    padding: 10px 20px;\n"
"    background: #333;\n"
"    color: #fff; \n"
"   \n"
"    border-radius: 5px;\n"
"    \n"
"    font-size: 16px;\n"
"    border : 1px solid #eee;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background:#555;\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1341, 751))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FileNametxt = QtWidgets.QLineEdit(self.frame)
        self.FileNametxt.setGeometry(QtCore.QRect(340, 20, 631, 41))
        self.FileNametxt.setObjectName("FileNametxt")
        self.LoadFileBtn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.open_file_dialog())
        self.LoadFileBtn.setGeometry(QtCore.QRect(1000, 20, 151, 40))
        self.LoadFileBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoadFileBtn.setObjectName("LoadFileBtn")
        self.img_preview = QtWidgets.QLabel(self.frame)
        self.img_preview.setGeometry(QtCore.QRect(340, 90, 821, 531))
        self.img_preview.setText("")
        self.img_preview.setPixmap(QtGui.QPixmap(":/newPrefix/ttt.jpg"))
        self.img_preview.setScaledContents(True)
        self.img_preview.setObjectName("img_preview")
        self.PointDetection_Btn = QtWidgets.QPushButton(self.frame , clicked = lambda: self.PointDetectionMethod())
        self.PointDetection_Btn.setGeometry(QtCore.QRect(30, 49, 191, 51))
        self.PointDetection_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PointDetection_Btn.setObjectName("PointDetection_Btn")
        self.HorzintalLine_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.HorzintalLine())
        self.HorzintalLine_Btn.setGeometry(QtCore.QRect(30, 120, 190, 51))
        self.HorzintalLine_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HorzintalLine_Btn.setObjectName("HorzintalLine_Btn")
        self.VerticalLine_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.VerticalLine())
        self.VerticalLine_Btn.setGeometry(QtCore.QRect(30, 190, 190, 51))
        self.VerticalLine_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VerticalLine_Btn.setObjectName("VerticalLine_Btn")
        self.F45Line_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.F45Line())
        self.F45Line_Btn.setGeometry(QtCore.QRect(30, 260, 190, 51))
        self.F45Line_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.F45Line_Btn.setObjectName("F45Line_Btn")
        self.FN45Line_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.FN45Line())
        self.FN45Line_Btn.setGeometry(QtCore.QRect(30, 330, 190, 51))
        self.FN45Line_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FN45Line_Btn.setObjectName("FN45Line_Btn")
        self.HorzintalEdge_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.HorzintalEdge())
        self.HorzintalEdge_Btn.setGeometry(QtCore.QRect(30, 400, 190, 51))
        self.HorzintalEdge_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HorzintalEdge_Btn.setObjectName("HorzintalEdge_Btn")
        self.VerticalEdge_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.VerticalEdge())
        self.VerticalEdge_Btn.setGeometry(QtCore.QRect(30, 470, 190, 51))
        self.VerticalEdge_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VerticalEdge_Btn.setObjectName("VerticalEdge_Btn")
        self.F45Edge_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.F45Edge())
        self.F45Edge_Btn.setGeometry(QtCore.QRect(30, 540, 190, 51))
        self.F45Edge_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.F45Edge_Btn.setObjectName("F45Edge_Btn")
        self.FN45Edge_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.FN45Edge())
        self.FN45Edge_Btn.setGeometry(QtCore.QRect(30, 610, 190, 51))
        self.FN45Edge_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FN45Edge_Btn.setObjectName("FN45Edge_Btn")
        self.Thershold_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.Thershold())
        self.Thershold_Btn.setGeometry(QtCore.QRect(340, 650, 190, 51))
        self.Thershold_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Thershold_Btn.setObjectName("Thershold_Btn")
        self.Laplacain_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.Laplacain())
        self.Laplacain_Btn.setGeometry(QtCore.QRect(550, 650, 190, 51))
        self.Laplacain_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Laplacain_Btn.setObjectName("Laplacain_Btn")
        self.LOG_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.LOG())
        self.LOG_Btn.setGeometry(QtCore.QRect(760, 650, 190, 51))
        self.LOG_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LOG_Btn.setObjectName("LOG_Btn")
        self.Custom_Btn = QtWidgets.QPushButton(self.frame,clicked=lambda:self.Custom())
        self.Custom_Btn.setGeometry(QtCore.QRect(970, 650, 190, 51))
        self.Custom_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Custom_Btn.setObjectName("Custom_Btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def open_file_dialog(self):
        #this function for get the image file from device using QFileDialog (built in Qt)
        file_dialog = QFileDialog() 
        file_path, _ = file_dialog.getOpenFileName(MainWindow, 'Open Image', '', 'All Files (*)')

        if file_path: # if file path is exists 
            self.FileNametxt.setText(file_path) # set the path
            self.img_preview.setPixmap(QtGui.QPixmap(file_path)) # set the image

        
    def PointDetectionMethod(self):
        image_input_path =self.FileNametxt.text() # get the image path
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE) # read the image with gray-scale
            obj = filters.filters(img) # build the filters object (1st class)
            output = obj.pointDetect() # call the matching filter method
            cv.imwrite("output.jpg",output) # save the enhanced image
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg")) # set the enhanced image on image-preveiw
        except Exception as e: # if something fails 
            self.show_error_message()
    def HorzintalLine(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.horizntalLine()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def VerticalLine(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.verticalLine()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def F45Line(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.F45Line()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def FN45Line(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.FN45Line()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def HorzintalEdge(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.horizntalEdge()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def VerticalEdge(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.verticalEdge()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def F45Edge(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.F45Edge()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def FN45Edge(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.FN45Edge()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def Laplacain(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.Laplacian()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def LOG(self):
        image_input_path =self.FileNametxt.text()
        try:
            img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
            obj = filters.filters(img)
            output = obj.LOG()
            cv.imwrite("output.jpg",output)
            self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
        except Exception as e:
            self.show_error_message()
    def Thershold(self):

        image_input_path =self.FileNametxt.text()
        input_dialog = QInputDialog() #input dialog for T value 
             
        List = ("Threshold","Inverse Threshold") # select either threshold,inverse threshold

        T, ok = input_dialog.getInt(MainWindow, 'Threshold', 'Enter an Threshold Value:')
        str1 , okk = input_dialog.getItem(MainWindow,"Select Type:","Select Threshold Type",List,0,False)

        flag = None
        if(str1 == 'Threshold'):flag = False
        else : flag = True
        if ok==False:
            return
        else:    
            try:
                
                img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
                obj = filters.filters(img)
                output = None
                if(flag == True): output=obj.inversethreshold(T)
                else: output = obj.thershold(T)
                cv.imwrite("output.jpg",output)
                self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
            except Exception as e:
                self.show_error_message()
    def Custom(self):
        matrix_dialog = QDialog(MainWindow) # custom Dialog in QT 
        layout = QVBoxLayout()
        text_edit = QTextEdit(matrix_dialog) # the TextArea
        palette = QPalette() # for color and styling 
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        text_edit.setPalette(palette)
        text_edit.setLineWrapMode(QTextEdit.NoWrap)
        text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # enable scroll
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(text_edit)
        button = QPushButton('Apply', matrix_dialog,clicked=lambda:self.convertMatrix(text_edit.toPlainText())) #this button will call the convert matrix func
        layout.addWidget(button)
        matrix_dialog.setLayout(layout)
        matrix_dialog.show()
        
    def convertMatrix(self,txt):
        image_input_path =self.FileNametxt.text() # get the file location (image)
        input_txt = txt
        lines = input_txt.split('\n') #split the textarea text into rows 
        array = []
        Fraction_flag = False
        try:
            for line in lines:
                row = []
                numbers = line.split(',') # split the row into values 
                for number in numbers:
                    try:
                        x = float(number) # turn the value into floating number
                    except Exception: # failed to convert into floating number
                        try:
                            x= Fraction(number) # using the Fraction class in Python ( for ex : 4/7 , 5/7 and so on..)
                            Fraction_flag = True
                        except Exception:
                            self.show_error_message()
                            return
                    row.append(x)
                array.append(row) #build the 2D filter
            if Fraction_flag:
                array = np.array(array).astype(float) # convert the 2D filter into 2D floating values using numpy
            try:
                img = cv.imread(image_input_path,cv.IMREAD_GRAYSCALE)
                obj = filters.filters(img)
                output = obj.customFilter(array)
                cv.imwrite("output.jpg",output)
                self.img_preview.setPixmap(QtGui.QPixmap("output.jpg"))
            except Exception as e:
                self.show_error_message()
                return
        except Exception:
            self.show_error_message()
        
    def show_error_message(self):
        #display an error message in QMessageBox 
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle('Error')
        error_box.setText('An error happend!')
        error_box.addButton(QMessageBox.Ok)
        error_box.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadFileBtn.setText(_translate("MainWindow", "Open Image"))
        self.PointDetection_Btn.setText(_translate("MainWindow", "Point Detection"))
        self.HorzintalLine_Btn.setText(_translate("MainWindow", "Horizontal Line"))
        self.VerticalLine_Btn.setText(_translate("MainWindow", "Vertical Line"))
        self.F45Line_Btn.setText(_translate("MainWindow", "+45 Line"))
        self.FN45Line_Btn.setText(_translate("MainWindow", "-45 Line"))
        self.HorzintalEdge_Btn.setText(_translate("MainWindow", "Horizontal Edge"))
        self.VerticalEdge_Btn.setText(_translate("MainWindow", "Vertical Edge"))
        self.F45Edge_Btn.setText(_translate("MainWindow", "+45 Edge"))
        self.FN45Edge_Btn.setText(_translate("MainWindow", "-45 Edge"))
        self.Thershold_Btn.setText(_translate("MainWindow", "Thershold"))
        self.Laplacain_Btn.setText(_translate("MainWindow", "Laplacain"))
        self.LOG_Btn.setText(_translate("MainWindow", "LOG"))
        self.Custom_Btn.setText(_translate("MainWindow", "Custom"))
import resources_rc

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())