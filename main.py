from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from design import report_prog
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = report_prog.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.btnOpen)
        self.ui.pushButton_2.clicked.connect(self.btnSave)


    def btnOpen(self):
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home', '*.csv;;')[0]
        print(fname)

    def btnSave(self):
        fname = QFileDialog.getSaveFileName(self, 'Открыть файл', '/home', '*.pdf')[0]
        print(fname)


app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())

# **************************** Обработки графиков ***************

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