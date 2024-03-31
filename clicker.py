# Импортируем функции из библиотеки tkinter
from tkinter import *
from tkinter import ttk

#И мпортируем функцию Timer для запуска указаной функции через определенное время 
from threading import Timer

# Задаем изначальные значения переменных
clicks = 0
add = 1
cost = 50
auto = 0
history = 0

uc10 = (add * cost * 2 + cost * 9) * 5
uc100 = (add * cost * 2 + cost * 9) * 50
cost_aut = 100 + 1000 * auto

# Функция для обновления данных
def update():
    global uc10,uc100,cost_aut
    
    uc10 = (add * cost * 2 + cost * 9) * 5
    uc100 = (add * cost * 2 + cost * 9) * 50
    cost_aut = 100 + 1000 * auto
    btn["text"] = f"Очки - {clicks}" 
    btnadd['text'] = f"Улучшить - {cost * add}"
    btnadd10['text'] = f"Улучшить X 10 - {uc10}"
    btnadd100['text'] = f"Улучшить X 100 - {uc100}"
    btnauadd['text'] = f'Улучшить Автоматичность - {cost_aut}'
    t2['text'] = f'Скорость - {add}'
    t1['text'] = f'Очки за все время - {history}'  
    t3['text'] =  f'Автоматическая скорость - {auto}'

# Функции кнопок    
def click_button():
    global clicks, add, history 
    clicks += add
    history += add
    update()

def add_num():
    global add,clicks,cost
    if clicks >= cost * add:
        clicks -= cost * add
        add += 1
        update()

        
def add_num_ten():
    global add,clicks,uc10
    if clicks >= uc10:
        clicks -= uc10
        add += 10
        update()

def add_num_hundred():
    global add,clicks,uc100
    if clicks >= uc100:
        clicks -= uc100
        add += 100
        update()
        
def auto_count():
    global auto, clicks, history
    clicks = round(clicks + auto, 1)
    history = round(history + auto, 1)
    update()
    Timer(1.0, auto_count).start()
       
def add_auto():
    global auto, clicks
    if clicks >= cost_aut:
        clicks -= cost_aut
        auto = round(auto + 0.1, 1)
        update()
                  
def cheat(event):
    global clicks, history
    clicks += 100000000000000
    history += 100000000000000
    update()
    
def clear():
    global clicks,add,cost,auto,history
    clicks = 0
    add = 1
    cost = 50
    auto = 0
    history = 0
    update()
        

# Параметры окна
root = Tk()
root.title(f"CLICKER")
root.geometry("350x450+950+400")
root.resizable('False', 'False')

# Создаем виджеты и добавляем их в окно
t1 = ttk.Label(text=f'Очки за все время - {history}')
t1.pack()

t2 = ttk.Label(text=f'Скорость - {add}')
t2.pack()

t3 = ttk.Label(text = f'Автоматическая скорость - {auto}')
t3.pack()

btn = ttk.Button(text="Нажми меня", command=click_button, )
btn.pack(fill=X)

btnadd = ttk.Button(text = f"Улучшить - {cost * add}", command=add_num)
btnadd.pack(fill=X)

btnadd10 = ttk.Button(text=f"Улучшить X 10 - {uc10}", command=add_num_ten)
btnadd10.pack(fill = X)

btnadd100 = ttk.Button(text = f"Улучшить X 100 - {uc100}", command = add_num_hundred)
btnadd100.pack(fill = X)

btnauadd = ttk.Button(text=f'Улучшить Автоматичность - {cost_aut}', command=add_auto)
btnauadd.pack(fill=X)

btnclear = ttk.Button(text='Очистить все!', command=clear)
btnclear.pack(fill=X)

btn.bind("<ButtonPress-2>", cheat)


auto_count() # Запускаем функцию в первый раз, для запуска цикла
root.mainloop() # Необходимо для работы