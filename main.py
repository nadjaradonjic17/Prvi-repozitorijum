import customtkinter as ctk
<<<<<<< HEAD
from tkinter import messagebox
=======
>>>>>>> 9ff08856eca99195e7fdddba40f4cfe45c92279e
import json
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

<<<<<<< HEAD
app = ctk.CTk()
app.geometry("1000x600")
app.title("📚 Biblioteka")

# ------------------- PODACI -------------------
korisnici_fajl = "korisnici.json"

if os.path.exists(korisnici_fajl):
    with open(korisnici_fajl, "r") as f:
        korisnici = json.load(f)
else:
    korisnici = {}

=======
prozor = ctk.CTk()
prozor.title("📚 Biblioteka")
prozor.geometry("700x700")

naslov_font = ("Helvetica", 16, "bold")
tekst_font = ("Helvetica", 12)

>>>>>>> 9ff08856eca99195e7fdddba40f4cfe45c92279e
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
<<<<<<< HEAD
    "Ponos i predrasude": "Džejn Austen",
=======
    "Ponos i predrasude": "Džejn Ostin",
>>>>>>> 9ff08856eca99195e7fdddba40f4cfe45c92279e
    "Lovac u žitu": "Dž. D. Selindžer",
    "Na zapadu ništa novo": "Erich Maria Remarque",
    "Veliki Getsbi": "F. Skot Ficdžerald",
    "Zov divljine": "Džek London",
    "Mrtve duše": "Nikolaj Gogolj",
    "Braća Karamazovi": "Fjodor Dostojevski",
    "Božanstvena komedija": "Dante Aligijeri",
    "Čarobnjak iz Oza": "L. Frank Baum"
}
<<<<<<< HEAD
status_knjige = {naslov: True for naslov in knjige_autori}

ulogovan_korisnik = None

# ------------------- FUNKCIJE -------------------
def prikazi_knjige(knjige=None):
    for widget in knjige_list_frame.winfo_children():
        widget.destroy()

    prikaz = knjige or knjige_autori
    for naslov, autor in prikaz.items():
        status = "✅" if status_knjige[naslov] else "❌"
        label = ctk.CTkLabel(knjige_list_frame, text=f"{naslov} - {autor} ({status})", anchor="w")
        label.pack(fill="x", padx=10, pady=2)

def login():
    global ulogovan_korisnik
    username = username_entry.get()
    password = password_entry.get()

    if username in korisnici and korisnici[username] == password:
        ulogovan_korisnik = username
        messagebox.showinfo("Uspeh", "Uspešno prijavljeni!")
        prikazi_knjige()
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    else:
        messagebox.showerror("Greška", "Pogrešno korisničko ime ili lozinka!")

def signup():
    global ulogovan_korisnik
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Greška", "Unesite korisničko ime i lozinku.")
        return

    if username in korisnici:
        messagebox.showerror("Greška", "Korisnik već postoji.")
    else:
        korisnici[username] = password
        with open(korisnici_fajl, "w") as f:
            json.dump(korisnici, f)
        ulogovan_korisnik = username
        messagebox.showinfo("Uspeh", "Uspešno registrovani!")
        prikazi_knjige()
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

def pretrazi_knjigu():
    upit = ctk.CTkInputDialog(title="Pretraga", text="Unesi naziv knjige ili autora:").get_input()
    if upit:
        filtrirano = {k: v for k, v in knjige_autori.items() if upit.lower() in k.lower() or upit.lower() in v.lower()}
        if filtrirano:
            prikazi_knjige(filtrirano)
        else:
            messagebox.showinfo("Rezultat", "Nema rezultata pretrage.")

def pozajmi_knjige_dialog():
    global ulogovan_korisnik
    if not ulogovan_korisnik:
        messagebox.showerror("Greška", "Morate biti prijavljeni da biste pozajmili knjige.")
        return

    prozor = ctk.CTkToplevel(app)
    prozor.title("📥 Pozajmi knjige")
    prozor.geometry("400x500")
    prozor.transient(app)
    prozor.grab_set()
    prozor.focus()

    check_vars = {}

    okvir = ctk.CTkScrollableFrame(prozor)
    okvir.pack(pady=10, padx=10, fill="both", expand=True)

    for naslov, autor in knjige_autori.items():
        if status_knjige[naslov]:
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(okvir, text=f"{naslov} - {autor}", variable=var)
            check.pack(anchor="w", pady=2)
            check_vars[naslov] = var

    def potvrdi():
        odabrane = [k for k, v in check_vars.items() if v.get()]
        if not odabrane:
            messagebox.showwarning("Upozorenje", "Niste izabrali nijednu knjigu.")
            return
        for knjiga in odabrane:
            status_knjige[knjiga] = False
        messagebox.showinfo("Uspeh", f"Pozajmljene knjige: {', '.join(odabrane)}")
        prikazi_knjige()
        prozor.destroy()

    ctk.CTkButton(prozor, text="📥 Pozajmi odabrane", command=potvrdi).pack(pady=10)

