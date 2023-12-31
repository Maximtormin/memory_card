#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
app = QApplication([])
window = QWidget()

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

questions_list = []
questions_list.append(Question('Какая песня группы Nirvana являеться самой популярной?', 'Smells like teen spirit', 'Polly', 'Come as you are' ,'Lithium'))
questions_list.append(Question('Самый успешный альбом группы Nirvana', 'Nevermind', 'In Utero', 'Bleach', 'Stop'))
questions_list.append(Question('Кто являлся вокалистом группы "Кино"', 'Виктор Цой', 'Игорь Тихомиров' ,'Юрий Каспарян', 'Георгий Гурьянов'))
questions_list.append(Question('Основатель группы The Beatles', 'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон' ,'Ринго Старр'))
questions_list.append(Question('Сколько было лет на момент самоубийства лидера Nirvana, Курту Кобейну?', '27', '56', '39', '32'))
questions_list.append(Question('Основатель группы Metallica', 'Джеймс Хэтфилд', 'Рон Макговни' ,'Кирк Хэмметт', 'Клифф Бёртон'))
questions_list.append(Question('hhf', 'fsfs', 'gfhfs', 'fsfghfs' ,'fshfjfs'))
questions_list.append(Question('fqsfs', 'fsfLGs', 'f45Ysfs', 'fsfKGs', 'fsfNFs'))
questions_list.append(Question('fsfGKs', 'FKLfsfsL', 'fFJsfs' ,'FJJfsfs', 'GKfsfs'))
questions_list.append(Question('fsfGKs', 'FKLfsfsL', 'fFJsfs' ,'FJJfsfs', 'GKfsfs'))

btn_OK = QPushButton ('Ответить')
lb_Question = QLabel ('В каком году была основана Москва?')
RadioGroupBox = QGroupBox ('Варианты ответов')
rbtn_1 = QRadioButton ('1147')
rbtn_2 = QRadioButton ('1242')
rbtn_3 = QRadioButton ('1861')
rbtn_4 = QRadioButton ('1943')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1= QHBoxLayout()
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch (1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout ()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addSpacing(5)
layout_card.addLayout(layout_line3, stretch=8)
window.setLayout(layout_card)

#ltym2
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('следуйщий вопрос')
    
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:',window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')

def next_question():
    '''window.cur_question = window.cur_question + 1'''
    window.total += 1
    print('Статистика\n-Всего вопросов:',window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    '''if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]'''
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.setLayout(layout_card)
window.setWindowTitle('memory card')
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()