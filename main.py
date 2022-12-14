from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from design import report_prog
import sys
import csv
import os

from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
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
        self.ui.comboBox.activated.connect(self.idSorting)
        self.ui.comboBox_2.activated.connect(self.dataParsing)

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
        # print(fname)
        self.exportToExcel(fname)

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

        self.dataParsing()

    def dataParsing(self):
        dirId = self.directory + "/ID/" + self.ui.comboBox.currentText()
        dirTemp = self.directory + "/Temp/" + self.ui.comboBox.currentText()
        dirStage = self.directory + "/Stage/" + self.ui.comboBox.currentText()

        fileId = open(dirId, encoding = "utf-8")
        fileTemp = open(dirTemp, encoding="utf-8")
        fileStage = open(dirStage, encoding="utf-8")

        readerId = csv.reader(fileId)
        readerTemp = csv.reader(fileTemp)
        readerStage = csv.reader(fileStage)

        listId = []
        listTemp = []
        listStage = []
        for x in readerId:
            listId.append(x)
        for x in readerTemp:
            listTemp.append(x)
        for x in readerStage:
            listStage.append(x)

        count = 0
        self.data = [[], [], [], []]
        for i in range(len(listId)):
            if listId[i][2]==self.ui.comboBox_2.currentText():
                self.data[0].append(count)
                count+=1
                self.data[1].append(listTemp[i][2])
                self.data[2].append(listId[i][1])
                self.data[3].append(listStage[i][2])

        for x in self.data:
            print(x)

    def exportToExcel(self, dir):
        wb = Workbook()
        wb.create_sheet(title="Отчет", index=0)
        sheet = wb["Отчет"]

        sheet['A1'] = "Отчет"
        sheet['B1'] = "ID: "+self.ui.comboBox_2.currentText()

        for x in range(len(self.data[0])):
            cell = sheet.cell(row = x+24, column=1)
            cell.value = self.data[0][x]
            cell = sheet.cell(row=x + 24, column=2)
            cell.value = float(self.data[1][x])
            cell = sheet.cell(row=x + 24, column=3)
            cell.value = self.data[2][x]
            cell = sheet.cell(row=x + 24, column=4)
            cell.value = self.data[3][x]

        chart = LineChart()
        chart.title = "Отчет"
        dataChart = Reference(sheet, min_col=2, min_row=24, max_col=2, max_row=len(self.data[0])+23)

        chart.add_data(dataChart, titles_from_data=True)
        sheet.add_chart(chart, 'A5')
        wb.save(dir)












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
