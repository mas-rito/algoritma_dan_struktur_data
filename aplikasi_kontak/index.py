import questionary
from colorama import Fore, init
from menu import tambah_kontak, tampilkan_kontak, cari_kontak, urutkan_kontak, hapus_kontak, hubungi_kontak, tampilkan_riwayat_hubungi,hapus_riwayat_hubungi, header
import os

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menjalankan menu utama
def main():

    options = [
        "📥 Tambah Kontak",
        "📂 Lihat Semua Kontak",
        "🔍 Cari Kontak",
        "🔢 Urutkan Kontak",
        "📤 Hapus Kontak",
        "📲 Hubungi Kontak",
        "📃 Lihat Riwayat Hubungi",
        "📤 Hapus Riwayat Hubungi",
        "🚪 Keluar"
    ]

    while True:
        clear_screen()
        header("📞 APLIKASI KONTAK")
        pilihan = questionary.select("Pilih menu:", choices=options, use_shortcuts=True).ask()
        index = options.index(pilihan)

        match index:
            case 0: tambah_kontak()
            case 1: tampilkan_kontak()
            case 2: cari_kontak()
            case 3: urutkan_kontak()
            case 4: hapus_kontak()
            case 5: hubungi_kontak()
            case 6: tampilkan_riwayat_hubungi()
            case 7: hapus_riwayat_hubungi()
            case 8:
                print(Fore.GREEN + "Terima kasih telah menggunakan aplikasi ini!")
                break

main()
