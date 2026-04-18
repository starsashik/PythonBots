import sys
import os
from time import sleep

import numpy as np
import sympy
import shutil
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap


# КЛАСС AGENT (ОСОБЬ)
class Agent:
    def __init__(self, x):
        self.X = x
        self.Y = None

    def mutate(self, strange, chast):
        """Мутация: с вероятностью chast изменяем X на ±strange"""
        if np.random.rand() <= chast:
            if np.random.rand() > 0.5:
                self.X += strange
            else:
                self.X -= strange

    def calculate(self, fun):
        """Вычисляем Y = fun(X)"""
        self.Y = fun(self.X)

    def print(self):
        print(self.X, self.Y)

    def rX(self):
        return self.X

    def rY(self):
        return self.Y


# ГЛАВНОЕ ОКНО
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем UI из файла
        uic.loadUi('main_window.ui', self)

        # Связываем кнопки с функциями
        self.StartBtn.clicked.connect(self.start)
        self.StopBtn.clicked.connect(self.stop)
        self.Slider.valueChanged.connect(self.slide)

        # Начальные настройки
        self.StopBtn.setVisible(False)
        self.Slider.setEnabled(False)
        self.count = 0
        self.is_running = False

        # Создаем папку для временных графиков
        os.makedirs('./tmp', exist_ok=True)

    def stop(self):
        """Остановка алгоритма"""
        self.is_running = False

    def start(self):
        """Главная функция запуска генетического алгоритма"""
        self.is_running = True
        self.StopBtn.setVisible(True)
        self.StartBtn.setEnabled(False)

        # Очищаем папку tmp перед запуском
        if os.path.exists('./tmp'):
            shutil.rmtree('./tmp')
        os.makedirs('./tmp', exist_ok=True)

        # Считываем параметры из интерфейса
        try:
            A = float(self.AEdit.text())
            B = float(self.BEdit.text())
            D = float(self.DEdit.text())
            tp = self.TypeBox.currentText()
            countpop = self.CountPopSB.value()
            strengMut = float(self.MutStrange.text())
            chastMut = float(self.MutChast.text())
            countos = self.CountOsSB.value()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Неверный формат данных:\n{e}")
            self.StopBtn.setVisible(False)
            self.StartBtn.setEnabled(True)
            return

        # Настройка слайдера
        self.Slider.setMaximum(countpop - 1)
        self.Slider.setEnabled(True)
        self.Slider.setValue(0)

        # Обработка введенной функции
        x = sympy.Symbol('x')
        try:
            fun = sympy.lambdify(x, self.FunEdit.text(), modules=['numpy'])
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Не удалось распознать функцию:\n{e}")
            self.StopBtn.setVisible(False)
            self.StartBtn.setEnabled(True)
            return

        # Генерация точек для графика функции (с учетом D для отображения)
        ar = np.array(self.gen_x(A - D, B + D))
        xx, y = self.get_y(fun, ar)

        # Создание первого поколения агентов
        self.agents = []
        for i in range(countos):
            par = (B - A) * np.random.rand() + A
            self.agents.append(Agent(par))
            self.agents[-1].calculate(fun)

        # Основной цикл по поколениям
        for generation in range(countpop):
            if not self.is_running:
                break

            # Рисуем график функции
            self.drawplot(xx, y)

            # Удаляем худших особей (половину)
            for _ in range(int(countos / 2)):
                if tp == 'максимум':
                    # Ищем минимум (худший для максимума)
                    min_y = float('inf')
                    index = 0
                    for idx, ag in enumerate(self.agents):
                        if ag.rY() < min_y:
                            min_y = ag.rY()
                            index = idx
                else:  # минимум
                    # Ищем максимум (худший для минимума)
                    max_y = float('-inf')
                    index = 0
                    for idx, ag in enumerate(self.agents):
                        if ag.rY() > max_y:
                            max_y = ag.rY()
                            index = idx

                # Отмечаем красной точкой удаляемую особь
                self.drawpoint(self.agents[index].rX(), self.agents[index].rY(), 'r')
                del self.agents[index]

            # Отмечаем зеленым оставшихся особей
            for ag in self.agents:
                self.drawpoint(ag.rX(), ag.rY(), 'g')

            # Сохраняем график поколения
            self.saveplt(generation)

            # Генерируем следующее поколение (копируем выживших)
            secund = 0
            current_count = len(self.agents)
            for _ in range(current_count):
                self.agents.append(Agent(self.agents[secund].rX()))
                secund += 1

            # Мутация всех особей
            for ag in self.agents:
                ag.mutate(strengMut, chastMut)
                ag.calculate(fun)

        # Показываем первое поколение
        self.show_graph(0)
        self.StopBtn.setVisible(False)
        self.StartBtn.setEnabled(True)

    def slide(self):
        """Слайдер для просмотра поколений"""
        gen_number = self.Slider.value()
        self.labelSlider.setText(f"Поколение: {str(gen_number + 1)}")
        self.show_graph(gen_number)

    def show_graph(self, name):
        """Отображение сохраненного графика"""
        filepath = f"./tmp/{name}.jpg"
        if os.path.exists(filepath):
            self.mypix = QPixmap(filepath).scaled(640, 480)
            self.Graph.setPixmap(self.mypix)

    def gen_x(self, A, B):
        """Генерация массива X от A до B с шагом 0.01"""
        shag = 0.01
        ret = []
        current = A
        while current <= B:
            ret.append(current)
            current += shag
        return ret

    def get_y(self, fun, ar):
        """Вычисление Y для массива X"""
        ret = np.zeros(len(ar))
        for ind, i in enumerate(ar):
            ret[ind] = fun(i)
        return ar, ret

    def drawplot(self, xx, y):
        """Создание графика функции"""
        plt.clf()
        self.fig = plt.figure(figsize=(6.4, 4.8), dpi=100)
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.plot(xx, y, 'b-', linewidth=2)

    def drawpoint(self, x, y, color):
        """Добавление точки на график"""
        self.ax.scatter(x, y, c=color, s=50, zorder=5)

    def saveplt(self, name):
        """Сохранение графика в файл"""
        plt.savefig(f'./tmp/{name}.jpg', dpi=100, bbox_inches='tight')
        plt.close(self.fig)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
