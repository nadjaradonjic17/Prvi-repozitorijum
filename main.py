from tkinter import *
from tkinter import font



prozor = Tk()
prozor.title("Biblioteka")
prozor.geometry("600x550")



#fontovi
naslov_font = font.Font(family="Helvetica", size=12, weight="bold")
tekst_font = font.Font(family="Helvetica", size=10)

#gornji frame
gornji_frame = Frame(prozor, bg="#ffffff", bd=2)
gornji_frame.place(relx=0.5, rely=0.05, anchor="n")

Label(gornji_frame, text="Pretraži, pozajmi, vrati ili dodaj knjigu:", font=naslov_font, bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=5)

unos = Entry(gornji_frame, width=45)
unos.grid(row=1, column=0, padx=10, pady=5)

#dugmad
dugmad_frame = Frame(gornji_frame, bg="#ffffff")
dugmad_frame.grid(row=2, column=0, columnspan=2, pady=5)

Button(dugmad_frame, text="Pretraži", width=15, command=lambda: pretrazi_knjigu()).grid(row=0, column=0, padx=5)
Button(dugmad_frame, text="Prikaži sve", width=15, command=lambda: prikazi_knjige()).grid(row=0, column=1, padx=5)
Button(dugmad_frame, text="Pozajmi", width=15, command=lambda: pozajmi_knjigu()).grid(row=1, column=0, padx=5, pady=3)
Button(dugmad_frame, text="Vrati", width=15, command=lambda: vrati_knjigu()).grid(row=1, column=1, padx=5, pady=3)

#donji frame za prikaz teksta i scrollbar
donji_frame = Frame(prozor, bg="#ffffff")
donji_frame.place(relx=0.5, rely=0.35, anchor="n")

scrollbar = Scrollbar(donji_frame)
scrollbar.pack(side=RIGHT, fill=Y)

tekst = Text(donji_frame, wrap=WORD, width=70, height=20, yscrollcommand=scrollbar.set, font=tekst_font)
tekst.pack()

scrollbar.config(command=tekst.yview)

#recnik knjiga i autora
knjige_autori = {
    "Ana Karenjina": "Lav Tolstoj",
    "Zločin i kazna": "Fjodor Dostojevski",
    "1984": "Džordž Orvel",
    "Mali princ": "Antoan de Sent-Egziperi",
    "Na Drini ćuprija": "Ivo Andrić",
    "Gospodar prstenova": "Dž. R. R. Tolkin",
    "Hari Poter i kamen mudrosti": "Dž. K. Rouling",
    "Sto godina samoće": "Gabrijel Garsija Markes",
    "Ljubav u doba kolere": "Gabrijel Garsija Markes",
    "Kad su cvetale tikve": "Dragoslav Mihailović",
    "Limeni doboš": "Ginter Gras",
    "Derviš i smrt": "Meša Selimović",
    "Tvrđava": "Meša Selimović",
    "Nečista krv": "Borisav Stanković",
    "To": "Stiven King"
}

#recnik statusa knjiga: True = dostupna, False = pozajmljena
status_knjige = {naslov: True for naslov in knjige_autori}

#prikaz svih knjiga sa statusom
def prikazi_knjige():
    tekst.delete(1.0, END)
    for naslov, autor in knjige_autori.items():
        status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
        tekst.insert(END, f"{naslov} - {autor} ({status})\n")

#pretraga knjiga
def pretrazi_knjigu():
    upit = unos.get().lower()
    tekst.delete(1.0, END)
    for naslov, autor in knjige_autori.items():
        if upit in naslov.lower():
            status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
            tekst.insert(END, f"{naslov} - {autor} ({status})\n")

#pozajmljivanje knjige
def pozajmi_knjigu():
    naslov = unos.get()
    if naslov in knjige_autori:
        if status_knjige[naslov]:
            status_knjige[naslov] = False
            tekst.insert(END, f"Knjiga '{naslov}' je uspješno pozajmljena.\n")
        else:
            tekst.insert(END, f"Knjiga '{naslov}' je već pozajmljena.\n")
    else:
        tekst.insert(END, f"Knjiga '{naslov}' ne postoji u sistemu.\n")

#vracanje knjige
def vrati_knjigu():
    naslov = unos.get()
    if naslov in knjige_autori:
        if not status_knjige[naslov]:
            status_knjige[naslov] = True
            tekst.insert(END, f"Knjiga '{naslov}' je uspješno vraćena.\n")
        else:
            tekst.insert(END, f"Knjiga '{naslov}' je već dostupna.\n")
    else:
        tekst.insert(END, f"Knjiga '{naslov}' ne postoji u sistemu.\n")

prozor.mainloop()
