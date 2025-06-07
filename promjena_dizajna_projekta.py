from tkinter import *
from tkinter import ttk
from tkinter import font

# Glavni prozor
prozor = Tk()
prozor.title("Biblioteka")
prozor.geometry("650x600")
prozor.configure(bg="#f2f2f2")

# Fontovi
naslov_font = font.Font(family="Helvetica", size=14, weight="bold")
tekst_font = font.Font(family="Helvetica", size=10)

# Gornji deo – unos i naslov
frame_top = Frame(prozor, bg="#f2f2f2")
frame_top.pack(pady=20)

Label(frame_top, text="Pretraži, pozajmi, vrati ili dodaj knjigu:", font=naslov_font, bg="#f2f2f2").pack()

unos = ttk.Entry(frame_top, width=50)
unos.pack(pady=10)

# Dugmad
frame_dugmad = Frame(prozor, bg="#f2f2f2")
frame_dugmad.pack(pady=10)

ttk.Button(frame_dugmad, text="Pretraži", width=18, command=lambda: pretrazi_knjigu()).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_dugmad, text="Prikaži sve", width=18, command=lambda: prikazi_knjige()).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_dugmad, text="Pozajmi", width=18, command=lambda: pozajmi_knjigu()).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame_dugmad, text="Vrati", width=18, command=lambda: vrati_knjigu()).grid(row=1, column=1, padx=5, pady=5)

# Donji deo – tekst i skrol
frame_tekst = Frame(prozor, bg="#f2f2f2")
frame_tekst.pack(pady=20, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame_tekst)
scrollbar.pack(side=RIGHT, fill=Y)

tekst = Text(frame_tekst, wrap=WORD, width=75, height=20, yscrollcommand=scrollbar.set, font=tekst_font, bg="#ffffff", bd=1, relief="solid")
tekst.pack(padx=10, pady=10)

scrollbar.config(command=tekst.yview)

# Podaci
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

status_knjige = {naslov: True for naslov in knjige_autori}

# Funkcije
def prikazi_knjige():
    tekst.delete(1.0, END)
    for naslov, autor in knjige_autori.items():
        status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
        tekst.insert(END, f"{naslov} - {autor} ({status})\n")

def pretrazi_knjigu():
    upit = unos.get().lower()
    tekst.delete(1.0, END)
    for naslov, autor in knjige_autori.items():
        if upit in naslov.lower():
            status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
            tekst.insert(END, f"{naslov} - {autor} ({status})\n")

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
