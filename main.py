from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from design import report_prog
import sys
import csv
import os
#---------------------------------------------------------------------------
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#---------------------------------------------------------------------------

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()      # Подключение интерфейса программы
        self.ui = report_prog.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnOpen)
        self.ui.pushButton_2.clicked.connect(self.btnSave)
    # ---------------------------------------------------------------------------
        self.ui.figure = plt.figure()       # Создаем фигуру графика
        self.ui.canvas = FigureCanvas(self.ui.figure)   # Поле для графика
        #self.ui.toolbar = NavigationToolbar(self.ui.canvas, self)   # Панель управления графика
        layout = QVBoxLayout()  # создаем контейнер и добавляем в него поле и тулбар
        #layout.addWidget(self.ui.toolbar)
        layout.addWidget(self.ui.canvas)

        self.ui.widget.setLayout(layout)    # добавление контейнера в интерфейс
        self.directory = ""
        self.data = [[],[],[],[]]   # [№], [температура], [время], [стадия]


    def btnOpen(self):  # Кнопка открыть
        #fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home', '*.csv;;')[0]
        self.directory = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.fileSorting()

    def btnSave(self):  # Кнопка сохранить
        fname = QFileDialog.getSaveFileName(self, 'Открыть файл', '/home', '*.xlsx')[0]
        print(fname)

    def fileSorting(self):   # Берем в директории + /ID файлы и отправляем в выпадающий список
        directoryId = self.directory + "/ID"
        files = os.listdir(directoryId)

        hystoryFiles = list(filter(lambda x: x.endswith('.csv'), files))
        self.ui.comboBox.addItems(hystoryFiles)
        self.idSorting()

    def idSorting(self):
        directoryId = self.directory + "/ID/" + self.ui.comboBox.currentText()
        fileId = open(directoryId, encoding="utf-8")

        readerId = csv.reader(fileId)

        hystoryList = []
        count = 0
        for x in readerId:
            if count == 0:
                pass
            else:
                if not x[2] in hystoryList:
                    hystoryList.append(x[2])
            count += 1

        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(hystoryList)

        fileId.close()

    def dataParsing(self):
        fileId = self.directory + "/ID/" + self.ui.comboBox.currentText()
        fileTemp = self.directory + "/Temp/" + self.ui.comboBox.currentText()
        fileStage = self.directory + "/Stage/" + self.ui.comboBox.currentText()







    # def plot(self): # Строим график
    #     # random data
    #     data = [random.random() for i in range(10)]
    #
    #     # clearing old figure
    #     self.ui.figure.clear()
    #
    #     # create an axis
    #     ax = self.ui.figure.add_subplot(111)
    #
    #     # plot data
    #     ax.plot(data, '*-')
    #
    #     # refresh canvas
    #     self.ui.canvas.draw()



app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())
