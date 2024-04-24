#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import randint
from random import shuffle
#создание элементов интерфейса
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('memory card')
main_win.resize(700, 700)
button1 = QRadioButton('2005')
button2 = QRadioButton('2010')
button3 = QRadioButton('2015')
button4 = QRadioButton('2020')
text = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
button_ok = QPushButton('Ответить')
hline1 = QHBoxLayout()
vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
RadioGroupBox = QGroupBox('Варианты')
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()
hline4 = QHBoxLayout()
vline3 = QVBoxLayout()
text2 = QLabel('Правильно/Неправильно')
text3 = QLabel('Правильный ответ')
vline4 = QVBoxLayout()
ansGroupBox = QGroupBox('результаты тестов')
RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)
#привязка элементов к вертикальной линии
vline1.addWidget(button1)
vline1.addWidget(button2)
vline2.addWidget(button3)
vline2.addWidget(button4)
hline1.addLayout(vline1)
hline1.addLayout(vline2)
RadioGroupBox.setLayout(hline1)
hline2.addWidget(text, alignment=Qt.AlignHCenter)
hline3.addWidget(RadioGroupBox)
hline4.addWidget(button_ok, stretch=2)
vline3.addLayout(hline2)
vline3.addLayout(hline3)
vline3.addLayout(hline4)
main_win.setLayout(vline3)
vline4.addWidget(text2)
vline4.addWidget(text3)
ansGroupBox.setLayout(vline4)
hline3.addWidget(ansGroupBox)
ansGroupBox.hide()
def cluck():
    RadioGroupBox.hide()
    ansGroupBox.show()
    button_ok.setText('Следующий вопрос')
def no_vopros():
    ansGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)
def next_question():
    chislo = randint(0,len(question_list)-1)
    peremennaya = question_list[chislo]
    ask(peremennaya)
    main_win.total += 1
    print('задано вопросов:', main_win.total)
    print('отвечено правильно на', main_win.score, 'вопросов')
def o_nachale_testa():
    if button_ok.text()== 'Ответить':
        proverka_otveta()
    else:
        next_question()
answers = [button1, button2, button3, button4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong3)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong1)
    text.setText(q.question)
    text3.setText(q.right_answer)
    no_vopros()
def proverka_otveta():
    if answers[0].isChecked():
        show_corect('Правильно')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corect('Не правильно')   
def show_corect(res):
    text2.setText(res)
    cluck()
question_list = []
question_list.append(Question('На каком языке разговаривают в Бразилии', 'Португальский', 'Бразильский', 'Английский', 'Воображаемый'))
question_list.append(Question('Кто такой Гагарин', 'Космонавт','Художник','Поэт', 'Дворник' ))
question_list.append(Question('Сколько зим в году?', '2', '1', '3', '100'))
question_list.append(Question('За какое число подписчиков дают рубиновую кнопку на ютубе', '40млн', '50млн', '10млн', '100млн'))
question_list.append(Question('Где придумали лего?','Дания','Франция', 'США', 'Великобритания'))
question_list.append(Question('Сколько линий метро не считая линии a и диаметров?', '15', '10', '20', '17'))
question_list.append(Question('Самая густонаселенная страна?', 'Индия', 'Китай', 'Япония', 'Россия'))
question_list.append(Question('В каких стране начало недели начинается с воскресения?', 'Канада', 'Россия','Казахстан', 'Ни в какой'))
question_list.append(Question('Сколько всего знаков зодиака?', '12', '15', '10', '11'))
question_list.append(Question('Какую команду в Python изучают в начале?', 'print', 'input', 'append', 'left()'))
question_list.append(Question('Что запустили в космос на юпитер на корабле "Юнона"?', 'лего фигурки', 'камни', 'еду', 'игрощечную собаку'))
main_win.total = 0
main_win.score = 0
next_question()
button_ok.clicked.connect(o_nachale_testa)
main_win.show()
app.exec_()
