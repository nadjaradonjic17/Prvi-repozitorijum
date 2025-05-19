from tkinter import *

# Rječnik knjiga i autora
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

# Rječnik statusa knjiga: True = dostupna, False = pozajmljena
status_knjige = {naslov: True for naslov in knjige_autori}

# Prikaz svih knjiga sa statusom
def prikazi_knjige():
    tekst.delete(1.0, END)
    for naslov, autor in knjige_autori.items():
        status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
        tekst.insert(END, f"{naslov} - {autor} ({status})\n")

# Pretraga knjiga
def pretrazi_knjigu():
    upit = unos.get().lower()
    tekst.delete(1.0, END)
    for naslov, autor in knjige_autori.items():
        if upit in naslov.lower():
            status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
            tekst.insert(END, f"{naslov} - {autor} ({status})\n")

# Pozajmljivanje knjige
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

# Vraćanje knjige
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

# GUI prozor
prozor = Tk()
prozor.title("Biblioteka")
prozor.geometry("550x500")

Label(prozor, text="Pretraži, pozajmi ili vrati knjigu:").pack()
unos = Entry(prozor, width=50)
unos.pack(pady=5)

Button(prozor, text="Pretraži", command=pretrazi_knjigu).pack(pady=2)
Button(prozor, text="Prikaži sve knjige", command=prikazi_knjige).pack(pady=2)
Button(prozor, text="Pozajmi knjigu", command=pozajmi_knjigu).pack(pady=2)
Button(prozor, text="Vrati knjigu", command=vrati_knjigu).pack(pady=2)

tekst = Text(prozor, wrap=WORD, width=65, height=20)
tekst.pack(pady=10)

prozor.mainloop()
