def input_set():
    print("\n=== Input Data Set ===")
    data_set = set()
    while True:
        print("\nMenu Set:")
        print("1. Tambah elemen")
        print("2. Lihat set")
        print("3. Kembali ke menu utama")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            elemen = input("Masukkan elemen: ")
            data_set.add(elemen)
            print("Elemen berhasil ditambahkan!")
        elif pilihan == '2':
            if len(data_set) == 0:
                print("Set masih kosong!")
            else:
                print("Isi set:", data_set)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid!")
    return data_set

def input_tuple():
    print("\n=== Input Data Tuple ===")
    data_list = []
    while True:
        print("\nMenu Tuple:")
        print("1. Tambah elemen")
        print("2. Lihat tuple")
        print("3. Kembali ke menu utama")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            elemen = input("Masukkan elemen: ")
            data_list.append(elemen)
            print("Elemen berhasil ditambahkan!")
        elif pilihan == '2':
            if len(data_list) == 0:
                print("Tuple masih kosong!")
            else:
                data_tuple = tuple(data_list)
                print("Isi tuple:", data_tuple)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid!")
    return tuple(data_list)

def input_string():
    print("\n=== Input Data String ===")
    data_string = ""
    while True:
        print("\nMenu String:")
        print("1. Input string baru")
        print("2. Tambah string (concatenate)")
        print("3. Lihat string")
        print("4. Kembali ke menu utama")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            data_string = input("Masukkan string baru: ")
            print("String berhasil diperbarui!")
        elif pilihan == '2':
            tambahan = input("Masukkan string tambahan: ")
            data_string += tambahan
            print("String berhasil ditambahkan!")
        elif pilihan == '3':
            if data_string == "":
                print("String masih kosong!")
            else:
                print("Isi string:", data_string)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid!")
    return data_string


set_data = set()
tuple_data = ()
string_data = ""

while True:
    print("\n=== Program Input Data Dinamis ===")
    print("1. Input/Edit Set")
    print("2. Input/Edit Tuple")
    print("3. Input/Edit String")
    print("4. Lihat Semua Data")
    print("5. Keluar")
        
    pilihan = input("\nPilih menu (1-5): ")
        
    if pilihan == '1':
        set_data = input_set()
    elif pilihan == '2':
        tuple_data = input_tuple()
    elif pilihan == '3':
        string_data = input_string()
    elif pilihan == '4':
        print("\nIsi Set:", set_data)
        print("Isi Tuple:", tuple_data)
        print("Isi String:", string_data)
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid!")