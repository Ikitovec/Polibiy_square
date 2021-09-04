from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox

def code(i,alphabet):
    if alphabet != 'none':
        for row_position in range(0, len(alphabet)):
            for col_position in range(0, len(alphabet)):
                if i==alphabet[row_position][col_position]:
                    if (len(alphabet)==6):
                        if ((row_position==len(alphabet)-1)|(((row_position==len(alphabet)-2) & (col_position>2)))):
                            txt2.insert(INSERT, alphabet[0][col_position])
                        else:
                            txt2.insert(INSERT, alphabet[row_position + 1][col_position])
                    else:
                        if (row_position == len(alphabet) - 1):
                            txt2.insert(INSERT, alphabet[0][col_position])
                        else:
                            txt2.insert(INSERT, alphabet[row_position + 1][col_position])
    else:
        txt2.insert(INSERT, i)


def decode(i,alphabet):
    if alphabet !='none':
        for row_position in range(0, len(alphabet)):
            for col_position in range(0, len(alphabet)):
                if i==alphabet[row_position][col_position]:
                    if (len(alphabet) == 5):
                        if row_position==0:
                            txt2.insert(INSERT, alphabet[len(alphabet)-1][col_position])
                        else:
                            txt2.insert(INSERT, alphabet[row_position - 1][col_position])
                    else:
                        if row_position==0:
                            if (col_position<3):
                                txt2.insert(INSERT, alphabet[len(alphabet)-1][col_position])
                            if (col_position > 2):
                                txt2.insert(INSERT, alphabet[len(alphabet) - 2][col_position])
                        else:
                            txt2.insert(INSERT, alphabet[row_position - 1][col_position])
    else:
        txt2.insert(INSERT, i)

def clicked():
    txt_original = txt.get("1.0", 'end-1c')
    txt2.delete(1.0, END)

    eng_upp_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rus_upp_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if ((combo2.get() == 'Зашифровать') | (combo2.get() == 'Расшифровать')):
        for i in txt_original:
            for j in range(0, 1):
                index = eng_upp_alphabet.find(i, 0)
                if i == 'J':
                    i = 'I'
                if (index != -1):
                    alphabet = [['A', 'B', 'C', 'D', 'E'],
                                ['F', 'G', 'H', 'I', 'K'],
                                ['L', 'M', 'N', 'O', 'P'],
                                ['Q', 'R', 'S', 'T', 'U'],
                                ['V', 'W', 'X', 'Y', 'Z']]

                    break
                if (index == -1):
                    index = eng_low_alphabet.find(i, 0)
                    if i == 'j':
                        i = 'i'
                    if (index != -1):
                        alphabet = [['a', 'b', 'c', 'd', 'e'],
                                    ['f', 'g', 'h', 'i', 'k'],
                                    ['l', 'm', 'n', 'o', 'p'],
                                    ['q', 'r', 's', 't', 'u'],
                                    ['v', 'w', 'x', 'y', 'z']]
                        break
                    if (index == -1):
                        index = rus_upp_alphabet.find(i, 0)
                        if (index != -1):
                            alphabet = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
                                        ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                                        ['Л', 'М', 'Н', 'О', 'П', 'Р'],
                                        ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                                        ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                                        ['Э', 'Ю', 'Я', 'ПУСТО1', 'ПУСТО2', 'ПУСТ03']]

                            break
                        if (index == -1):
                            index = rus_low_alphabet.find(i, 0)
                            if (index != -1):
                                alphabet = [['а', 'б', 'в', 'г', 'д', 'е'],
                                            ['ё', 'ж', 'з', 'и', 'й', 'к'],
                                            ['л', 'м', 'н', 'о', 'п', 'р'],
                                            ['с', 'т', 'у', 'ф', 'х', 'ц'],
                                            ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
                                            ['э', 'ю', 'я', 'пусто1', 'пусто2', 'пусто3']]

                                break
                            if (index == -1):
                                alphabet='none'


            if combo2.get() == 'Зашифровать':
                code(i,alphabet)
            if combo2.get() == 'Расшифровать':
                decode(i,alphabet)
    else:
        messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')




window = Tk()
window.title("Квадрат Полибия")
window.geometry('500x200')


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)


txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=6)


window.mainloop()