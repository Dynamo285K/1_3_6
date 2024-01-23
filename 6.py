import tkinter as tk
root = tk.Tk()
H = 500
W = 500

canvas = tk.Canvas(root, height=H,width=W,bg='white')
canvas.pack()

fr = open('noty.txt','r',encoding='utf-8')
noty = fr.readline().strip()
print(noty)

note_to_y = {'c': 45, 'd': 40, 'e': 35, 'f': 30, 'g': 25, 'a': 20, 'h': 15}

y = 20
counter = 0
f = -1

def ciary(y):
    for i in range(5):
        canvas.create_line(0,y+10*i,500,y+10*i)

def draw_notes(y, counter):
    global f
    while counter < len(noty):
        f += 1
        counter += 1
        nota = noty[counter-1]
        if 20 + 20 * f > W or 30 + 20 * f + 10 > W:
            y += 150
            f = 0
            ciary(y)
        else:
            canvas.create_oval(20 + 20*f,y + note_to_y[nota],30 + 20*f+10,y + note_to_y[nota]+10)
    return

ciary(y)
draw_notes(y,counter)

root.mainloop()

