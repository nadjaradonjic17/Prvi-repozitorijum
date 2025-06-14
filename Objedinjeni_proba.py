import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1000x600")
app.title("📚 Biblioteka")

# ------------------- PODACI -------------------
korisnici_fajl = "korisnici.json"
zaduzenja_fajl = "zaduzenja.json"

if os.path.exists(korisnici_fajl):
    with open(korisnici_fajl, "r") as f:
        korisnici = json.load(f)
else:
    korisnici = {}

if os.path.exists(zaduzenja_fajl):
    with open(zaduzenja_fajl, "r") as f:
        zaduzenja = json.load(f)
else:
    zaduzenja = {}

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
    "Ponos i predrasude": "Džejn Austen",
    "Lovac u žitu": "Dž. D. Selindžer",
    "Na zapadu ništa novo": "Erich Maria Remarque",
    "Veliki Getsbi": "F. Skot Ficdžerald",
    "Zov divljine": "Džek London",
    "Mrtve duše": "Nikolaj Gogolj",
    "Braća Karamazovi": "Fjodor Dostojevski",
    "Božanstvena komedija": "Dante Aligijeri",
    "Čarobnjak iz Oza": "L. Frank Baum"
}
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
        zaduzenja.setdefault(ulogovan_korisnik, []).extend(odabrane)
        with open(zaduzenja_fajl, "w") as f:
            json.dump(zaduzenja, f)
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
            if knjiga in zaduzenja.get(ulogovan_korisnik, []):
                zaduzenja[ulogovan_korisnik].remove(knjiga)
        with open(zaduzenja_fajl, "w") as f:
            json.dump(zaduzenja, f)
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

def prikazi_moje_knjige():
    if not ulogovan_korisnik:
        messagebox.showerror("Greška", "Morate biti prijavljeni.")
        return
    moje = zaduzenja.get(ulogovan_korisnik, [])
    if not moje:
        messagebox.showinfo("Info", "Niste zadužili nijednu knjigu.")
        return
    filtrirane = {k: knjige_autori[k] for k in moje}
    prikazi_knjige(filtrirane)

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
ctk.CTkButton(meni_frame, text="📚 Moje knjige", command=prikazi_moje_knjige).pack(pady=5)
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

ctk.CTkLabel(auth_frame, text="Korisničko ime").pack(pady=(20, 5), padx=5)
username_entry = ctk.CTkEntry(auth_frame, width=100)
username_entry.pack(pady=5, padx=5)

ctk.CTkLabel(auth_frame, text="Lozinka").pack(pady=5, padx=5)
password_entry = ctk.CTkEntry(auth_frame, width=100, show="*")
password_entry.pack(pady=5, padx=5)

ctk.CTkButton(auth_frame, text="Prijavi se", command=login).pack(pady=10, padx=5, fill="x")
ctk.CTkButton(auth_frame, text="Registruj se", command=signup).pack(pady=5, padx=5, fill="x")

prikazi_knjige()

app.mainloop()
