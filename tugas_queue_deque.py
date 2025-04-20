from collections import deque

antrian_cuci_mobil = deque()
jumlah_mobil_keluar = 0
tarif_cuci = 50000

def tampilkan_menu():
    print("\n=== MENU ANTRIAN CUCI MOBIL ===")
    print("1. Input antrian cuci mobil")
    print("2. Cetak antrian cuci mobil")
    print("3. Keluarkan antrian terdepan yang sudah selesai")
    print("4. Hitung total pembayaran terkini")
    print("5. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama_mobil = input("Masukkan nama/plat mobil: ")
        antrian_cuci_mobil.append(nama_mobil)
        print(f"Mobil '{nama_mobil}' telah masuk ke antrian.")

    elif pilihan == "2":
        if not antrian_cuci_mobil:
            print("Antrian kosong.")
        else:
            print("Daftar antrian cuci mobil:")
            for i, mobil in enumerate(antrian_cuci_mobil, start=1):
                print(f"{i}. {mobil}")

    elif pilihan == "3":
        if not antrian_cuci_mobil:
            print("Tidak ada mobil dalam antrian.")
        else:
            mobil_selesai = antrian_cuci_mobil.popleft()
            jumlah_mobil_keluar += 1
            print(f"Mobil '{mobil_selesai}' telah selesai dicuci dan keluar dari antrian.")

    elif pilihan == "4":
        total_pembayaran = jumlah_mobil_keluar * tarif_cuci
        print(f"Total mobil yang telah dicuci: {jumlah_mobil_keluar}")
        print(f"Total pembayaran terkini: Rp{total_pembayaran:,}")

    elif pilihan == "5":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-5.")
