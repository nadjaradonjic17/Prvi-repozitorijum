import customtkinter as ctk


ctk.set_appearance_mode("light")  # ili "dark"
ctk.set_default_color_theme("blue")

prozor = ctk.CTk()
prozor.title("Biblioteka")
prozor.geometry("700x600")


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


def prikazi_knjige():
    tekstbox.delete("0.0", "end")
    for naslov, autor in knjige_autori.items():
        status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
        tekstbox.insert("end", f"{naslov} - {autor} ({status})\n")

def pretrazi_knjigu():
    upit = unos.get().lower()
    tekstbox.delete("0.0", "end")
    for naslov, autor in knjige_autori.items():
        if upit in naslov.lower():
            status = "Dostupna" if status_knjige[naslov] else "Pozajmljena"
            tekstbox.insert("end", f"{naslov} - {autor} ({status})\n")

def pozajmi_knjigu():
    naslov = unos.get()
    if naslov in knjige_autori:
        if status_knjige[naslov]:
            status_knjige[naslov] = False
            tekstbox.insert("end", f"✅ Knjiga '{naslov}' je uspješno pozajmljena.\n")
        else:
            tekstbox.insert("end", f"❌ Knjiga '{naslov}' je već pozajmljena.\n")
    else:
        tekstbox.insert("end", f"⚠️ Knjiga '{naslov}' ne postoji u sistemu.\n")

def vrati_knjigu():
    naslov = unos.get()
    if naslov in knjige_autori:
        if not status_knjige[naslov]:
            status_knjige[naslov] = True
            tekstbox.insert("end", f"✅ Knjiga '{naslov}' je uspješno vraćena.\n")
        else:
            tekstbox.insert("end", f"ℹ️ Knjiga '{naslov}' je već dostupna.\n")
    else:
        tekstbox.insert("end", f"⚠️ Knjiga '{naslov}' ne postoji u sistemu.\n")


naslov_label = ctk.CTkLabel(prozor, text="📚 Pretraži, pozajmi, vrati ili dodaj knjigu", font=ctk.CTkFont(size=18, weight="bold"))
naslov_label.pack(pady=15)


unos = ctk.CTkEntry(prozor, placeholder_text="Unesite naziv knjige", width=400)
unos.pack(pady=10)


frame_dugmad = ctk.CTkFrame(prozor)
frame_dugmad.pack(pady=10)

ctk.CTkButton(frame_dugmad, text="Pretraži", command=pretrazi_knjigu, width=150).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="Prikaži sve", command=prikazi_knjige, width=150).grid(row=0, column=1, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="Pozajmi", command=pozajmi_knjigu, width=150).grid(row=1, column=0, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="Vrati", command=vrati_knjigu, width=150).grid(row=1, column=1, padx=10, pady=5)


tekstbox = ctk.CTkTextbox(prozor, width=650, height=300)
tekstbox.pack(pady=15)


prozor.mainloop()
