from collections import deque
from colorama import Fore
import questionary

from utility import header

# Data awal
books = []
hash_rak = {}
riwayat_pencarian = []
antrian_pinjam = deque()

# Fungsi-fungsi
def tambah_buku():
    header("📘 TAMBAH BUKU BARU")
    kode = input("Masukkan kode buku        : ").upper()
    judul = input("Masukkan judul buku       : ")
    pengarang = input("Masukkan nama pengarang   : ")
    rak = input("Masukkan lokasi rak       : ").upper()
    
    buku = {"kode": kode, "judul": judul, "pengarang": pengarang, "rak": rak}
    books.append(buku)
    hash_rak[kode] = rak
    print(Fore.GREEN + "✅ Buku berhasil ditambahkan!\n")

def cari_buku_judul():
    header("🔍 CARI BUKU BERDASARKAN JUDUL")
    keyword = input("Masukkan keyword judul: ").lower()
    riwayat_pencarian.append(keyword)
    
    hasil = [b for b in books if keyword in b["judul"].lower()]
    
    if hasil:
        print(Fore.GREEN + "\n📚 Hasil pencarian:")
        for b in hasil:
            print(Fore.WHITE + f"{b['kode']} - {b['judul']} oleh {b['pengarang']} (Rak {b['rak']})")
    else:
        print(Fore.RED + "❌ Buku tidak ditemukan.")
    print()

def tampilkan_semua_buku():
    header("📂 DAFTAR SELURUH BUKU")
    if not books:
        print(Fore.RED + "Tidak ada buku yang tersedia.\n")
        return

    sorted_books = sorted(books, key=lambda x: x["judul"].lower())
    for i, b in enumerate(sorted_books, start=1):
        print(Fore.WHITE + f"{i}. {b['kode']} - {b['judul']} oleh {b['pengarang']} (Rak {b['rak']})")
    print()

def cari_lokasi_buku():
    header("📌 CARI LOKASI BUKU")
    kode = input("Masukkan kode buku: ").upper()
    lokasi = hash_rak.get(kode)
    if lokasi:
        print(Fore.GREEN + f"Buku dengan kode {kode} berada di rak {lokasi}\n")
    else:
        print(Fore.RED + "❌ Kode buku tidak ditemukan.\n")

def lihat_riwayat_pencarian():
    header("🕓 RIWAYAT PENCARIAN")
    if not riwayat_pencarian:
        print(Fore.YELLOW + "Belum ada riwayat pencarian.\n")
    else:
        for i, keyword in enumerate(reversed(riwayat_pencarian), start=1):
            print(f"{i}. {keyword}")
        print()

def tambah_antrian_pinjam():
    header("📥 TAMBAH KE ANTRIAN PINJAM")
    kode = input("Masukkan kode buku untuk dipinjam: ").upper()
    if any(b["kode"] == kode for b in books):
        antrian_pinjam.append(kode)
        print(Fore.GREEN + f"Buku {kode} ditambahkan ke antrian peminjaman.\n")
    else:
        print(Fore.RED + "❌ Kode buku tidak ditemukan.\n")

def proses_antrian_pinjam():
    header("📦 PROSES PEMINJAMAN")
    if antrian_pinjam:
        antrian_pertama = antrian_pinjam[0]
        print(Fore.GREEN + f"Buku {antrian_pertama} sedang diproses untuk dipinjam.\n")

        options = [
            "Dipinjamkan",
            "Tidak dipinjamkan"
        ]

        selected = questionary.select(
            "Apakah buku ini dipinjamkan?",
            choices=options
        ).ask()

        if selected == "Dipinjamkan":
            antrian_pinjam.popleft()
            print(Fore.GREEN + "✅ Buku berhasil dipinjamkan.\n")
        else:
            print(Fore.RED + "❌ Buku tidak dipinjamkan.\n")

    else:
        print(Fore.YELLOW + "Tidak ada antrian peminjaman.\n")
