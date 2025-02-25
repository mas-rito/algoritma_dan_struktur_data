def input_ordo_matriks():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    return baris, kolom

def input_data_matriks(baris, kolom):
    matriks = []
    print("Masukkan data matriks:")
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            nilai = int(input(f"Data [{i}][{j}]: "))
            baris_matriks.append(nilai)
        matriks.append(baris_matriks)
    return matriks

def tampilkan_matriks(matriks):
    print("\nMatriks yang dimasukkan:")
    for baris in matriks:
        for nilai in baris:
            print(nilai, end="\t")
        print()

def cari_indeks_bilangan(matriks, nilai_cari):
    for i in range(len(matriks)):
        for j in range(len(matriks[i])):
            if matriks[i][j] == nilai_cari:
                return True, i, j  # Nilai ditemukan, mengembalikan posisi
    
    # Jika nilai tidak ditemukan
    return False, -1, -1

def main():
    # Memanggil fungsi input ordo matriks
    baris, kolom = input_ordo_matriks()
    
    # Memanggil fungsi input data matriks
    matriks = input_data_matriks(baris, kolom)
    
    # Menampilkan matriks
    tampilkan_matriks(matriks)
    
    # Menu pencarian data
    lanjut = 'y'
    while lanjut.lower() == 'y':
        nilai_cari = int(input("\nNilai yang dicari: "))
        
        # Memanggil fungsi pencarian indeks bilangan
        ketemu, posisi_baris, posisi_kolom = cari_indeks_bilangan(matriks, nilai_cari)
        
        # Menampilkan hasil pencarian
        if ketemu:
            print(f"output: data {nilai_cari} berada pada posisi [{posisi_baris}][{posisi_kolom}]")
        else:
            print(f"output: data {nilai_cari} tidak ditemukan dalam matriks")
        
        lanjut = input("Cari lagi? (y/n): ")
    
    print("Program selesai")


main()