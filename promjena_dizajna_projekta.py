import customtkinter as ctk


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

prozor = ctk.CTk()
prozor.title("📚 Biblioteka")
prozor.geometry("700x600")

naslov_font = ("Helvetica", 16, "bold")
tekst_font = ("Helvetica", 12)

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
    "To": "Stiven King",
    "Mali čovek, veliki grad": "Alfred Döblin",
    "Ponos i predrasude": "Džejn Ostin",
    "Lovac u žitu": "Dž. D. Selindžer",
    "Na zapadu ništa novo": "Erich Maria Remarque",
    "Veliki Getsbi": "F. Skot Ficdžerald",
    "Zov divljine": "Džek London",
    "Mrtve duše": "Nikolaj Gogolj",
    "Braća Karamazovi": "Fjodor Dostojevski",
    "Božanstvena komedija": "Dante Aligijeri",
    "Čarobnjak iz Oza": "L. Frank Baum"
}

status_knjige = {naslov: True for naslov in knjige_autori}  # True = dostupna

trenutno_prikazane_knjige = list(knjige_autori.items())

dobrodoslica = ctk.CTkLabel(prozor, text="Dobrodošli u našu biblioteku!", font=naslov_font)
dobrodoslica.pack(pady=(20, 5))

unos = ctk.CTkEntry(prozor, width=400, placeholder_text="Unesi naziv knjige ili autora...")
unos.pack(pady=(0, 10))

frame_dugmad = ctk.CTkFrame(prozor)
frame_dugmad.pack(pady=10)

def prikazi_knjige():
    global trenutno_prikazane_knjige
    trenutno_prikazane_knjige = list(knjige_autori.items())
    tekstbox.delete("1.0", "end")
    for naslov, autor in trenutno_prikazane_knjige:
        status = "✅ Dostupna" if status_knjige[naslov] else "❌ Pozajmljena"
        tekstbox.insert("end", f"{naslov} - {autor} ({status})\n")

def pretrazi_knjigu():
    global trenutno_prikazane_knjige
    upit = unos.get().lower()
    trenutno_prikazane_knjige = []
    tekstbox.delete("1.0", "end")
    for naslov, autor in knjige_autori.items():
        if upit in naslov.lower() or upit in autor.lower():
            trenutno_prikazane_knjige.append((naslov, autor))
            status = "✅ Dostupna" if status_knjige[naslov] else "❌ Pozajmljena"
            tekstbox.insert("end", f"{naslov} - {autor} ({status})\n")
    if not trenutno_prikazane_knjige:
        tekstbox.insert("end", "⚠️ Nema knjiga koje odgovaraju pretrazi.\n")

ctk.CTkButton(frame_dugmad, text="Pretraži", command=pretrazi_knjigu, width=150).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="Prikaži sve", command=prikazi_knjige, width=150).grid(row=0, column=1, padx=10, pady=5)


def otvori_pozajmljivanje_prozor():
    poz_prozor = ctk.CTkToplevel(prozor)
    poz_prozor.title("Pozajmi knjige")
    poz_prozor.geometry("500x500")

    poz_prozor.grab_set()  

    checkbox_frame = ctk.CTkScrollableFrame(poz_prozor, width=480, height=400)
    checkbox_frame.pack(pady=10)

    check_var_map = {}

    
    for naslov, autor in trenutno_prikazane_knjige:
        if status_knjige[naslov]:
            var = ctk.BooleanVar()
            chk = ctk.CTkCheckBox(checkbox_frame, text=f"{naslov} - {autor}", variable=var)
            chk.pack(anchor="w", pady=3, padx=10)
            check_var_map[naslov] = var

    def potvrdi_pozajmljivanje():
        broj = 0
        for naslov, var in check_var_map.items():
            if var.get():
                status_knjige[naslov] = False
                tekstbox.insert("end", f"📕 Pozajmljena: {naslov}\n")
                broj += 1
        if broj == 0:
            tekstbox.insert("end", "⚠️ Niste izabrali nijednu knjigu za pozajmljivanje.\n")
        else:
            poz_prozor.destroy()

    ctk.CTkButton(poz_prozor, text="📥 Potvrdi pozajmljivanje", command=potvrdi_pozajmljivanje).pack(pady=10)

ctk.CTkButton(frame_dugmad, text="Pozajmi", command=otvori_pozajmljivanje_prozor, width=150).grid(row=1, column=0, padx=10, pady=5)


def otvori_vracanje_prozor():
    vrati_prozor = ctk.CTkToplevel(prozor)
    vrati_prozor.title("Vrati pozajmljene knjige")
    vrati_prozor.geometry("500x500")

    vrati_prozor.grab_set()  

    checkbox_frame = ctk.CTkScrollableFrame(vrati_prozor, width=480, height=400)
    checkbox_frame.pack(pady=10)

    check_var_map = {}

    for naslov, dost in status_knjige.items():
        if not dost:
            var = ctk.BooleanVar()
            chk = ctk.CTkCheckBox(checkbox_frame, text=f"{naslov} - {knjige_autori[naslov]}", variable=var)
            chk.pack(anchor="w", pady=3, padx=10)
            check_var_map[naslov] = var

    def potvrdi_vracanje():
        broj = 0
        for naslov, var in check_var_map.items():
            if var.get():
                status_knjige[naslov] = True
                tekstbox.insert("end", f"🔄 Vraćena: {naslov}\n")
                broj += 1
        if broj == 0:
            tekstbox.insert("end", "⚠️ Niste izabrali nijednu knjigu za vraćanje.\n")
        else:
            vrati_prozor.destroy()

    ctk.CTkButton(vrati_prozor, text="🔁 Potvrdi vraćanje", command=potvrdi_vracanje).pack(pady=10)

ctk.CTkButton(frame_dugmad, text="Vrati", command=otvori_vracanje_prozor, width=150).grid(row=1, column=1, padx=10, pady=5)

tekstbox = ctk.CTkTextbox(prozor, width=650, height=300, font=tekst_font)
tekstbox.pack(pady=10)

prikazi_knjige()

prozor.mainloop()