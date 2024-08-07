from tkinter import*

root = Tk(className="Djepardy")
canvas = Canvas(width=1920, height=1080)
canvas.pack()

x = 0
c_box = "blue"
c_text = "yellow"
f_size = "Arial 32"

cat = []
file_1 = open("djepardy_themes.txt", "r", encoding="utf8")
for k in range(6):
    o = file_1.readline()
    cat.append(o)
file_1.close()


def button_sel(get, cc, aq):
    a = get.x
    b = get.y
    if 870 <= a <= 1050:
        if 800 <= b <= 860:
            cc.delete("all")
            Misc.lift(canvas)
        elif 900 <= b <= 960:
            cc.create_text(960, 600, text=aq, fill="yellow", font="Arial 24")
            

def opener(ans, t):
    file = open(f"questions/{ans+1}.txt", "r", encoding="utf8")
    arr = file.readlines()
    file.close()
    qtion = arr[t*2]
    answer = arr[t*2+1]
    new = Canvas(width=1920, height=1080, bg="blue")
    new.place(x=0, y=0)
    new.create_rectangle(870, 800, 1050, 860, fill="yellow", outline="black")
    new.create_text(960, 830, text="CLOSE", fill="blue", font=f_size)
    new.create_rectangle(870, 900, 1050, 960, fill="yellow", outline="black")
    new.create_text(960, 930, text="SHOW", fill="blue", font=f_size)
    new.create_text(960, 300, text=qtion, fill="yellow", font="Arial 24")
    canvas.itemconfig(f"box{ans}{t}", fill="gray")
    canvas.itemconfig(f"text{ans}{t}", fill="silver")
    new.bind("<Button-1>", lambda event: button_sel(event, new, answer))


def cords(get):
    a = get.x
    b = get.y
    if b > 100:
        if 0 < a <= 320:
            c = 0
        elif 320 < a <= 640:
            c = 1
        elif 640 < a <= 960:
            c = 2
        elif 960 < a <= 1280:
            c = 3
        elif 1280 < a <= 1600:
            c = 4
        else:
            c = 5

        if 100 < b <= 280:
            d = 0
        elif 280 < b <= 460:
            d = 1
        elif 460 < b <= 640:
            d = 2
        elif 640 < b <= 720:
            d = 3
        else:
            d = 4
            
        opener(c, d)


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
