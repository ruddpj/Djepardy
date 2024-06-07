from tkinter import*

root = Tk(className="Djepardy")
canvas = Canvas(width=1920, height=1080)
canvas.pack()

x = 0
c_box = "blue"
c_text = "yellow"
f_size = "Arial 32"

cat = []
file_1 = open("djepardy_q.txt", "r", encoding="utf8")
for k in range(6):
    o = file_1.readline()
    cat.append(o)
file_1.close()


def opener(ans, t):
    file = open("djepardy_q.txt", "r", encoding="utf8")
    answer = file.readlines()[ans]
    file.close()
    new = Toplevel(root)
    new.geometry("600x600")
    text = Text(new, bg="blue", wrap=WORD, font="Arial 42", fg="yellow")
    text.insert(INSERT, answer)
    text.pack()
    canvas.itemconfig(f"box{t}", fill="gray")
    canvas.itemconfig(f"text{t}", fill="silver")


def cords(get):
    a = get.x
    b = get.y
    if a in range(0, 320):
        c = 0
    elif a in range(321, 640):
        c = 1
    elif a in range(640, 960):
        c = 2
    elif a in range(961, 1280):
        c = 3
    elif a in range(1281, 1600):
        c = 4
    else:
        c = 5
    question(c, b)


def question(m, n):
    if n > 99:
        if n in range(100, 280):
            p = 0
        elif n in range(281, 460):
            p = 1
        elif n in range(461, 640):
            p = 2
        elif n in range(641, 820):
            p = 3
        else:
            p = 4
        u = (m*5)+p+6
        s = f"{m}{p}"
        opener(u, s)


for i in range(6):
    y = 0
    canvas.create_rectangle(x, y, x+320, y+180, fill=c_box)
    canvas.create_text(x+160, y+75, text=cat[i], fill=c_text, font=f_size)
    y += 100
    for j in range(5):
        canvas.create_rectangle(x, y, x+320, y+180, fill=c_box, tags=f"box{i}{j}")
        canvas.create_text(x+160, y+90, text=str((j+1)*100), fill=c_text, font=f_size, tags=f"text{i}{j}")
        y += 180
    x += 320

canvas.bind("<Button-1>", cords)

root.mainloop()
