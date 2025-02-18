def tampilkan_matriks(matriks):
    for baris in matriks:
        print([round(elemen, 2) for elemen in baris])

def penjumlahan_matriks(matriks1, matriks2):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(baris)
    return hasil

def pengurangan_matriks(matriks1, matriks2):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(matriks1[i][j] - matriks2[i][j])
        hasil.append(baris)
    return hasil

def perkalian_matriks(matriks1, matriks2):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            elemen = sum(matriks1[i][k] * matriks2[k][j] for k in range(2))
            baris.append(elemen)
        hasil.append(baris)
    return hasil


while True:
        print("\n=== Program Operasi Matriks 2x2 ===")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Keluar")
        
        pilihan = input("\nPilih operasi (1-4): ")
        
        if pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
            
        if pilihan in ['1', '2', '3']:
            matriks1 = [[1, 2], [3, 4]]
            matriks2 = [[5, 6], [7, 8]]
            
            print("\nMatriks 1:")
            tampilkan_matriks(matriks1)
            print("\nMatriks 2:")
            tampilkan_matriks(matriks2)
            
            if pilihan == '1':
                hasil = penjumlahan_matriks(matriks1, matriks2)
                print("\nHasil Penjumlahan:")
            elif pilihan == '2':
                hasil = pengurangan_matriks(matriks1, matriks2)
                print("\nHasil Pengurangan:")
            else:
                hasil = perkalian_matriks(matriks1, matriks2)
                print("\nHasil Perkalian:")
                
            tampilkan_matriks(hasil)
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-4.")