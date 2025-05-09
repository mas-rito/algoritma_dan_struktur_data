from collections import deque
from tabulate import tabulate
from colorama import Fore
import questionary

# Struktur Data
contacts = {}  # dictionary utama
riwayat_hubungi = deque() # kotak yang sudah dihubungi

# Fungsi hashing untuk kategorisasi nama
def hash_nama(nama):
    return ord(nama[0].lower()) % 26

def header(text):
    print()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + f"{text.center(50)}")
    print(Fore.CYAN + "=" * 50)
    print()

# Tambah kontak baru
def tambah_kontak():
    while True:
        nama = questionary.text("Masukkan nama:").ask()
        if nama in contacts:
            print(Fore.RED + "Kontak sudah ada.")
            return
        telepon = questionary.text("Masukkan nomor telepon:").ask()
        contacts[nama] = {"telepon": telepon}
        print(Fore.GREEN + f"Kontak '{nama}' berhasil ditambahkan!")

        pilihan = questionary.select("Tambah kontak lagi?", choices=["Ya", "Tidak"]).ask()
        if pilihan == "Tidak":
            break
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")

# Tampilkan semua kontak
def tampilkan_kontak():
    if not contacts:
        print(Fore.YELLOW + "Tidak ada kontak untuk ditampilkan.")
        return
    tabel = [[nama, data['telepon']] for nama, data in contacts.items()]
    print(tabulate(tabel, headers=["Nama", "Telepon"], tablefmt="grid"))
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")


# Cari kontak
def cari_kontak():
    while True:
        if not contacts:
            print(Fore.YELLOW + "Kontak masih kosong.")
            return
        keyword = questionary.text("Masukkan nama yang ingin dicari:").ask()
        hasil = []
        for nama, data in contacts.items():
            if keyword.lower() in nama.lower():
                hasil.append([nama, data['telepon']])
        if hasil:
            print(Fore.GREEN + "Hasil pencarian:")
            print(tabulate(hasil, headers=["Nama", "Telepon"], tablefmt="grid"))

            pilihan = questionary.select("Cari kontak lagi?", choices=["Ya", "Tidak"]).ask()
            if pilihan == "Tidak":
                break
        else:
            print(Fore.RED + "Kontak tidak ditemukan.")
            break
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")

# Urutkan kontak
def urutkan_kontak():
    if not contacts:
        print(Fore.YELLOW + "Kontak kosong.")
        return
    pilihan = questionary.select("Urutkan berdasarkan:", choices=["Nama", "Nomor Telepon"]).ask()
    if pilihan == "Nama":
        sorted_items = sorted(contacts.items())
    else:
        sorted_items = sorted(contacts.items(), key=lambda x: x[1]['telepon'])
    tabel = [[nama, data['telepon']] for nama, data in sorted_items]
    print(Fore.CYAN + "Kontak setelah diurutkan:")
    print(tabulate(tabel, headers=["Nama", "Telepon"], tablefmt="grid"))
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")

# Hapus kontak
def hapus_kontak():
    while True:
        if not contacts:
            print(Fore.YELLOW + "Kontak kosong.")
            return
        nama = questionary.text("Masukkan nama kontak yang ingin dihapus:").ask()
        if nama in contacts:
            del contacts[nama]
            print(Fore.GREEN + f"Kontak '{nama}' berhasil dihapus.")

            pilihan = questionary.select("Hapus kontak lagi?", choices=["Ya", "Tidak"]).ask()
            if pilihan == "Tidak":
                break
        else:
            print(Fore.RED + "Kontak tidak ditemukan.")
            break
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")

# Hubungi kontak
def hubungi_kontak():
    if not contacts:
        print(Fore.YELLOW + "Kontak masih kosong.")
        return
    nama = questionary.text("Masukkan nama kontak yang ingin dihubungi:").ask()
    if nama in contacts:
        riwayat_hubungi.append(nama)
        print(Fore.GREEN + f"Kontak '{nama}' berhasil dihubungi.")
    else:
        print(Fore.RED + "Kontak tidak ditemukan.")
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")

# Tampilkan daftar antrian (queue)
def tampilkan_riwayat_hubungi():
    if not riwayat_hubungi :
        print(Fore.YELLOW + "Daftar hubungi masih kosong.")
        return
    print(Fore.CYAN + "Daftar hubungi:")
    for i, nama in enumerate(riwayat_hubungi, start=1):
        print(f"{i}. {nama}")
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")

def hapus_riwayat_hubungi():
    if not riwayat_hubungi:
        print(Fore.YELLOW + "Daftar hubungi masih kosong.")
        print()
        input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")
        return
    while True:
        pilihan = questionary.select("Hapus daftar hubungi?", choices=["Hapus paling atas saja", "Hapus semuanya", "Batal hapus"]).ask()
        if pilihan == "Batal hapus":
            break
        elif pilihan == "Hapus paling atas saja":
            nama_kontak = riwayat_hubungi.popleft()
            print(Fore.GREEN + f"riwayat hubungi '{nama_kontak}' berhasil dihapus.")

            if not riwayat_hubungi:
                print()
                print(Fore.YELLOW + "Daftar hubungi sudah kosong.")
                break
            else:
                hapus_lagi = questionary.select("Hapus lagi?", choices=["Ya", "Tidak"]).ask()
                if hapus_lagi == "Tidak":
                    break
                else:
                    continue
        elif pilihan == "Hapus semuanya":
            riwayat_hubungi.clear()
            print(Fore.GREEN + "Daftar hubungi berhasil dihapus.")
            break
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk melanjutkan...")