def vrati_knjige_dialog():
    global ulogovan_korisnik
    if not ulogovan_korisnik:
        messagebox.showerror("Greška", "Morate biti prijavljeni da biste vratili knjige.")
        return

    prozor = ctk.CTkToplevel(app)
    prozor.title("📤 Vrati knjige")
    prozor.geometry("400x500")
    prozor.transient(app)
    prozor.grab_set()
    prozor.focus()

    check_vars = {}

    okvir = ctk.CTkScrollableFrame(prozor)
    okvir.pack(pady=10, padx=10, fill="both", expand=True)

    for naslov, autor in knjige_autori.items():
        if not status_knjige[naslov]:
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(okvir, text=f"{naslov} - {autor}", variable=var)
            check.pack(anchor="w", pady=2)
            check_vars[naslov] = var

    def potvrdi():
        odabrane = [k for k, v in check_vars.items() if v.get()]
        if not odabrane:
            messagebox.showwarning("Upozorenje", "Niste izabrali nijednu knjigu.")
            return
        for knjiga in odabrane:
            status_knjige[knjiga] = True
        messagebox.showinfo("Uspeh", f"Vraćene knjige: {', '.join(odabrane)}")
        prikazi_knjige()
        prozor.destroy()

    ctk.CTkButton(prozor, text="📤 Vrati odabrane", command=potvrdi).pack(pady=10)

def sortiraj_naslov():
    sortirano = dict(sorted(knjige_autori.items()))
    prikazi_knjige(sortirano)

def sortiraj_autor():
    sortirano = dict(sorted(knjige_autori.items(), key=lambda item: item[1]))
    prikazi_knjige(sortirano)

def prikazi_statistiku():
    ukupno = len(knjige_autori)
    dostupne = sum(1 for dostupna in status_knjige.values() if dostupna)
    pozajmljene = ukupno - dostupne
    messagebox.showinfo("📊 Statistika", f"Ukupno knjiga: {ukupno}\nDostupne: {dostupne}\nPozajmljene: {pozajmljene}")

def logout():
    global ulogovan_korisnik
    if ulogovan_korisnik:
        ulogovan_korisnik = None
        messagebox.showinfo("Odjava", "Uspešno ste se odjavili.")
    else:
        messagebox.showinfo("Odjava", "Niste prijavljeni.")

# ------------------- INTERFEJS -------------------
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# ------- Lijeva kolona (meni) -------
meni_frame = ctk.CTkFrame(main_frame)
meni_frame.pack(side="left", fill="y", padx=10, pady=10)

ctk.CTkLabel(meni_frame, text="📖 Meni", font=("Helvetica", 16, "bold")).pack(pady=10)
ctk.CTkButton(meni_frame, text="Prikaži sve", command=lambda: prikazi_knjige()).pack(pady=5)
ctk.CTkButton(meni_frame, text="Pretraži", command=pretrazi_knjigu).pack(pady=5)
ctk.CTkButton(meni_frame, text="📥 Pozajmi", command=pozajmi_knjige_dialog).pack(pady=5)
ctk.CTkButton(meni_frame, text="📤 Vrati", command=vrati_knjige_dialog).pack(pady=5)
ctk.CTkButton(meni_frame, text="Sortiraj po naslovu", command=sortiraj_naslov).pack(pady=5)
ctk.CTkButton(meni_frame, text="Sortiraj po autoru", command=sortiraj_autor).pack(pady=5)
ctk.CTkButton(meni_frame, text="Statistika", command=prikazi_statistiku).pack(pady=5)
ctk.CTkButton(meni_frame, text="Logout", fg_color="red", command=logout).pack(pady=15)

# ------- Centralna kolona (prikaz knjiga) -------
knjige_list_frame = ctk.CTkScrollableFrame(main_frame)
knjige_list_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# ------- Desna kolona (prijava / registracija) -------
auth_frame = ctk.CTkFrame(main_frame)
auth_frame.pack(side="left", fill="y", padx=10, pady=10)

