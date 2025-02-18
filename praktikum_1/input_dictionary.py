def input_data(data_dict):
    print("\n=== Input Data ===")
    while True:
        key = input("Masukkan kunci (key): ")
        if key in data_dict:
            print("Kunci sudah ada! Gunakan kunci yang berbeda.")
            continue
            
        value = input("Masukkan nilai (value): ")
        data_dict[key] = value
        print("Data berhasil ditambahkan!")
        
        lanjut = input("\nIngin menambah data lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break

def cetak_data(data_dict):
    print("\n=== Data Dictionary ===")
    if len(data_dict) == 0:
        print("Dictionary masih kosong!")
    else:
        print("\nIsi Dictionary:")
        for key, value in data_dict.items():
            print(f"Key: {key} | Value: {value}")

def hitung_record(data_dict):
    print("\n=== Jumlah Record ===")
    jumlah = len(data_dict)
    print(f"Jumlah record dalam dictionary: {jumlah}")

def update_data(data_dict):
    print("\n=== Update Data ===")
    if len(data_dict) == 0:
        print("Dictionary masih kosong!")
        return
        
    cetak_data(data_dict)
    key = input("\nMasukkan kunci yang akan diupdate: ")
    
    if key in data_dict:
        value_baru = input("Masukkan nilai baru: ")
        data_dict[key] = value_baru
        print("Data berhasil diupdate!")
    else:
        print("Kunci tidak ditemukan!")

def delete_data(data_dict):
    print("\n=== Hapus Data ===")
    if len(data_dict) == 0:
        print("Dictionary masih kosong!")
        return
        
    cetak_data(data_dict)
    key = input("\nMasukkan kunci yang akan dihapus: ")
    
    if key in data_dict:
        del data_dict[key]
        print("Data berhasil dihapus!")
    else:
        print("Kunci tidak ditemukan!")

data_dict = {}
    
while True:
    print("\n=== Program Manajemen Dictionary ===")
    print("1. Input Data")
    print("2. Cetak Data")
    print("3. Hitung Jumlah Record")
    print("4. Update Data")
    print("5. Hapus Data")
    print("6. Keluar")
        
    pilihan = input("\nPilih menu (1-6): ")
        
    if pilihan == '1':
        input_data(data_dict)
    elif pilihan == '2':
        cetak_data(data_dict)
    elif pilihan == '3':
        hitung_record(data_dict)
    elif pilihan == '4':
        update_data(data_dict)
    elif pilihan == '5':
        delete_data(data_dict)
    elif pilihan == '6':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-6.")