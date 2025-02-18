data_list = []
    
while True:
    print("\n=== Program Input Data List ===")
    print("1. Tambah data")
    print("2. Lihat semua data")
    print("3. Keluar")
        
    pilihan = input("\nPilih menu (1-3): ")
        
    if pilihan == '1':
        data_baru = input("Masukkan data: ")
        data_list.append(data_baru)
        print("Data berhasil ditambahkan!")
            
    elif pilihan == '2':
        if len(data_list) == 0:
            print("List masih kosong!")
        else:
            print("\nIsi data dalam list:")
            for index, data in enumerate(data_list, 1):
                print(f"{index}. {data}")
                    
    elif pilihan == '3':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-3.")