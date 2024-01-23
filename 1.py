import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, width=500,height=500, bg= 'white')
canvas.pack()


new_rect = canvas.create_rectangle(250,250,250+1,250+1, fill = 'black')
x1,y1,x2,y2 = canvas.bbox(new_rect)
move = [0,1]
listik = []

def move_snake():
    global x1,y1
    if [x1,y1] in listik:
        return
    r = canvas.create_rectangle(x1 ,y1,x1 + 1,y1 + 1)
    listik.append([x1,y1])
    x1 += move[0]
    y1 += move[1]
    print(x1,y1)

    canvas.after(100,move_snake)

def changer(e):
    global move
    if e.char == ('d'):
        move = [1,0]
    elif e.char == ('a'):
        move = [-1,0]
    elif e.char == ('s'):
        move = [0,1]
    elif e.char == ('w'):
        move = [0,-1]

move_snake()
root.bind("<KeyPress>",changer)
root.mainloop()
