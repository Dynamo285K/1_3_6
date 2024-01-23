import tkinter as tk

def draw_staff(canvas, start_y):
    for i in range(5):
        canvas.create_line(50, start_y + i*20, 450, start_y + i*20)

def draw_note(canvas, note, x, y):
    canvas.create_oval(x-10, y-10, x+10, y+10, outline="black")

def draw_notes(notes):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    note_to_y = {'c': 80, 'd': 70, 'e': 60, 'f': 50, 'g': 40, 'a': 30, 'h': 20}
    staff_start = 100
    for i, note in enumerate(notes):
        if i % 16 == 0 and i > 0:
            staff_start += 120
        draw_staff(canvas, staff_start)
        draw_note(canvas, note, 50 + (i % 16) * 25, staff_start + note_to_y[note])

    root.mainloop()

with open('noty.txt', 'r') as f:
    notes = f.read().strip()
    draw_notes(notes)


