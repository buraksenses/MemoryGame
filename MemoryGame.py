from random import *
import time
from tkinter import *
import tkinter.font

app = Tk()
app.title("Memory Game")
app.geometry("400x400")
app.resizable(width="false", height="false")
app.configure(bg='red')

sayac = 0
numbers = [0, 0, 0, 0, 0]
gameCount = 5
labelFont = tkinter.font.Font(family="Arial", size=15, weight='bold')
lblShowNumbers = Label(app, height="2", width="2",bg='red')
lblShowNumbers['font'] = labelFont

def btnKaydetOnClick():
    global gameCount
    global numbers

    btnKaydet.pack_forget()
    lblInput.pack_forget()
    lblWarning.pack_forget()
    userInput.pack_forget()


    temp = userInput.get()
    tempList = temp.split()

    if len(tempList) != gameCount:
        gameCount = 5
        lblBitti.pack()
        btnYeniden.pack()
        btnKapat.pack()
        userInput.delete(0, 'end')
        return
    for j in range(gameCount):
        if int(tempList[j]) != numbers[j]:
            gameCount = 5
            lblBitti.pack()
            btnYeniden.pack()
            btnKapat.pack()
            userInput.delete(0, 'end')
            return
    userInput.delete(0, 'end')
    lblDogru.pack()
    gameCount = gameCount + 1
    numbers.append(0)
    btnSonraki.pack()


def btnBaslatOnClick():
    global sayac
    global gameCount
#region Sayıları ekrana bastıran kısım
    while sayac < gameCount:
        btnBaslat.destroy()
        numbers[sayac] = randrange(1, 100)
        lblShowNumbers.place(x=randrange(1, 300), y=randrange(1, 300))
        lblShowNumbers.config(text=str(numbers[sayac]))
        app.update()
        time.sleep(1.5)
        sayac = sayac + 1
        if sayac == gameCount:
            lblShowNumbers.place_forget()
#endregion
    sayac = 0
    lblInput.pack()
    userInput.pack()
    lblWarning.pack()
    btnKaydet.pack()


def btnYenidenOnClick():
    btnKapat.pack_forget()
    btnYeniden.pack_forget()
    lblBitti.pack_forget()
    btnBaslatOnClick()

def btnSonrakiOnClick():
    btnSonraki.pack_forget()
    lblDogru.forget()
    btnBaslatOnClick()

def btnKapatOnClick():
    app.destroy()

##Başlat butonu
btnBaslat = Button(app, text="Start Game!", fg="blue", bg="maroon", padx="10", pady="20", command=btnBaslatOnClick)
btnBaslat.place(x=150, y=150)

##Cevap butonu
btnKaydet = Button(app,text="Answer!", fg="blue", bg="maroon", padx="5", pady="10", command=btnKaydetOnClick)

##Oyun bitti labeli
lblBitti = Label(app, text="Game Over!", bg="red", height="2", width="20")

##Doğru cevap labeli
lblDogru = Label(app, text="Correct!", bg="red", height="2", width="20")

##Bilgilendirme
lblInput = Label(app, height="2", width="50", bg='red', text="Enter the numbers shown in the correct order!")
lblWarning = Label(app, height="1", width="20", text="Example: 5 17 21 87 64...", bg="red")

##Yeniden dene butonu
btnYeniden = Button(app, text="Try Again!", fg="blue", bg="maroon", padx="5", pady="10", command=btnYenidenOnClick)

##Sonraki seviye butonu
btnSonraki = Button(app, text="Next Level", fg="blue", bg="maroon", padx="5", pady="10", command=btnSonrakiOnClick)

##Oyunu kapatma butonu
btnKapat = Button(app, text="Exit Game", fg="blue", bg="maroon", padx="5", pady="10", command=btnKapatOnClick)

##Kullanıcı girişi
userInput = Entry(app, width=50)

app.mainloop()