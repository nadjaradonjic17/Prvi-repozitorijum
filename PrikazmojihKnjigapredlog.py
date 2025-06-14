def prikazi_moje_knjige():
    if not ulogovan_korisnik:
        messagebox.showerror("Greška", "Morate biti prijavljeni.")
        return

    moje_knjige = zaduzenja.get(ulogovan_korisnik, [])
    if not moje_knjige:
        messagebox.showinfo("Informacija", "Nemate nijednu zaduženu knjigu.")
        return

    filtrirane_knjige = {naslov: knjige_autori[naslov] for naslov in moje_knjige}
    prikazi_knjige(filtrirane_knjige)
