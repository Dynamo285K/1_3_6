import tkinter as tk
import keyboard

fr = open('zastavky.txt','r',encoding='utf-8')
x = fr.readlines()
listik = []
for i in x:
    listik.append(i.strip())
print(listik)
counter = 0


def move_text():
    global counter
    canvas.move(text_id, -5, 0)

    x, y = canvas.coords(text_id)
    x1,y1,x2,y2 = canvas.bbox(text_id)

    if keyboard.is_pressed('q'):
        canvas.coords(text_id, 300+(x2-x1), y)
        canvas.itemconfig(text_id, text=listik[counter])
        counter += 1
    elif x2 < 0:
        canvas.coords(text_id, 300+(x2-x1), y)
        if counter == len(listik) - 1:
            canvas.itemconfig(text_id, text=listik[counter] + ',posledna zastavka prosim vystupte!')
        else:
            canvas.itemconfig(text_id, text=listik[counter])
            counter += 1


    root.after(50, move_text)


root = tk.Tk()
root.title("Move Text on Canvas")

canvas = tk.Canvas(root, width=300, height=50, bg='black')
canvas.pack()

initial_text = 'start'

text_id = canvas.create_text(500, 25,fill = 'red', text=initial_text, font=('Helvetica', 14), anchor='e')

move_text()

root.mainloop()


