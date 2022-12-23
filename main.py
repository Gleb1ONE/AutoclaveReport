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
import random
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


    def btnOpen(self):  # Кнопка открыть
        #fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home', '*.csv;;')[0]
        fname = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print(fname)
        self.fileSorting(fname)
        #self.plot()

    def btnSave(self):  # Кнопка сохранить
        fname = QFileDialog.getSaveFileName(self, 'Открыть файл', '/home', '*.pdf')[0]
        print(fname)

    def fileSorting(self, directory):   # Берем в директории + /ID файлы и отправляем в выпадающий список
        directory = directory + "/ID"
        files = os.listdir(directory)

        hystoryFiles = list(filter(lambda x: x.endswith('.csv'), files))
        self.ui.comboBox.addItems(hystoryFiles)



    def plot(self): # Строим график
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.ui.figure.clear()

        # create an axis
        ax = self.ui.figure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.ui.canvas.draw()



app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())

# **************************** Обработка графиков ***************

# def openFile(file):
#     #Открытие CSV файла
#     doc_input = open(file)
#     file = doc_input.read()     #чтение файла в переменную
#     doc_input.close()
#
#
#     list = file.replace(';','\n')   #Замена ';' на переносы строк
#     list = list.splitlines()    # Разбиение list по переносу
#
#
#     for x in range(len(list)):  #Разброс температуры и времени по четности
#         if x % 2 == 0:
#             time_graph.append(list[x])
#         else:
#             temperature_graph.append(list[x])
#
#     time_graph.pop(0)       #Удаление заголовка
#     temperature_graph.pop(0)
#
#     for i in range(len(temperature_graph)): #Перевод температуры в формат с плавающей точкой
#         temperature_graph[i] = temperature_graph[i].replace(',', '.')
#         temperature_graph[i] = float(temperature_graph[i])

# def initGraph(time, temperature):
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#
#     #ax.set_xlim([-10, 10])
#     ax.set_ylim([10, 150])
#     ax.set_title('График')
#     ax.set_xlabel('Время')
#     ax.set_ylabel('Температура')
#
#     ax.plot(time, temperature)
#     plt.show()