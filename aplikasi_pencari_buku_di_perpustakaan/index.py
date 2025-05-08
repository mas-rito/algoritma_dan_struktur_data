from collections import deque
from colorama import init, Fore
import questionary

from utility import clear_screen, header
from menu import tambah_buku, cari_buku_judul, tampilkan_semua_buku, cari_lokasi_buku, lihat_riwayat_pencarian, tambah_antrian_pinjam, proses_antrian_pinjam

# Inisialisasi colorama
init(autoreset=True)


def show_menu():
        clear_screen()

        # Cetak header 3 baris
        header("📚 APLIKASI PENCARI BUKU PERPUSTAKAAN")
        print(Fore.YELLOW + "Gunakan panah ↑↓ untuk memilih, tekan ENTER untuk konfirmasi:\n")

        # Menu utama
        options = [
        "📘 Tambah buku",
        "🔍 Cari buku berdasarkan judul",
        "📂 Tampilkan semua buku",
        "📌 Cari lokasi buku",
        "🕓 Lihat riwayat pencarian",
        "📥 Tambah ke antrian pinjam",
        "📦 Proses antrian pinjam",
        "🚪 Keluar"
        ]

        # Menggunakan questionary untuk menampilkan menu
        selected = questionary.select(
            "Silakan pilih menu:",
            choices=options,
            use_shortcuts=True
        ).ask()

        index = options.index(selected)

        return index

def main():
        functions = [
            tambah_buku,
            cari_buku_judul,
            tampilkan_semua_buku,
            cari_lokasi_buku,
            lihat_riwayat_pencarian,
            tambah_antrian_pinjam,
            proses_antrian_pinjam
        ]

        while True:
            pilihan = show_menu()

            if pilihan == 7:
                print(Fore.MAGENTA + "\n👋 Terima kasih telah menggunakan aplikasi!")
                break
            else:
                    functions[pilihan]()
                    input(Fore.YELLOW + "\nTekan ENTER untuk kembali ke menu...")

main()