ctk.CTkLabel(auth_frame, text="Korisničko ime").pack()
username_entry = ctk.CTkEntry(auth_frame, width=100)
username_entry.pack(pady=5, padx=5)

ctk.CTkLabel(auth_frame, text="Lozinka").pack()
password_entry = ctk.CTkEntry(auth_frame, width=100, show="*")
password_entry.pack(pady=5, padx=5)

ctk.CTkButton(auth_frame, text="Prijavi se", command=login).pack(pady=10, padx=5, fill="x")
ctk.CTkButton(auth_frame, text="Registruj se", command=signup).pack(pady=5, padx=5, fill="x")

prikazi_knjige()

app.mainloop()
=======

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

#Sortiranje
def sortiraj_po_naslovu():
    global trenutno_prikazane_knjige
    trenutno_prikazane_knjige.sort()
    prikazi_sortirane()

def sortiraj_po_autoru():
    global trenutno_prikazane_knjige
    trenutno_prikazane_knjige.sort(key=lambda x: x[1])
    prikazi_sortirane()

def prikazi_sortirane():
    tekstbox.delete("1.0", "end")
    for naslov, autor in trenutno_prikazane_knjige:
        status = "✅ Dostupna" if status_knjige[naslov] else "❌ Pozajmljena"
        tekstbox.insert("end", f"{naslov} - {autor} ({status})\n")

ctk.CTkButton(frame_dugmad, text="Sortiraj po naslovu", command=sortiraj_po_naslovu, width=150).grid(row=2, column=0, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="Sortiraj po autoru", command=sortiraj_po_autoru, width=150).grid(row=2, column=1, padx=10, pady=5)

#Filtriranje
def prikazi_dostupne():
    tekstbox.delete("1.0", "end")
    for naslov, autor in knjige_autori.items():
        if status_knjige[naslov]:
            tekstbox.insert("end", f"{naslov} - {autor} (✅ Dostupna)\n")

def prikazi_pozajmljene():
    tekstbox.delete("1.0", "end")
    for naslov, autor in knjige_autori.items():
        if not status_knjige[naslov]:
            tekstbox.insert("end", f"{naslov} - {autor} (❌ Pozajmljena)\n")

ctk.CTkButton(frame_dugmad, text="Dostupne", command=prikazi_dostupne, width=150).grid(row=3, column=0, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="Pozajmljene", command=prikazi_pozajmljene, width=150).grid(row=3, column=1, padx=10, pady=5)

#Statistika
def prikazi_statistiku():
    ukupno = len(knjige_autori)
    dostupne = sum(1 for v in status_knjige.values() if v)
    pozajmljene = ukupno - dostupne
    tekstbox.insert("end", f"\n📊 Statistika:\nUkupno: {ukupno}\n✅ Dostupne: {dostupne}\n❌ Pozajmljene: {pozajmljene}\n")

ctk.CTkButton(frame_dugmad, text="📊 Statistika", command=prikazi_statistiku, width=310).grid(row=4, column=0, columnspan=2, pady=5)


def sacuvaj_stanje():
    with open("stanje_biblioteke.json", "w") as f:
        json.dump(status_knjige, f)
    tekstbox.insert("end", "💾 Stanje sačuvano.\n")

def ucitaj_stanje():
    if os.path.exists("stanje_biblioteke.json"):
        with open("stanje_biblioteke.json", "r") as f:
            podaci = json.load(f)
            for naslov in podaci:
                if naslov in status_knjige:
                    status_knjige[naslov] = podaci[naslov]
        tekstbox.insert("end", "📂 Stanje učitano.\n")
        prikazi_knjige()
    else:
        tekstbox.insert("end", "⚠️ Nema sačuvanog stanja.\n")

ctk.CTkButton(frame_dugmad, text="💾 Sačuvaj stanje", command=sacuvaj_stanje, width=150).grid(row=5, column=0, padx=10, pady=5)
ctk.CTkButton(frame_dugmad, text="📂 Učitaj stanje", command=ucitaj_stanje, width=150).grid(row=5, column=1, padx=10, pady=5)

tekstbox = ctk.CTkTextbox(prozor, width=650, height=300, font=tekst_font)
tekstbox.pack(pady=10)

ucitaj_stanje()
prozor.mainloop()
>>>>>>> 9ff08856eca99195e7fdddba40f4cfe45c92279e
